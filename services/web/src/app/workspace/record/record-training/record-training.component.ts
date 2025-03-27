import { Component, Input, OnInit } from '@angular/core';
import { DetectObject, DetectorImageLabelAdd, DetectorImageMode, DetectorLabel, DetectorSuggestion, DetectText, TrainImageObject, TrainLesson } from '@api/index';
import { ImageAnnotatorBox } from '@train/image-annotator/image-annotator-box';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-training',
  standalone: false,
  templateUrl: './record-training.component.html',
  styleUrl: './record-training.component.scss'
})
export class RecordTrainingComponent extends BaseComponent implements OnInit {
  @Input() objects!: DetectObject[];
  @Input() texts!: DetectText[];
  @Input() boxes!: ImageAnnotatorBox[];
  @Input() lesson!:TrainLesson;
  @Input() frame!:number;
  training: boolean = true;
  evaluating: boolean = true;
  testing: boolean = false;
  savedLabels: DetectorLabel[] = [];
  totalTrainingObjects: number = 0;
  trainImageObjects: TrainImageObject[] = [];


  ngOnInit(): void {
    setTimeout(()=>{
      this.loadImageObjects();
      this.calculateTrainingObjects();
    });


  }

  calculateTrainingObjects(){
    this.totalTrainingObjects = 0;
      this.boxes.forEach(box=>{
        box.labels.forEach(label=>{
          if (!this.labelIsDetected(label)){
            this.totalTrainingObjects+=1;
          }
        })
      })
  }

  loadImageObjects(){
    this.loading.next(this.ctx.translate.instant('workspace.detector.training.loading_objects'));
    setTimeout(()=>{
      if (!this.lesson._id) return;
      this.ctx.api.trainer.trainerLessonImageObjectList(this.lesson._id,this.frame).subscribe({
        next: (result)=>{
          this.loading.next(undefined);
          this.trainImageObjects = result.objects;
        },
        error: (result)=>{
          this.loading.next(undefined);
          this.error.next(result.error.detail);
        }
      })
    });

  }

  dismiss() {
    this.ctx.closeModal(undefined);
  }

  labelIsDetected(value: DetectorLabel): boolean {
    if (!this.objects) return false;
    for (let i = 0; i < this.objects.length; i++) {
      let obj = this.objects[i];
      if (obj.name == value.name) {
        return true;
      }
    }
    for (let i = 0; i< this.trainImageObjects.length; i++){
      let tio = this.trainImageObjects[i];
      if (tio.label == value.name){
        return true;
      }
    }
    return false;
  }

  labelIsSaved(value: DetectorLabel):boolean{
    if (this.savedLabels.findIndex(item=>item._id == value._id) == -1){
      return false;
    }else{
      return true;
    }
  }

  labelIsInTrainQueue(value: DetectorLabel): TrainImageObject | undefined {
    for (let i = 0; i< this.trainImageObjects.length; i++){
      let tio = this.trainImageObjects[i];
      if (tio.label == value.name){
        return tio;
      }
    }
    return undefined;
  }

  onRemoveObject(value: TrainImageObject){
    if (!value._id) return;
    this.ctx.api.trainer.trainerLessonImageObjectRemove(value._id).subscribe({
      next: (result)=>{
        this.loadImageObjects();
      }
    })
  }

  onAcceptObject(box: ImageAnnotatorBox, label: DetectorLabel) {
    if (!this.lesson._id) return;
    // Check if box and labels are already in the training queue
    this.ctx.api.trainer.trainerLessonImageObject({
      lessonId: this.lesson._id,
    frame: this.frame,
    label: label.name,
    xstart: box.x,
    xend: box.x+box.w,
    ystart: box.y,
    yend: box.y+box.h,
    val: this.evaluating,
    test: this.testing,
    train: this.training
    }).subscribe({
      next: (result)=>{
        this.loadImageObjects();
      }
    })
  }

  onRejectObject(box: ImageAnnotatorBox, label: DetectorLabel) {}



  saveForTraining(box: ImageAnnotatorBox) {
    // Converting the current image to blob
    if (this.lesson.detector && this.lesson.record) {
      let modes: DetectorImageMode[] = [];
      if (this.training) {
        modes.push(DetectorImageMode.Train);
      }
      if (this.evaluating) {
        modes.push(DetectorImageMode.Val);
      }
      if (this.testing) {
        modes.push(DetectorImageMode.Test);
      }
      this.ctx.api.detector
        .detectorFrameUpload(
          this.lesson.record,
          this.lesson.detector,
          this.frame,
          modes
        )
        .subscribe({
          next: (result) => {
            this.setLoading(undefined);
            for (let i = 0; i < result.length; i++) {
              let el = result[i];

              box.labels.forEach((label) => {
                if (el._id) {
                  let payloadAdd: DetectorImageLabelAdd = {
                    image_id: el._id,
                    xstart: box.x,
                    xend: box.x + box.w,
                    ystart: box.y,
                    yend: box.y + box.h,
                    label: label.name,
                  };

                  this.ctx.api.detector
                    .detectorImageLabelAdd(payloadAdd)
                    .subscribe({
                      next: (result2) => {
                        this.setLoading(undefined);
                        this.savedLabels.push(label);
                      },
                      error: (result2) => {
                        this.setError(result2.error.detail);
                        this.setLoading(undefined);
                      },
                    });
                }
              });
            }
          },
          error: (result) => {
            this.setError(result.error.detail);
            this.setLoading(undefined);
          },
        });
    }
  }
}
