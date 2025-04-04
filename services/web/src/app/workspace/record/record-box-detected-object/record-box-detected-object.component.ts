import { Component, Input } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';
import { ImageAnnotatorBox } from '../../../train/image-annotator/image-annotator-box';
import { DetectObject } from '@api/index';

@Component({
  selector: 'app-record-box-detected-object',
  standalone: false,
  templateUrl: './record-box-detected-object.component.html',
  styleUrl: './record-box-detected-object.component.scss'
})
export class RecordBoxDetectedObjectComponent extends BaseComponent {
  @Input() box!:ImageAnnotatorBox;
  @Input() obj!:DetectObject;

  dismiss(){
    this.ctx.dismissModal();

  }
}
