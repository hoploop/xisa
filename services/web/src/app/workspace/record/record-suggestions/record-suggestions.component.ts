import { Component, Input } from '@angular/core';
import {
  DetectObject,
  DetectorImageLabelAdd,
  DetectorImageMode,
  DetectorLabel,
  DetectorSuggestion,
  DetectText,
  TrainLesson,
} from '@api/index';
import { ImageAnnotatorBox } from '@train/image-annotator/image-annotator-box';
import { BaseComponent } from '@utils/base/base.component';
import { BehaviorSubject } from 'rxjs';
import { Frame } from '../record-frame';

@Component({
  selector: 'app-record-suggestions',
  standalone: false,
  templateUrl: './record-suggestions.component.html',
  styleUrl: './record-suggestions.component.scss',
})
export class RecordSuggestionsComponent extends BaseComponent {
  @Input() frame!:Frame;

  dismiss() {
    this.ctx.closeModal(undefined);
  }

  onAcceptObject(box: ImageAnnotatorBox, label: DetectorLabel) {

  }

  onRejectObject(box: ImageAnnotatorBox, label: DetectorLabel) {}

  onAcceptSuggestion(value: DetectorSuggestion) {}

  onRejectSuggestion(value: DetectorSuggestion) {}

}
