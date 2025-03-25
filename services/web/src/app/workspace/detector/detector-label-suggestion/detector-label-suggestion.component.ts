import { Component, EventEmitter, Input, Output } from '@angular/core';
import { DetectorLabel } from '@api/index';
import { ImageAnnotatorBox } from '@train/image-annotator/image-annotator-box';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-label-suggestion',
  standalone: false,
  templateUrl: './detector-label-suggestion.component.html',
  styleUrl: './detector-label-suggestion.component.scss'
})
export class DetectorLabelSuggestionComponent extends BaseComponent{
  @Input() box!: ImageAnnotatorBox;
  @Input() label!:DetectorLabel;
  @Output() onAccept = new EventEmitter<ImageAnnotatorBox>();
  @Output() onReject = new EventEmitter<ImageAnnotatorBox>();
}
