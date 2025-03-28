import { Component, Input } from '@angular/core';
import { TrainImageObject } from '@api/index';
import { ImageAnnotatorBox } from '@train/image-annotator/image-annotator-box';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-box-train-object',
  standalone: false,
  templateUrl: './record-box-train-object.component.html',
  styleUrl: './record-box-train-object.component.scss'
})
export class RecordBoxTrainObjectComponent extends BaseComponent {
  @Input() box!:ImageAnnotatorBox;
  @Input() train!:TrainImageObject;

  dismiss(){
    this.ctx.closeModal(undefined);
  }
}
