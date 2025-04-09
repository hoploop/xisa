import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Frame } from '../record-frame';
import { BehaviorSubject } from 'rxjs';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-scroller',
  standalone: false,
  templateUrl: './record-scroller.component.html',
  styleUrl: './record-scroller.component.scss'
})
export class RecordScrollerComponent extends BaseComponent {
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
