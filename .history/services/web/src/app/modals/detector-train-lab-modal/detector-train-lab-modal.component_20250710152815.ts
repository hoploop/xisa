import { Component, Input } from '@angular/core';
import { TrainSession } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-train-lab-modal',
  standalone: false,
  templateUrl: './detector-train-lab-modal.component.html',
  styleUrl: './detector-train-lab-modal.component.scss'
})
export class DetectorTrainLabModalComponent extends BaseComponent {
  @Input() session!:TrainSession;
 dismiss() {
    this.ctx.dismissModal();
  }
}
