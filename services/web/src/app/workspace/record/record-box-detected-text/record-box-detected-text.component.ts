import { Component, Input } from '@angular/core';
import { DetectText } from '@api/index';
import { ImageAnnotatorBox } from '@train/image-annotator/image-annotator-box';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-box-detected-text',
  standalone: false,
  templateUrl: './record-box-detected-text.component.html',
  styleUrl: './record-box-detected-text.component.scss'
})
export class RecordBoxDetectedTextComponent extends BaseComponent{
  @Input() box!: ImageAnnotatorBox;
  @Input() text!: DetectText;

  dismiss(){
    this.ctx.closeModal(undefined);
  }
}
