import { Component, Input, OnDestroy, OnInit } from '@angular/core';
import { Detector, DetectorTrainingSession } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { filter, Subscription } from 'rxjs';

@Component({
  selector: 'app-detector-learn',
  standalone: false,
  templateUrl: './detector-learn.component.html',
  styleUrl: './detector-learn.component.scss',
})
export class DetectorLearnComponent extends BaseComponent implements OnInit, OnDestroy {
  subs = new Subscription();

  @Input() detector!:Detector;
  progress: number = -1;

  train(){
    if (!this.detector._id) return;
    this.progress = 0;
    this.error.next(undefined);

    this.log.debug('Preparing the training objects');
    this.ctx.api.trainer.trainerLessonImageObjectToDetector(this.detector._id).subscribe({
      next: (result)=>{
        if (result > 0 && this.detector._id){
          this.loading.next(this.ctx.translate.instant('workspace.detector.training.loading'));
          this.ctx.api.detector.detectorTrain(this.detector._id,3).subscribe({
            next: (result)=>{},
            error: (result)=>{
              this.loading.next(undefined);
              this.error.next(result.error.detail);
            }
          })
        }
      },
      error: (result)=>{
        this.log.error(result.error.detail);
      }
    })



  }

  dismiss(){
    this.ctx.dismissModal();
  }


  ngOnInit(): void {
    let filtered = this.ctx.ws.messages$.pipe(filter(msg => msg.type == 'detector.training.session' && msg.detector == this.detector._id));
    this.subs.add(filtered.subscribe({
      next: (result)=>{
          let res = result as DetectorTrainingSession;
            this.progress =  Math.round((res.epoch_progress / res.epoch_total)*100);
            if (this.progress >=99){
              this.loading.next(undefined);
            }

      }
    }));

  }

  ngOnDestroy(): void {
    this.subs.unsubscribe();
  }
}
