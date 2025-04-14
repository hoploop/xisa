import { Component, Input, OnInit } from '@angular/core';
import { Detector, Project } from '@api/index';
import { DetectorFormComponent } from '../detector-form/detector-form.component';
import { DetectorLearnComponent } from '../detector-learn/detector-learn.component';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-list',
  standalone: false,
  templateUrl: './detector-list.component.html',
  styleUrl: './detector-list.component.scss',
})
export class DetectorListComponent extends BaseComponent implements OnInit {
  @Input() project!: Project;
  skip: number = 0;
  limit: number = 10;
  search: string = '';
  total: number = 0;
  detectors: Detector[] = [];

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
        project: this.project,
        detector: {
          project: this.project,
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

  images(detector:Detector){
    if (!detector._id) return;
    this.router.navigate(['detector/image/list',detector._id]);
  }

  clone(detector: Detector) {
    if (!this.project) return;
    this.ctx
      .openModal<Detector | undefined>(DetectorFormComponent, {
        project: this.project,
        detector: {
          project: this.project,
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

  train(detector: Detector) {
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
        project: this.project,
        detector: detector,
      })
      .subscribe({
        next: (result) => {
          this.load();
        },
        error: (result) => {},
      });
  }

  load() {
    if (!this.project) return;
    if (!this.project._id) return;
    this.log.debug('Loading detectors');
    this.loading.next(
      this.ctx.translate.instant('workspace.detector.loadings')
    );
    this.error.next(undefined);
    this.ctx.api.detector
      .detectorList(this.project._id, this.skip, this.limit, this.search)
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
