import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Detector } from '@api/index';
import { ContextService } from '@services/context.service';
import { DetectorFormComponent } from '../detector-form/detector-form.component';
import { DetectorLearnComponent } from '../detector-learn/detector-learn.component';
import { BaseComponent } from '@utils/base/base.component';
import { NGXLogger } from 'ngx-logger';

@Component({
  selector: 'app-detector-list',
  standalone: false,
  templateUrl: './detector-list.component.html',
  styleUrl: './detector-list.component.scss',
})
export class DetectorListComponent extends BaseComponent implements OnInit {
  skip: number = 0;
  limit: number = 10;
  search: string = '';
  total: number = 0;
  detectors: Detector[] = [];
  projectId?: string;

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
    this.ctx
      .openModal<Detector | undefined>(DetectorFormComponent, {
        detector: {
          project: this.projectId,
          name: '',
          description: '',
        },
      })
      .subscribe({
        next: (result) => {
          if (result) {
            this.load();
          }
        },
        error: (result) => {},
      });
  }

  clone(detector: Detector) {
    this.ctx
      .openModal<Detector | undefined>(DetectorFormComponent, {
        detector: {
          project: this.projectId,
          name: '',
          description: '',
        },
        origin: detector,
      })
      .subscribe({
        next: (result) => {
          if (result) {
            this.load();
          }
        },
        error: (result) => {},
      });
  }

  train(detector:Detector){
    if (!detector._id) return;
    this.ctx
      .openModal<Detector | undefined>(DetectorLearnComponent, {
        detector: detector,
      })
      .subscribe({
        next: (result) => {
          this.load();
        },
        error: (result) => {},
      });
  }

  edit(detector: Detector) {
    if (!detector._id) return;
    this.ctx
      .openModal<Detector | undefined>(DetectorFormComponent, {
        detector: detector,
      })
      .subscribe({
        next: (result) => {
          this.load();
        },
        error: (result) => {},
      });
  }

  learn(detector: Detector) {
    if (!detector._id) return;
    this.router.navigateByUrl('/detector/learn/' + detector._id);
  }

  load() {
    if (!this.projectId) return;
    this.log.debug("Loading detectors");
    this.loading.next(
      this.ctx.translate.instant('workspace.detector.loadings')
    );
    this.error.next(undefined);
    this.ctx.api.detector
      .detectorList(this.projectId, this.skip, this.limit, this.search)
      .subscribe({
        next: (result) => {
          this.loading.next(undefined);
          this.total = result.total;
          this.detectors = result.detectors;
        },
        error: (result) => {
          this.loading.next(undefined);
          this.error.next(result.error.detail);
        },
      });
  }
}
