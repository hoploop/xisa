import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { DetectObject, DetectorLabel } from '@api/index';
import { ImageAnnotatorBox } from '@train/image-annotator/image-annotator-box';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-label-train',
  standalone: false,
  templateUrl: './detector-label-train.component.html',
  styleUrl: './detector-label-train.component.scss'
})
export class DetectorLabelTrainComponent extends BaseComponent {
  @Input() box!: ImageAnnotatorBox;
  @Input() label!:DetectorLabel;
  @Output() onAccept = new EventEmitter<ImageAnnotatorBox>();
  @Output() onReject = new EventEmitter<ImageAnnotatorBox>();

}
