import {
  AfterViewInit,
  Component,
  ElementRef,
  Input,
  OnInit,
  ViewChild,
} from '@angular/core';
import { Frame } from '../record-frame';
import {
  DetectorImageMode,
  KeyComboPressEventTypeEnum,
  KeyPressEventTypeEnum,
  KeyReleaseEventTypeEnum,
  MouseClickLeftEvent,
  MouseClickLeftEventTypeEnum,
  MousePressLeftEvent,
  MousePressLeftEventTypeEnum,
} from '@api/index';
import { environment } from '@environments/environment';
import { BaseComponent } from '@utils/base/base.component';
import { ImageAnnotatorBox } from '@train/image-annotator/image-annotator-box';
import { ImageAnnotatorHighlight } from '@train/image-annotator/image-annotator-highlight';
import { ImageAnnotatorSettings } from '@train/image-annotator/image-annotator-settings';
import { BehaviorSubject } from 'rxjs';


@Component({
  selector: 'app-record-frame',
  standalone: false,
  templateUrl: './record-frame.component.html',
  styleUrl: './record-frame.component.scss',
})
export class RecordFrameComponent
  extends BaseComponent
  implements AfterViewInit
{
  @Input() frame!: Frame;
  @Input() detectorId!: string;
  @Input() recordId!:string;
  highlights = new BehaviorSubject<ImageAnnotatorHighlight[]>([]);
  training: boolean = true;
  evaluating: boolean = true;
  testing: boolean = false;
  settings: ImageAnnotatorSettings = {
      resizeHandleSize: 10,
      selectedBorderColor: 'blue',
      defaultBorderColor: 'red',
      selectedColor: 'rgba(255,255,255,0.4)',
      defaultColor: 'rgba(255,255,255,0.2)',
      selectedHighlightBorderColor: 'blue',
      defaultHighlightBorderColor: 'red',
      selectedHighlightColor: 'rgba(255,255,255,0.4)',
      defaultHighlightColor: 'rgba(255,255,255,0.2)',
      showHighlights: true,
    };

  get imageUrl():string {
    return environment.imageUrl+this.recordId+'/'+this.frame.count.toString();
  }

  save(box:ImageAnnotatorBox) {
    // Converting the current image to blob
    if (this.detectorId && this.recordId) {
      let modes: DetectorImageMode[] = [];
      if (this.training){
        modes.push(DetectorImageMode.Train);
      }
      if (this.evaluating){
        modes.push(DetectorImageMode.Val);
      }
      if (this.testing){
        modes.push(DetectorImageMode.Test);
      }
      this.ctx.api.detector
        .detectorFrameUpload(
          this.recordId,
          this.detectorId,
          this.frame.count,
          modes
        )
        .subscribe({
          next: (result) => {
            this.setLoading(undefined);
            for (let i = 0; i < result.length; i++){
              let el = result[i];
            if (el._id) {
              let payloadAdd = {
                image_id: el._id,
                xstart: box.x,
                xend: box.x+box.w,
                ystart: box.y,
                yend: box.y+box.h,
                classes: box.classesToStringList(),
              }
              this.ctx.api.detector
                .detectorImageLabelAdd(payloadAdd)
                .subscribe({
                  next: (result2) => {
                    this.setLoading(undefined);
                  },
                  error: (result2) => {
                    this.setError(result2.error.detail);
                    this.setLoading(undefined);
                  },
                });
              }
            }
          },
          error: (result) => {
            this.setError(result.error.detail);
            this.setLoading(undefined);
          },
        });
    }
  }


  ngAfterViewInit(): void {
    setTimeout(()=>{

      this.load();
    })

  }


  objects(){
    if (!this.detectorId) return;
    this.ctx.api.detector.detectorFrameObjectsRecordid(this.recordId,this.detectorId,this.frame.count,0.1).subscribe({
      next: (result)=>{
        console.log(result);
      },
      error: (result)=>{
        console.log(result);
      }
    })
  }

  texts(){
    this.loading.next(this.ctx.translate.instant("workspace.record.frame.loading"));
    this.ctx.api.detector.detectorFrameTexts(this.recordId,this.frame.count,0.1).subscribe({
      next: (result)=>{
        console.log(result);
        let nh = this.highlights.getValue();
        result.forEach(text=>{
          nh.push(new ImageAnnotatorHighlight(text.x,text.y,text.w,text.h));
        })
        this.highlights.next(nh);

        this.loading.next(undefined);
      },
      error: (result)=>{
        console.log(result);
      }
    })
  }


  load() {
    if (!this.frame) return;
    if (!this.frame.event) return;
    let event = this.frame.event;
    this.loading.next(this.ctx.translate.instant("workspace.record.frame.loading"));
    if (event.type == KeyComboPressEventTypeEnum.KeyComboPress) {
    }
    switch (event.type) {
      case KeyComboPressEventTypeEnum.KeyComboPress:
        break;
      case KeyPressEventTypeEnum.KeyPress:
        break;
      case KeyReleaseEventTypeEnum.KeyRelease:
        break;
      case MouseClickLeftEventTypeEnum.MouseClickLeft:
        let evt = event as MouseClickLeftEvent;
        if (evt.position) {

          let x =  evt.position[0] - 20;
          let y = evt.position[1] - 20;
          let w = 40;
          let h =  40;
          let nh = this.highlights.getValue();

          nh.push(new ImageAnnotatorHighlight(x,y,w,h));
          this.highlights.next(nh);
        }

        break;
      case MousePressLeftEventTypeEnum.MousePressLeft:
        let evt2 = event as MousePressLeftEvent;
        if (evt2.position) {
          let x =  evt2.position[0] - 20;
          let y = evt2.position[1] - 20;
          let w = 40;
          let h =  40;
          let nh = this.highlights.getValue();
          nh.push(new ImageAnnotatorHighlight(x,y,w,h));
          this.highlights.next(nh);
        }
        break;
      default:
        break;
    }

    this.texts();

    this.loading.next(undefined);
  }


}
