import { Component, OnInit } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';
import { WorkspaceModule } from '../../workspace.module';
import { Project } from '@api/index';
import { ProjectFormComponent } from '../project-form/project-form.component';

@Component({
  selector: 'app-project-page',
  standalone: false,
  templateUrl: './project-page.component.html',
  styleUrl: './project-page.component.scss'
})
export class ProjectPageComponent extends BaseComponent implements OnInit{
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

    edit(project: Project) {
      this.ctx
        .openModal<undefined>(ProjectFormComponent, {
          project: project,
        })
        .subscribe({
          next: (result) => {

          },
          error: (result) => {},
        });
    }
}
