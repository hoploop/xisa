import { Component, EventEmitter, Input, Output } from '@angular/core';
import { TrainImageObject } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { v4 as uuid } from 'uuid';

@Component({
  selector: 'app-trainer-lesson-train-card',
  standalone: false,
  templateUrl: './trainer-lesson-train-card.component.html',
  styleUrl: './trainer-lesson-train-card.component.scss'
})
export class TrainerLessonTrainCardComponent extends BaseComponent {
  @Input() train!:TrainImageObject;
  @Output() onSelected = new EventEmitter<string>();
  @Output() onDeselected = new EventEmitter<string>();
  id: string = uuid();
  checked: boolean = false;

  toggleCheck() {
    this.checked = !this.checked;
    if (this.checked){
      this.onSelected.next(this.id);
    }
    else{
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
