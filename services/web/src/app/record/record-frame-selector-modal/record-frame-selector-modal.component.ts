import { Component, Input } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';
import { Frame } from '@record/record-frame';

@Component({
  selector: 'app-record-frame-selector-modal',
  standalone: false,
  templateUrl: './record-frame-selector-modal.component.html',
  styleUrl: './record-frame-selector-modal.component.scss'
})
export class RecordFrameSelectorModalComponent  extends BaseComponent {
  frames_count:number = 0;
  @Input() frames: Frame[] = [];
  frame?:Frame = undefined;
  @Input() synthetic: boolean = false;

  dismiss(){
    this.ctx.closeModal(undefined);
  }

  selectFrame(frame:Frame){
    this.ctx.closeModal(frame);
  }

  toggleSynthetic(){
    this.synthetic = !this.synthetic;
  }

}
