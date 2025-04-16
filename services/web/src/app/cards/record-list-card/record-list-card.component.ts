import { Component, Input, OnInit } from '@angular/core';
import { Detector, Project, Record } from '@api/index';
import { DetectorSelectorModalComponent } from '@modals/detector-selector-modal/detector-selector-modal.component';
import { RecordControllerModalComponent } from '@modals/record-controller-modal/record-controller-modal.component';
import { RecordFormModalComponent } from '@modals/record-form-modal/record-form-modal.component';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-list-card',
  standalone: false,
  templateUrl: './record-list-card.component.html',
  styleUrl: './record-list-card.component.scss'
})
export class RecordListCardComponent extends BaseComponent implements OnInit {
  @Input() project!: Project;
  skip: number = 0;
  limit: number = 0;
  search: string = '';
  total: number = 0;
  records: Record[] = [];
  running?: boolean;

  ngOnInit(): void {
    this.load();
  }

  onChangeSearch(value: string) {
    this.search = value;
    this.skip = 0;
    this.load();
  }

  create() {
    if (!this.project) return;
    this.ctx
      .openModal<undefined>(RecordControllerModalComponent, {
        project: this.project,
      })
      .subscribe({
        next: (result) => {
          this.load();
        },
        error: (result) => {},
      });
  }

  edit(record: Record) {
    this.ctx
      .openModal<undefined>(RecordFormModalComponent, { record: record })
      .subscribe({
        next: (result) => {
          this.load();
        },
        error: (result) => {},
      });
  }

  setDetector(record: Record) {
    if (!this.project) return;
    if (!record._id) return;
    this.ctx.api.trainer.trainerLesson(record._id).subscribe({
      next: (result) => {
        this.ctx
          .openModal<Detector | undefined>(DetectorSelectorModalComponent, {
            project: this.project,
          })
          .subscribe({
            next: (resultb) => {
              if (resultb && resultb._id && result._id) {
                this.ctx.api.trainer
                  .trainerLessonSetDetector(resultb._id, result._id)
                  .subscribe({ next: (resultc) => {} });
              }
            },
            error: (result) => {},
          });
      },
    });
  }

  studio(record: Record) {
    if (!record._id) return;
    if (!this.project) return;
    this.ctx.api.trainer.trainerLesson(record._id).subscribe({
      next: (result) => {
        if (result.detector == undefined) {
          this.ctx
            .openModal<Detector | undefined>(DetectorSelectorModalComponent, {
              project: this.project,
            })
            .subscribe({
              next: (resultb) => {
                if (resultb && resultb._id && result._id) {
                  this.ctx.api.trainer
                    .trainerLessonSetDetector(resultb._id, result._id)
                    .subscribe({
                      next: (resultc) => {
                        if (resultb._id) {
                          this.navigateRecordStudio(record);
                        }
                      },
                    });
                }
              },
              error: (result) => {},
            });
        } else {
          this.navigateRecordStudio(record);
        }
      },
    });
  }

  navigateRecordStudio(record: Record) {
    this.router.navigate(['record/studio',record._id]);
  }

  load() {
    if (!this.project) return;
    if (!this.project._id) return;
    this.ctx.api.recorder.recorderRunning().subscribe({
      next: (result) => {
        this.running = result;
      },
      error: (result) => {
        this.running = undefined;
      },
    });

    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant('recorder.loadings'));
    this.ctx.api.recorder
      .recorderList(this.project._id, this.skip, this.limit, this.search)
      .subscribe({
        next: (result) => {
          this.loading.next(undefined);
          this.total = result.total;
          this.records = result.records;
        },
        error: (result) => {
          this.loading.next(undefined);
          this.error.next(result.error.detail);
        },
      });
  }
}
