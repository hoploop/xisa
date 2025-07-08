import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Action } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { v4 as uuid } from 'uuid';
@Component({
  selector: 'app-trainer-lesson-action-card',
  standalone: false,
  templateUrl: './trainer-lesson-action-card.component.html',
  styleUrl: './trainer-lesson-action-card.component.scss'
})
export class TrainerLessonActionCardComponent extends BaseComponent{
  @Input() action!:Action;
  @Output() onSelected = new EventEmitter<string>();
  @Output() onDeselected = new EventEmitter<string>();
  @Output() onRemove = new EventEmitter<string>();
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
      if (this.action.confidence >=0.5 && this.action.confidence < 0.85){
        return 'border-0 bg-warning';
      }else if (this.action.confidence > 0.85){
        return 'border-0 bg-success';

      }else if (this.action.confidence < 0.5) {
        return 'border-0 bg-danger';
      }
      else{return '';}
    }else{
      if (this.action.confidence >=0.5 && this.action.confidence < 0.85){
        return 'border border-warning';

      }else if (this.action.confidence > 0.85){
        return 'border border-success';

      }else if (this.action.confidence < 0.5){
        return 'border border-danger';
      }
      else{return '';}
    }

  }

  remove(){
    if (!this.action._id) return;
    this.ctx.api.recorder.recorderActionRemove(this.action._id).subscribe({
      next: (result)=>{
        this.onRemove.next(this.id);
      },
      error: (result)=>{this.log.warn(result.error.detail);}
    })
  }
}
