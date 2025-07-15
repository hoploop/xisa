import { Component, Input } from '@angular/core';
import { DetectContour } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-contour-modal',
  standalone: false,
  templateUrl: './detector-contour-modal.component.html',
  styleUrl: './detector-contour-modal.component.scss'
})
export class DetectorContourModalComponent extends BaseComponent {
  @Input() contour!:DetectContour;
    dismiss() {
    this.ctx.dismissModal();
  }

}
