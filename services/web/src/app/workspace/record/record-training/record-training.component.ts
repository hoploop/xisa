import { Component, Input, OnInit } from '@angular/core';
import { DetectObject, DetectorImageLabelAdd, DetectorImageMode, DetectorLabel, DetectorSuggestion, DetectText, TrainLesson } from '@api/index';
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


  trainingQueue: Array<[ImageAnnotatorBox,DetectorLabel]> = [];

  ngOnInit(): void {
      this.calculateTrainingObjects();
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
    return false;
  }

  labelIsSaved(value: DetectorLabel):boolean{
    if (this.savedLabels.findIndex(item=>item._id == value._id) == -1){
      return false;
    }else{
      return true;
    }
  }


  onAcceptObject(box: ImageAnnotatorBox, label: DetectorLabel) {

    // Check if box and labels are already in the training queue
    for (let i = 0; i < this.trainingQueue.length; i++){
      let tBox = this.trainingQueue[i][0];
      let tLabel = this.trainingQueue[i][1];
      if (tBox.id == box.id && label._id == tLabel._id){
        return;
      }
    }

    this.trainingQueue.push([box,label]);
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
