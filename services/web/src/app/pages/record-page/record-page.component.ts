import { Component, OnInit } from '@angular/core';
import { Record } from '@api/index';
import { MenuArea } from '@models/menu-area-enum';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-page',
  standalone: false,
  templateUrl: './record-page.component.html',
  styleUrl: './record-page.component.scss'
})
export class RecordPageComponent extends BaseComponent implements OnInit {
  record?:Record;


  ngOnInit(): void {
      this.ctx.beat.area.next(MenuArea.RECORD);

      let recordId = this.getRouteParam('record_id');
      if (recordId){
      this.ctx.api.recorder.recorderLoad(recordId).subscribe({
        next: (result)=>{
          this.record = result;
          this.ctx.beat.record.next(result);
          this.ctx.api.project.projectLoad(result.project).subscribe({
            next: (resultb)=>{
              this.ctx.beat.project.next(resultb);
            }
          })
        },
        error: (result)=>{
          this.log.warn(result.error.detail);
        }
      })
    }
  }

}
