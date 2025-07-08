import { Component, Input } from '@angular/core';
import { RecorderEventList200ResponseInner } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { ImageAnnotatorBox } from '@utils/image-annotator/image-annotator-box';

@Component({
  selector: 'app-record-event-modal',
  standalone: false,
  templateUrl: './record-event-modal.component.html',
  styleUrl: './record-event-modal.component.scss',
})
export class RecordEventModalComponent extends BaseComponent {
  @Input() box!: ImageAnnotatorBox;
  @Input() event!: RecorderEventList200ResponseInner;

  dismiss() {
    this.ctx.dismissModal();
  }
}
