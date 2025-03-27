import {
  AfterViewInit,
  Component,
  Input,
  OnDestroy,
  OnInit,
  Output,
} from '@angular/core';
import { Frame } from '../record-frame';
import {
  DetectorLabel,
  DetectorSuggestion,
  KeyComboPressEventTypeEnum,
  KeyPressEventTypeEnum,
  KeyReleaseEventTypeEnum,
  MouseClickLeftEvent,
  MouseClickLeftEventTypeEnum,
  MousePressLeftEvent,
  MousePressLeftEventTypeEnum,
  DetectObject,
  DetectText,
} from '@api/index';
import { environment } from '@environments/environment';
import { BaseComponent } from '@utils/base/base.component';
import { ImageAnnotatorBox } from '@train/image-annotator/image-annotator-box';
import { ImageAnnotatorSettings } from '@train/image-annotator/image-annotator-settings';
import { BehaviorSubject, Subscription } from 'rxjs';
import { DetectorLabelSelectComponent } from '@workspace/detector/detector-label-select/detector-label-select.component';
import { ImageAnnotatorHighlight } from '@train/image-annotator/image-annotator-highlight';

@Component({
  selector: 'app-record-frame',
  standalone: false,
  templateUrl: './record-frame.component.html',
  styleUrl: './record-frame.component.scss',
})
export class RecordFrameComponent
  extends BaseComponent
  implements AfterViewInit, OnInit, OnDestroy
{
  @Input() frame!: Frame;
  @Output() boxes = new BehaviorSubject<ImageAnnotatorBox[]>([]);
  @Output() highlights = new BehaviorSubject<ImageAnnotatorHighlight[]>([]);
  @Output() suggestions = new BehaviorSubject<DetectorSuggestion[]>([]);
  @Output() objects = new BehaviorSubject<DetectObject[]>([]);
  @Output() texts = new BehaviorSubject<DetectText[]>([]);

  subs = new Subscription();
  settings: ImageAnnotatorSettings = {
    resizeHandleSize: 10,
    showHighlights: true,
    canCreateBox: true,
  };


  get imageUrl(): string {
    return (
      environment.imageUrl + this.frame.lesson.record + '/' + this.frame.count.toString()
    );
  }

  ngOnDestroy(): void {
      this.subs.unsubscribe();
  }

  ngOnInit(): void {
      this.subs.add(this.boxes.subscribe(result=>{

      }))
  }

  selectClasses(box: ImageAnnotatorBox) {
    this.ctx
      .openModal<DetectorLabel[] | undefined>(DetectorLabelSelectComponent, {
        detectorId: this.frame.lesson.detector,
        selected: box.labels,
      })
      .subscribe({
        next: (result) => {
          if (result && result.length > 0) {
            box.labels = result;
            let boxes = this.boxes.getValue();
            this.boxes.next(boxes);
          }
        },
        error: (result) => {},
      });
  }

  ngAfterViewInit(): void {
    setTimeout(() => {
      this.load();
    });
  }

  detectObjects() {
    if (!this.frame.lesson.detector) return;
    this.ctx.api.detector
      .detectorObjectsFromFrame(
        this.frame.lesson.record,
        this.frame.lesson.detector,
        this.frame.count,
        0.1
      )
      .subscribe({
        next: (result) => {
          this.objects.next(result);
        },
        error: (result) => {
          console.log(result);
        },
      });
  }

  accept(suggestion: DetectorSuggestion) {

  }

  loadSuggestions() {
    if (!this.frame.event?._id) return;
    if (!this.frame.lesson.detector) return;
    this.ctx.api.detector
      .detectorFrameSuggestions(this.frame.lesson.detector, this.frame.event._id, 0.1)
      .subscribe({
        next: (result) => {
          let ret = this.highlights.getValue();
          this.suggestions.next(result);
          result.forEach((sug) => {
            let n = new ImageAnnotatorHighlight(sug.x, sug.y, sug.w, sug.h);
            n.defaultBorderColor = 'green';
            n.defaultBorderSize = 2;
            n.selectedBorderSize = 2;

            ret.push(n);
          });
          this.highlights.next(ret);
        },
        error: (result) => {
          console.log(result);
        },
      });
  }

  detectTexts() {
    this.loading.next(
      this.ctx.translate.instant('workspace.record.frame.loading')
    );
    this.ctx.api.detector
      .detectorFrameTexts(this.frame.lesson.record, this.frame.count, 0.1)
      .subscribe({
        next: (result) => {
          this.texts.next(result);
          this.loading.next(undefined);
        },
        error: (result) => {
          console.log(result);
        },
      });
  }

  load() {
    this.detectObjects();
    this.detectTexts();
    if (!this.frame) return;
    if (!this.frame.event) return;
    let event = this.frame.event;
    this.loadSuggestions();
    this.loading.next(
      this.ctx.translate.instant('workspace.record.frame.loading')
    );
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
          let x = evt.position[0] - 20;
          let y = evt.position[1] - 20;
          let w = 40;
          let h = 40;
          let nh = this.boxes.getValue();
          let evt_box = new ImageAnnotatorBox(x, y, w, h);
          evt_box.canResize = true;
          evt_box.canMove = false;
          nh.push(evt_box);
          this.boxes.next(nh);
        }

        break;
      case MousePressLeftEventTypeEnum.MousePressLeft:
        let evt2 = event as MousePressLeftEvent;
        if (evt2.position) {
          let x = evt2.position[0] - 20;
          let y = evt2.position[1] - 20;
          let w = 40;
          let h = 40;
          let nh = this.boxes.getValue();
          let evt_box = new ImageAnnotatorBox(x, y, w, h);
          evt_box.canResize = true;
          evt_box.canMove = false;
          nh.push(evt_box);
          this.boxes.next(nh);
        }
        break;
      default:
        break;
    }



    this.loading.next(undefined);
  }
}
