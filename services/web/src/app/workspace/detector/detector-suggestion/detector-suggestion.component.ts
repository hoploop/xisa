import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { DetectorSuggestion, ResponseRecordereventload } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-suggestion',
  standalone: false,
  templateUrl: './detector-suggestion.component.html',
  styleUrl: './detector-suggestion.component.scss'
})
export class DetectorSuggestionComponent extends BaseComponent implements OnInit {
  @Input() suggestion!:DetectorSuggestion;
  @Output() onAccept = new EventEmitter<DetectorSuggestion>();
  @Output() onReject = new EventEmitter<DetectorSuggestion>();
  event?:ResponseRecordereventload


  ngOnInit(): void {
    this.ctx.api.recorder.recorderEventLoad(this.suggestion.event).subscribe({
      next: (result)=>{
        this.event = result;
      }
    })
  }

}
