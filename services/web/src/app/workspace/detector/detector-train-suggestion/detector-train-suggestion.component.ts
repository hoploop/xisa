import { Component, EventEmitter, Input, Output } from '@angular/core';
import { DetectorLabel } from '@api/index';
import { ImageAnnotatorBox } from '@train/image-annotator/image-annotator-box';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-train-suggestion',
  standalone: false,
  templateUrl: './detector-train-suggestion.component.html',
  styleUrl: './detector-train-suggestion.component.scss'
})
export class DetectorTrainSuggestionComponent extends BaseComponent {
  @Input() box!: ImageAnnotatorBox;
  @Input() label!:DetectorLabel;
  @Output() onAccept = new EventEmitter<[ImageAnnotatorBox,DetectorLabel]>();
  @Output() onReject = new EventEmitter<[ImageAnnotatorBox,DetectorLabel]>();
}
