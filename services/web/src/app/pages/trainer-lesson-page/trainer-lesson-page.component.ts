import { Component, OnInit } from '@angular/core';
import { Detector, Project, TrainLesson, Record } from '@api/index';
import { MenuArea } from '@models/menu-area-enum';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-trainer-lesson-page',
  standalone: false,
  templateUrl: './trainer-lesson-page.component.html',
  styleUrl: './trainer-lesson-page.component.scss',
})
export class TrainerLessonPageComponent
  extends BaseComponent
  implements OnInit
{
  lesson?: TrainLesson;
  project?: Project;
  detector?: Detector;
  record?: Record;

  ngOnInit(): void {
    this.ctx.beat.area.next(MenuArea.TRAIN);
    let recordId = this.getRouteParam('record_id');
    let detectorId = this.getRouteParam('detector_id');
    if (recordId && detectorId) {
      this.ctx.api.recorder.recorderLoad(recordId).subscribe({
        next: (result) => {
          this.record = result;
        },
        error: (result) => {
          this.log.warn(result.error.detail);
        },
      });

      this.ctx.api.detector.detectorLoad(detectorId).subscribe({
        next: (result) => {
          this.detector = result;
          this.ctx.api.project.projectLoad(this.detector.project).subscribe({
            next: (resultb) => {
              this.project = resultb;
              this.ctx.beat.project.next(this.project);
              this.log.debug('Project loaded');
            },
            error: (resultb) => {
              this.log.warn(resultb.error.detail);
            },
          });
        },
        error: (result) => {
          this.log.warn(result.error.detail);
        },
      });

      this.ctx.api.trainer.trainerLesson(recordId).subscribe({
        next: (result) => {
          if (result.detector && result._id) {
            this.ctx.api.trainer
              .trainerLessonSetDetector(detectorId, result._id)
              .subscribe({
                next: (resultb) => {
                  this.lesson = resultb;
                  this.log.info('Lesson loaded');
                },
                error: (resultb) => {
                  this.log.warn(resultb.error.detail);
                },
              });
          } else {
            this.log.info('Lesson loaded');
            this.lesson = result;
          }
        },
        error: (result) => {
          this.log.warn(result.error.detail);
        },
      });
    }
  }
}
