import { Component, Input } from '@angular/core';
import { DetectorSuggestion } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { ImageAnnotatorBox } from '@utils/image-annotator/image-annotator-box';

@Component({
  selector: 'app-detector-suggestion-list',
  standalone: false,
  templateUrl: './detector-suggestion-list.component.html',
  styleUrl: './detector-suggestion-list.component.scss',
})
export class DetectorSuggestionListComponent extends BaseComponent {
  @Input() suggestions: DetectorSuggestion[] = [];
  @Input() suggestionBoxes = new Map<string, DetectorSuggestion>();
  @Input() boxes: ImageAnnotatorBox[] = [];

  dismiss() {
    this.ctx.dismissModal();
  }

  onAccept(value: DetectorSuggestion) {}

  onReject(value: DetectorSuggestion) {}

  getSuggestionUrl(selected: DetectorSuggestion): string | undefined {


    for (let [key, value] of this.suggestionBoxes) {
      if (value == selected) {
        for (let i = 0; i < this.boxes.length; i++){
          let box = this.boxes[i];
          if (box.id == key) {
            return box.dataUrl;
          }
        }
        return undefined;
      }
    };
    return undefined;
  }
}
