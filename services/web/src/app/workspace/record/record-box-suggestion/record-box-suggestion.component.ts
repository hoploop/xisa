import { Component, Input } from '@angular/core';
import { DetectorSuggestion } from '@api/index';
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
  @Input() syggestion!:DetectorSuggestion;

  dismiss(){
    this.ctx.closeModal(undefined);
  }
}
