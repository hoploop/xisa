import { Component, Input } from '@angular/core';
import {
  DetectObject,
  DetectorLabel,
  DetectorSuggestion,
  DetectText,
} from '@api/index';
import { ImageAnnotatorBox } from '@train/image-annotator/image-annotator-box';
import { BaseComponent } from '@utils/base/base.component';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-record-suggestions',
  standalone: false,
  templateUrl: './record-suggestions.component.html',
  styleUrl: './record-suggestions.component.scss',
})
export class RecordSuggestionsComponent extends BaseComponent {
  @Input() objects!: DetectObject[];
  @Input() texts!: DetectText[];
  @Input() suggestions!: DetectorSuggestion[];
  @Input() boxes!: ImageAnnotatorBox[];

  dismiss() {
    this.ctx.closeModal(undefined);
  }

  labelIsDetected(value: string): boolean {
    if (!this.objects) return false;
    for (let i = 0; i < this.objects.length; i++) {
      let obj = this.objects[i];
      if (obj.name == value) {
        return true;
      }
    }
    return false;
  }

  onAcceptTraining(box: ImageAnnotatorBox, label: DetectorLabel) {}

  onRejectTraining(box: ImageAnnotatorBox, label: DetectorLabel) {}

  onAcceptObject(box: ImageAnnotatorBox, label: DetectorLabel) {}

  onRejectObject(box: ImageAnnotatorBox, label: DetectorLabel) {}

  onAcceptSuggestion(value: DetectorSuggestion) {}

  onRejectSuggestion(value: DetectorSuggestion) {}
}
