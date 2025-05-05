import { Component, OnInit } from '@angular/core';
import { MenuArea } from '@models/menu-area-enum';
import { BaseComponent } from '@utils/base/base.component';
import { Project, Record } from '@api/index';
@Component({
  selector: 'app-player-page',
  standalone: false,
  templateUrl: './player-page.component.html',
  styleUrl: './player-page.component.scss',
})
export class PlayerPageComponent extends BaseComponent implements OnInit {
  record?:Record;
  project?: Project;

  ngOnInit(): void {
    this.ctx.beat.area.next(MenuArea.AUTO);
    let recordId = this.getRouteParam('record_id');
    if (!recordId) return;
    this.ctx.api.recorder.recorderLoad(recordId).subscribe({
      next: (result)=>{
        this.record = result;
        this.ctx.beat.record.next(result);

        this.ctx.api.project.projectLoad(result.project).subscribe({
          next: (resultb)=>{
            this.project = resultb;
            this.ctx.beat.project.next(resultb);

          }
        })
      },
      error: (result)=>{
        this.log.error(result.error.detail);
      }
    })
  }
}
