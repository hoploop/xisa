import { Component, Input } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';
import {Record} from '@api/model/record';
@Component({
  selector: 'app-record-form',
  standalone: false,
  templateUrl: './record-form.component.html',
  styleUrl: './record-form.component.scss',
})
export class RecordFormComponent  extends BaseComponent{
  @Input() record!: Record;



  ngOnInit(): void {

  }

  dismiss(){
    this.ctx.dismissModal();
  }


   remove(){
      if (!this.record._id) return;
      this.error.next(undefined);

      this.loading.next(this.ctx.translate.instant('workspace.record.removing'));
      this.ctx.api.recorder.recorderRemove(this.record._id).subscribe({
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


  cancel(){
    this.ctx.dismissModal();
  }

  save(){
    if (!this.record._id) return;
    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant('workspace.record.saving'));
    this.ctx.api.recorder.recorderEdit(this.record._id,this.record.name,this.record.description||'').subscribe({
      next: (result)=>{
          this.loading.next(undefined);
          this.ctx.closeModal(this.record);
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }
}
