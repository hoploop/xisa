import { Component, Input } from '@angular/core';
import { RecordEventsList200ResponseInner } from '@api/model/record-events-list200-response-inner';
import { ImageAnnotatorBox } from '@train/image-annotator/image-annotator-box';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-box-event',
  standalone: false,
  templateUrl: './record-box-event.component.html',
  styleUrl: './record-box-event.component.scss'
})
export class RecordBoxEventComponent extends BaseComponent {
  @Input() box!: ImageAnnotatorBox;
  @Input() event!: RecordEventsList200ResponseInner;


  dismiss(){
    this.ctx.dismissModal();
  }
}
