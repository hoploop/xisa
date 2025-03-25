import { Component, EventEmitter, Input, Output } from '@angular/core';
import { DetectorSuggestion } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-suggestion',
  standalone: false,
  templateUrl: './detector-suggestion.component.html',
  styleUrl: './detector-suggestion.component.scss'
})
export class DetectorSuggestionComponent extends BaseComponent {
  @Input() suggestion!:DetectorSuggestion;
  @Output() onAccept = new EventEmitter<DetectorSuggestion>();
  @Output() onReject = new EventEmitter<DetectorSuggestion>();

}
