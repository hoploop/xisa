import { Component, EventEmitter, Input, Output } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';
import { Frame } from '@record/record-frame';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-record-frame-scroller-card',
  standalone: false,
  templateUrl: './record-frame-scroller-card.component.html',
  styleUrl: './record-frame-scroller-card.component.scss'
})
export class RecordFrameScrollerCardComponent extends BaseComponent {
  @Input() frames: Frame[] = [];
  @Output() selectedFrame = new EventEmitter<Frame>();
  @Input() synthetic: boolean = false;
  @Output() syntheticChange = new EventEmitter<boolean>();
  collapsed = new BehaviorSubject<boolean>(false);

  selectFrame(value:Frame){
    this.selectedFrame.next(value);
  }

  toggleSynthetic(){
    this.synthetic = !this.synthetic;
    this.syntheticChange.next(this.synthetic);
  }
}
