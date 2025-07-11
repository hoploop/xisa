import { Component } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-train-lab-modal',
  standalone: false,
  templateUrl: './detector-train-lab-modal.component.html',
  styleUrl: './detector-train-lab-modal.component.scss'
})
export class DetectorTrainLabModalComponent extends BaseComponent {
 dismiss() {
    this.ctx.dismissModal();
  }
}
