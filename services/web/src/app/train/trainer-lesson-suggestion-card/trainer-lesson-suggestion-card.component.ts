import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Action, DetectorSuggestion, ResponseRecordereventload } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { v4 as uuid } from 'uuid';

@Component({
  selector: 'app-trainer-lesson-suggestion-card',
  standalone: false,
  templateUrl: './trainer-lesson-suggestion-card.component.html',
  styleUrl: './trainer-lesson-suggestion-card.component.scss',
})
export class TrainerLessonSuggestionCardComponent
  extends BaseComponent
  implements OnInit
{
  @Input() suggestion!: DetectorSuggestion;
  @Input() actions:Action[] = []
  @Output() onAccept = new EventEmitter<DetectorSuggestion>();
  @Output() onReject = new EventEmitter<DetectorSuggestion>();
  @Output() onSelected = new EventEmitter<string>();
  @Output() onDeselected = new EventEmitter<string>();
  @Output() onAccepted = new EventEmitter<string>();
  @Output() onRejected = new EventEmitter<string>();
  id: string = uuid();
  event?: ResponseRecordereventload;
  checked: boolean = false;

  toggleCheck() {
    this.checked = !this.checked;
    if (this.checked){
      this.onSelected.next(this.id);
    }
    else{
      this.onDeselected.next(this.id);
    }
  }

  get hasAction():boolean {
    if (this.actions.length == 0) return false;
    for (let i = 0; i< this.actions.length; i++){
      if (this.actions[i].event == this.suggestion.event)
        return true;
    }
    return false;
  }

  ngOnInit(): void {

    this.ctx.api.recorder.recorderEventLoad(this.suggestion.event).subscribe({
      next: (result) => {
        this.event = result;
      },
    });
  }
  accept(){
    this.onAccepted.next(this.id);
  }

  reject(){
    this.onRejected.next(this.id);
  }

  buildNgClass():string{
    if (this.checked){
      if (this.suggestion.confidence >=0.5 && this.suggestion.confidence < 0.85){
        return 'border-0 bg-warning';
      }else if (this.suggestion.confidence > 0.85){
        return 'border-0 bg-success';

      }else if (this.suggestion.confidence < 0.5) {
        return 'border-0 bg-danger';
      }
      else{return '';}
    }else{
      if (this.suggestion.confidence >=0.5 && this.suggestion.confidence < 0.85){
        return 'border border-warning';

      }else if (this.suggestion.confidence > 0.85){
        return 'border border-success';

      }else if (this.suggestion.confidence < 0.5){
        return 'border border-danger';
      }
      else{return '';}
    }

  }
}
