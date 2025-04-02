import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FAIconType } from '@constants/icons';
import { ContextService } from '@services/context.service';
import { BehaviorSubject, Observable } from 'rxjs';
import { Detector, Record } from '@api/index';
import { BIconType } from '@constants/icons';
import { DetectorSelectorComponent } from '@workspace/detector/detector-selector/detector-selector.component';
import { RecordFormComponent } from '../record-form/record-form.component';
import { RecordControllerComponent } from '../record-controller/record-controller.component';
import { BaseComponent } from '../../../utils/base/base.component';
import { NGXLogger } from 'ngx-logger';

@Component({
  selector: 'app-record-list',
  standalone: false,
  templateUrl: './record-list.component.html',
  styleUrl: './record-list.component.scss',
})
export class RecordListComponent extends BaseComponent implements OnInit {
  projectId?: string;
  skip: number = 0;
  limit: number = 0;
  search: string = '';
  total: number = 0;
  records: Record[] = [];
  running?: boolean;

  constructor(
    protected override ctx: ContextService,
    protected override router: Router,
    protected override route: ActivatedRoute,
    protected override log: NGXLogger
  ) {
    super(ctx,router,route,log);
    this.projectId = route.snapshot.paramMap.get('project_id') || undefined;
  }

  ngOnInit(): void {
    this.load();
  }

  onChangeSearch(value: string) {
    this.search = value;
    this.skip = 0;
    this.load();
  }

  create() {
    this.ctx.openModal<undefined>(RecordControllerComponent, {}).subscribe({
      next: (result) => {
        this.load();
      },
      error: (result) => {},
    });
  }

  edit(record: Record) {
    this.ctx
      .openModal<undefined>(RecordFormComponent, { record: record })
      .subscribe({
        next: (result) => {
          this.load();
        },
        error: (result) => {},
      });
  }

  setDetector(record: Record) {
    if (!record._id) return;
    this.ctx.api.trainer.trainerLesson(record._id).subscribe({
      next: (result) => {
        this.ctx
          .openModal<Detector | undefined>(DetectorSelectorComponent, {
            projectId: this.projectId,
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
    this.ctx.api.trainer.trainerLesson(record._id).subscribe({
      next: (result) => {
        if (result.detector == undefined) {
          this.ctx
            .openModal<Detector | undefined>(DetectorSelectorComponent, {
              projectId: this.projectId,
            })
            .subscribe({
              next: (resultb) => {
                if (resultb && resultb._id && result._id) {
                  this.ctx.api.trainer
                    .trainerLessonSetDetector(resultb._id, result._id)
                    .subscribe({
                      next: (resultc) => {
                        this.router.navigateByUrl(
                          '/record/studio/' + record._id + '/' + resultb._id
                        );
                      },
                    });
                }
              },
              error: (result) => {},
            });
        } else {
          this.router.navigateByUrl(
            '/record/studio/' + record._id + '/' + result.detector
          );
        }
      },
    });
  }

  load() {
    if (!this.projectId) return;
    this.ctx.api.recorder.recorderRunning().subscribe({
      next: (result) => {
        this.running = result;
      },
      error: (result) => {
        this.running = undefined;
      },
    });

    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant('workspace.record.loadings'));
    this.ctx.api.recorder
      .recorderList(this.projectId, this.skip, this.limit, this.search)
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
