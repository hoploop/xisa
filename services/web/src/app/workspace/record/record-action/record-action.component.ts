import { Component, Input, OnInit } from '@angular/core';
import { Action, ResponseRecordereventload } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-action',
  standalone: false,
  templateUrl: './record-action.component.html',
  styleUrl: './record-action.component.scss'
})
export class RecordActionComponent extends BaseComponent implements OnInit {
  @Input() action!:Action;
  dismiss(){
    this.ctx.dismissModal();

  }

  ngOnInit(): void {

  }
  remove(){
    if (!this.action._id) return;
    this.ctx.api.recorder.recorderActionRemove(this.action._id).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.ctx.closeModal(undefined);
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }


}
