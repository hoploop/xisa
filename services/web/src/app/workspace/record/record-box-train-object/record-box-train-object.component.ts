import { Component, Input, OnInit } from '@angular/core';
import { DetectorLabel, TrainImageObject, TrainLesson } from '@api/index';
import { ImageAnnotatorBox } from '@train/image-annotator/image-annotator-box';
import { BaseComponent } from '@utils/base/base.component';
import { Observable } from 'rxjs';
import { Frame } from '../record-frame';

@Component({
  selector: 'app-record-box-train-object',
  standalone: false,
  templateUrl: './record-box-train-object.component.html',
  styleUrl: './record-box-train-object.component.scss'
})
export class RecordBoxTrainObjectComponent extends BaseComponent implements OnInit {
  @Input() box!:ImageAnnotatorBox;
  @Input() train!:TrainImageObject;
  @Input() frame!:Frame;
  @Input() lesson!:TrainLesson;
  @Input() enableCreate: boolean = true;
  labels: DetectorLabel[] = []
  selected: DetectorLabel[] = [];
  total: number = 0;
  skip:number = 0;
  limit:number = 10;
  search:string = '';

  newLabel: string = '';
  newLabelValid: boolean = false;

  dismiss(){
    this.ctx.dismissModal();
  }
  ngOnInit(): void {
    setTimeout(()=>{
      this.selected = [];
        this.train.labels?.forEach(value=>{
          this.loadLabel(value).subscribe({next:(resultb)=>{
            this.selected.push(resultb);
          }})
        })
      this.load();
    });

  }


  onNewLabelChange(value:string){
    this.newLabel = value;
    if (this.newLabel.trim()!=''){
      this.newLabelValid = true;
    }
  else{
      this.newLabelValid=false;
  }
  }

  addNewLabel(){
    if (!this.lesson.detector) return;
    this.loading.next(this.ctx.translate.instant("workspace.detector.class.adding"));
    this.error.next(undefined);
    this.ctx.api.detector.detectorLabelAdd(this.lesson.detector,this.newLabel).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.load();
      },
      error: (result)=>{
        this.error.next(result.error.detail);
        this.loading.next(undefined);
      }
    })
  }

  onChangeSearch(value:string){
    this.skip = 0;
    this.search = value;
    this.load();
  }

  onSkipChange(value:number){
    this.skip = value;
    this.load();
  }

  onLimitChange(value:number){
    this.limit = value;
    this.load();
  }

  onSearchChange(value:string){
    this.skip = 0;
    this.search = value;
    this.load();
  }

  submit(){
    if (!this.train._id) return;
    let labels = this.labelsToStringList(this.selected);
    this.ctx.api.trainer.trainerLessonImageObjectUpdate({id:this.train._id,labels:labels,val:true,test:true,train:true,xstart:this.box.x,xend:this.box.x+this.box.w,ystart:this.box.y,yend:this.box.y+this.box.h}).subscribe({
      next: (result)=>{
        this.train.labels = labels;
        this.ctx.closeModal(undefined);
      },
      error: (result)=>{

      }
    })

  }

  remove(){
    if (this.train._id)
    this.ctx.api.trainer.trainerLessonImageObjectRemove(this.train._id).subscribe({
      next: (result)=>{
        this.frame.train.splice(this.frame.train.findIndex(item=>item._id == this.train._id),1);
        this.ctx.closeModal(undefined);
      },
      error: (result)=>{}
    })
  }

  select(label: DetectorLabel){
    let found = this.selected.findIndex(item=> item._id === label._id);
    if (found!=-1){
      this.selected.splice(found,1);
    }else{
      this.selected.push(label);
    }

    this.load();

  }

  labelsToStringList(value: DetectorLabel[]): string[]{
    let ret = [];
    for (let i = 0; i < value.length; i++){
      ret.push(value[i].name);
    }
    return ret;
  }

  loadLabel(value:string): Observable<DetectorLabel>{
    return new Observable<DetectorLabel>(observer=>{
      if (!this.lesson.detector){
        observer.error('Detector not specified');
      }else{
        this.ctx.api.detector.detectorLabel(this.lesson.detector,value).subscribe({
          next: (result)=>{
            observer.next(result);
          },
          error: (result)=>{
            observer.error(result);
          }
        })
      }

    })
  }

  load(){
    if (!this.lesson.detector) return;

    this.loading.next(this.ctx.translate.instant("workspace.detector.class.loadings"));
    this.error.next(undefined);
    this.ctx.api.detector.detectorLabelList(this.lesson.detector,this.skip,this.limit,this.search).subscribe({
      next: (result)=>{
        this.total = result.total;
        this.labels = result.labels;
        this.loading.next(undefined);


      },
      error: (result)=>{
        this.error.next(result.error.detail);
        this.loading.next(undefined);
      }
    })
  }
}
