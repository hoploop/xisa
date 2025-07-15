import { Component, Input } from '@angular/core';
import { DetectText } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { ImageAnnotatorBox } from '@utils/image-annotator/image-annotator-box';

@Component({
  selector: 'app-detector-text-modal',
  standalone: false,
  templateUrl: './detector-text-modal.component.html',
  styleUrl: './detector-text-modal.component.scss',
})
export class DetectorTextModalComponent extends BaseComponent {
  @Input() box!: ImageAnnotatorBox;
  @Input() text!: DetectText;

  dismiss() {
    this.ctx.dismissModal();
  }
}
