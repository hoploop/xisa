import { Component, Input } from '@angular/core';
import { DetectorSuggestion, TrainLesson } from '@api/index';
import { ImageAnnotatorBox } from '@train/image-annotator/image-annotator-box';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-box-suggestion',
  standalone: false,
  templateUrl: './record-box-suggestion.component.html',
  styleUrl: './record-box-suggestion.component.scss'
})
export class RecordBoxSuggestionComponent extends BaseComponent{
  @Input() box!:ImageAnnotatorBox;
  @Input() suggestion!:DetectorSuggestion;
  @Input() lesson!:TrainLesson;

  dismiss(){
    this.ctx.dismissModal();
  }

  onAcceptSuggestion(value: DetectorSuggestion) {
    this.ctx.api.recorder.recorderActionCreate({
      recordId: this.lesson.record,
      eventId: this.suggestion.event,
      byLabel: this.suggestion.by_label,
      byText: this.suggestion.by_text,
      byRegex: this.suggestion.by_regex,
      byOrder: this.suggestion.by_order,
      confidence: this.suggestion.confidence
    }).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.ctx.closeModal(result);
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
        this.ctx.dismissModal();
      }
    })
  }

  onRejectSuggestion(value: DetectorSuggestion) {}
}
