import { Component, OnInit } from '@angular/core';
import { Project } from '@api/index';
import { MenuArea } from '@models/menu-area-enum';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-page',
  standalone: false,
  templateUrl: './record-page.component.html',
  styleUrl: './record-page.component.scss'
})
export class RecordPageComponent extends BaseComponent implements OnInit {
  project?:Project;

  ngOnInit(): void {

      this.ctx.beat.area.next(MenuArea.RECORD);
      let projectId = this.getRouteParam('project_id');
      if (projectId){
      this.ctx.api.project.projectLoad(projectId).subscribe({
        next: (result)=>{
          this.project = result;
        },
        error: (result)=>{
          this.log.warn(result.error.detail);
        }
      })
    }
  }

}
