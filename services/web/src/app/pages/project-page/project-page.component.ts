import { Component, Input, OnInit } from '@angular/core';
import { Project } from '@api/index';
import { MenuArea } from '@models/menu-area-enum';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-project-page',
  standalone: false,
  templateUrl: './project-page.component.html',
  styleUrl: './project-page.component.scss'
})
export class ProjectPageComponent extends BaseComponent implements OnInit{
  project?: Project;

  ngOnInit(): void {
    this.ctx.beat.area.next(MenuArea.PROJECT);
      let projectId = this.getRouteParam('project_id');
      if (projectId){
        this.ctx.api.project.projectLoad(projectId).subscribe({
          next: (result)=>{
            this.project = result;
            this.ctx.beat.project.next(result);
          },
          error: (result)=>{
            this.log.warn(result.error.detail);
          }
        })
      }
  }


}
