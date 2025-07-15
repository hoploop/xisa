import { Component, EventEmitter, Input, Output } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-text-settings-modal',
  standalone: false,
  templateUrl: './detector-text-settings-modal.component.html',
  styleUrl: './detector-text-settings-modal.component.scss',
})
export class DetectorTextSettingsModalComponent extends BaseComponent {
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
