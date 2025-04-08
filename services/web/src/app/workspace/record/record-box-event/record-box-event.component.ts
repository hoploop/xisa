import { Component, Input } from '@angular/core';
import { RecorderEventList200ResponseInner } from '@api/index';
import { ImageAnnotatorBox } from '@utils/image-annotator/image-annotator-box';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-box-event',
  standalone: false,
  templateUrl: './record-box-event.component.html',
  styleUrl: './record-box-event.component.scss'
})
export class RecordBoxEventComponent extends BaseComponent {
  @Input() box!: ImageAnnotatorBox;
  @Input() event!: RecorderEventList200ResponseInner;


  dismiss(){
    this.ctx.dismissModal();
  }
}
