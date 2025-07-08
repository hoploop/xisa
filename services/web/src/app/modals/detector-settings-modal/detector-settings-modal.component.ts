import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Detector } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-settings-modal',
  standalone: false,
  templateUrl: './detector-settings-modal.component.html',
  styleUrl: './detector-settings-modal.component.scss',
})
export class DetectorSettingsModalComponent extends BaseComponent {
  @Input() detector!: Detector;
  @Input() confidence: number = 0.1;
  @Output() confidenceChange = new EventEmitter<number>();
  dismiss() {
    this.ctx.dismissModal();
  }
  updateConfidence(value: number) {
    this.confidence = value;
    this.confidenceChange.next(value);
  }

  accept() {
    this.ctx.closeModal(this.confidence);
  }
}
