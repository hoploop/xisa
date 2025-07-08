import { Component, EventEmitter, Input, Output } from '@angular/core';
import { RecorderEventList200ResponseInner } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { v4 as uuid } from 'uuid';

@Component({
  selector: 'app-trainer-lesson-event-card',
  standalone: false,
  templateUrl: './trainer-lesson-event-card.component.html',
  styleUrl: './trainer-lesson-event-card.component.scss',
})
export class TrainerLessonEventCardComponent extends BaseComponent {
  @Input() event!: RecorderEventList200ResponseInner;
  @Output() onSelected = new EventEmitter<string>();
  @Output() onDeselected = new EventEmitter<string>();
  id: string = uuid();
  checked: boolean = false;
  toggleCheck() {
    this.checked = !this.checked;
    if (this.checked){
      this.onSelected.next(this.id)
    }else{
      this.onDeselected.next(this.id);
    }
  }

  buildNgClass():string{
    if (this.checked){
      return 'border-0 bg-info';

    }else{
      return 'border border-info';
    }

  }
}
