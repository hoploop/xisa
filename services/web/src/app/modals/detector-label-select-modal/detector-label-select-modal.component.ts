import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { DetectorLabel } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-label-select-modal',
  standalone: false,
  templateUrl: './detector-label-select-modal.component.html',
  styleUrl: './detector-label-select-modal.component.scss',
})
export class DetectorLabelSelectModalComponent
  extends BaseComponent
  implements OnInit
{
  @Input() detectorId?: string;

  @Input() enableCreate: boolean = true;
  @Input() selected: DetectorLabel[] = [];
  @Output() selectedChange = new EventEmitter<DetectorLabel[]>();
  total: number = 0;
  skip: number = 0;
  limit: number = 10;
  search: string = '';
  labels: DetectorLabel[] = [];

  newLabel: string = '';
  newLabelValid: boolean = false;

  ngOnInit(): void {
    setTimeout(() => {
      this.load();
    });
  }

  onNewLabelChange(value: string) {
    this.newLabel = value;
    if (this.newLabel.trim() != '') {
      this.newLabelValid = true;
    } else {
      this.newLabelValid = false;
    }
  }

  addNewLabel() {
    if (!this.detectorId) return;
    this.loading.next(this.ctx.translate.instant('detector.class.adding'));
    this.error.next(undefined);
    this.ctx.api.detector
      .detectorLabelAdd(this.detectorId, this.newLabel)
      .subscribe({
        next: (result) => {
          this.loading.next(undefined);
          this.load();
        },
        error: (result) => {
          this.error.next(result.error.detail);
          this.loading.next(undefined);
        },
      });
  }

  onChangeSearch(value: string) {
    this.skip = 0;
    this.search = value;
    this.load();
  }

  onSkipChange(value: number) {
    this.skip = value;
    this.load();
  }

  onLimitChange(value: number) {
    this.limit = value;
    this.load();
  }

  onSearchChange(value: string) {
    this.skip = 0;
    this.search = value;
    this.load();
  }

  submit() {
    this.ctx.closeModal(this.selected);
  }

  remove(){
    this.ctx.closeModal(undefined);
  }

  select(label: DetectorLabel) {
    let found = this.selected.findIndex((item) => item._id === label._id);
    if (found != -1) {
      this.selected.splice(found, 1);
    } else {
      this.selected.push(label);
    }
    this.selectedChange.next(this.selected);
    this.load();
  }

  load() {
    if (!this.detectorId) return;
    this.loading.next(this.ctx.translate.instant('detector.class.loadings'));
    this.error.next(undefined);
    this.ctx.api.detector
      .detectorLabelList(this.detectorId, this.skip, this.limit, this.search)
      .subscribe({
        next: (result) => {
          this.total = result.total;
          this.labels = result.labels;
          this.loading.next(undefined);
        },
        error: (result) => {
          this.error.next(result.error.detail);
          this.loading.next(undefined);
        },
      });
  }

  dismiss() {
    this.ctx.dismissModal();
  }
}
