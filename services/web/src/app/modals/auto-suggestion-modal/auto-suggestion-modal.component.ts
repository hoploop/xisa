import { Component, Input } from '@angular/core';
import { DetectorSuggestion, Record } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { ImageAnnotatorBox } from '@utils/image-annotator/image-annotator-box';

@Component({
  selector: 'app-auto-suggestion-modal',
  standalone: false,
  templateUrl: './auto-suggestion-modal.component.html',
  styleUrl: './auto-suggestion-modal.component.scss',
})
export class AutoSuggestionModalComponent extends BaseComponent {
  @Input() box!: ImageAnnotatorBox;
  @Input() suggestion!: DetectorSuggestion;
  @Input() record!: Record;

  dismiss() {
    this.ctx.dismissModal();
  }

  onAcceptSuggestion(value: DetectorSuggestion) {
    let position: number[] | undefined = undefined;
    if (this.suggestion.by_position) {
      position = [this.suggestion.by_position.x, this.suggestion.by_position.y];
    }
    if (this.record._id)
    this.ctx.api.recorder
      .recorderActionCreate({
        recordId: this.record._id,
        eventId: this.suggestion.event,
        byLabel: this.suggestion.by_label,
        byText: this.suggestion.by_text,
        byRegex: this.suggestion.by_regex,
        byOrder: this.suggestion.by_order,
        byPosition: position,
        confidence: this.suggestion.confidence,
        image: this.box.dataUrl,
      })
      .subscribe({
        next: (result) => {
          this.loading.next(undefined);
          this.ctx.closeModal(result);
        },
        error: (result) => {
          this.loading.next(undefined);
          this.error.next(result.error.detail);
          this.ctx.dismissModal();
        },
      });
  }

  onRejectSuggestion(value: DetectorSuggestion) {}
}
