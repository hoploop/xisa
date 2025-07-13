import { Component, Input, OnInit } from '@angular/core';
import { Detector, Project } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-selector-modal',
  standalone: false,
  templateUrl: './detector-selector-modal.component.html',
  styleUrl: './detector-selector-modal.component.scss',
})
export class DetectorSelectorModalComponent
  extends BaseComponent
  implements OnInit
{
  @Input() project!: Project;
  @Input() detector?: Detector;
  @Input() class: string = '';
  @Input() enableCreate: boolean = false;

  search: string = '';
  skip: number = 0;
  limit: number = 10;
  detectors: Detector[] = [];
  total: number = 0;

  ngOnInit(): void {
    this.load();
  }

  select(value: Detector) {
    this.detector = value;
    this.ctx.closeModal(this.detector);
  }

  onSearchChange(value: string) {
    this.skip = 0;
    this.search = value;
    this.load();
  }

  create() {}

  dismiss() {
    this.ctx.dismissModal();
  }

  load() {
    if (!this.project) return;
    if (!this.project._id) return;
    this.setError(undefined);
    this.setLoading(this.ctx.translate.instant('detector.loadings'));
    this.ctx.api.detector
      .detectorList(this.project._id, this.skip, this.limit, this.search)
      .subscribe({
        next: (result) => {
          this.total = result.total;
          this.detectors = result.detectors;
          this.setLoading(undefined);
        },
        error: (result) => {
          this.setLoading(undefined);
          this.setError(result.error.detail);
        },
      });
  }
}
