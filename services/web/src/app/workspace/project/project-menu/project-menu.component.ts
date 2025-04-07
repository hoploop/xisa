import { Component, OnInit } from '@angular/core';
import { Project } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-project-menu',
  standalone: false,
  templateUrl: './project-menu.component.html',
  styleUrl: './project-menu.component.scss'
})
export class ProjectMenuComponent extends BaseComponent implements OnInit{
  project?:Project;
  ngOnInit(): void {
      let projectId = this.getRouteParam('project_id');
      if (projectId){
        this.loadProject(projectId);
      }
  }

  loadProject(projectId:string){
    this.ctx.api.workspace.workspaceProjectLoad(projectId).subscribe({
      next: (result)=>{
        this.project = result;
      },
      error: (result)=>{
        this.error.next(result.error.detail);
      }
    })
  }


}
