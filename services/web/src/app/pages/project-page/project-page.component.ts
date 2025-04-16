import { Component, Input, OnInit } from '@angular/core';
import { Project } from '@api/index';
import { ProjectFormModalComponent } from '@modals/project-form-modal/project-form-modal.component';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-project-page',
  standalone: false,
  templateUrl: './project-page.component.html',
  styleUrl: './project-page.component.scss'
})
export class ProjectPageComponent extends BaseComponent implements OnInit{
  project!: Project;

  ngOnInit(): void {
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

  edit(project: Project) {
    this.ctx
      .openModal<undefined>(ProjectFormModalComponent, {
        project: project,
      })
      .subscribe({
        next: (result) => {},
        error: (result) => {},
      });
  }

  navigateProjectDetectors() {
    this.router.navigate(['detector/list', this.project._id]);
  }

  navigateProjectRecords() {
    this.router.navigate(['record/list', this.project._id]);
  }
}
