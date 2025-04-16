import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { DetectorSuggestion, ResponseRecordereventload } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-suggestion-card',
  standalone: false,
  templateUrl: './detector-suggestion-card.component.html',
  styleUrl: './detector-suggestion-card.component.scss',
})
export class DetectorSuggestionCardComponent
  extends BaseComponent
  implements OnInit
{
  @Input() suggestion!: DetectorSuggestion;
  @Output() onAccept = new EventEmitter<DetectorSuggestion>();
  @Output() onReject = new EventEmitter<DetectorSuggestion>();
  event?: ResponseRecordereventload;

  ngOnInit(): void {
    this.ctx.api.recorder.recorderEventLoad(this.suggestion.event).subscribe({
      next: (result) => {
        this.event = result;
      },
    });
  }
}
