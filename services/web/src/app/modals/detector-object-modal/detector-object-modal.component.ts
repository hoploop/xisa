import { Component, Input } from '@angular/core';
import { DetectObject } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { ImageAnnotatorBox } from '@utils/image-annotator/image-annotator-box';

@Component({
  selector: 'app-detector-object-modal',
  standalone: false,
  templateUrl: './detector-object-modal.component.html',
  styleUrl: './detector-object-modal.component.scss'
})
export class DetectorObjectModalComponent extends BaseComponent {
  @Input() box!:ImageAnnotatorBox;
  @Input() obj!:DetectObject;

  dismiss(){
    this.ctx.dismissModal();

  }
}
