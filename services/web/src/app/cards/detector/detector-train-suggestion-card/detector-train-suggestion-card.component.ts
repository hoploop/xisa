import { Component, EventEmitter, Input, Output } from '@angular/core';
import { DetectorLabel, TrainImageObject } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { ImageAnnotatorBox } from '@utils/image-annotator/image-annotator-box';

@Component({
  selector: 'app-detector-train-suggestion-card',
  standalone: false,
  templateUrl: './detector-train-suggestion-card.component.html',
  styleUrl: './detector-train-suggestion-card.component.scss'
})
export class DetectorTrainSuggestionCardComponent extends BaseComponent {
  @Input() box!: ImageAnnotatorBox;
  @Input() label!:DetectorLabel;
  @Input() train?: TrainImageObject;
  @Output() onAccept = new EventEmitter<[ImageAnnotatorBox,DetectorLabel]>();
  @Output() onReject = new EventEmitter<[ImageAnnotatorBox,DetectorLabel]>();
  @Output() onRemove = new EventEmitter<TrainImageObject>();
}

