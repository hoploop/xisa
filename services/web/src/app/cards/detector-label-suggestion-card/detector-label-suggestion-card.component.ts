import { Component, EventEmitter, Input, Output } from '@angular/core';
import { DetectorLabel } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { ImageAnnotatorBox } from '@utils/image-annotator/image-annotator-box';

@Component({
  selector: 'app-detector-label-suggestion-card',
  standalone: false,
  templateUrl: './detector-label-suggestion-card.component.html',
  styleUrl: './detector-label-suggestion-card.component.scss',
})
export class DetectorLabelSuggestionCardComponent extends BaseComponent {
  @Input() box!: ImageAnnotatorBox;
  @Input() label!: DetectorLabel;
  @Output() onAccept = new EventEmitter<ImageAnnotatorBox>();
  @Output() onReject = new EventEmitter<ImageAnnotatorBox>();
}
