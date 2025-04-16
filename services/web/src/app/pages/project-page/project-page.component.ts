import { Component, Input, OnInit } from '@angular/core';
import { Project } from '@api/index';
import { ProjectFormModalComponent } from '@modals/project-form-modal/project-form-modal.component';
import { MenuArea } from '@models/menu-area-enum';
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

  edit(project: Project) {
    this.ctx
      .openModal<Project | undefined>(ProjectFormModalComponent, {
        project: project,
      })
      .subscribe({
        next: (result) => {
          if (result==undefined){
            this.router.navigate(['project/list']);
          }
        },
        error: (result) => {},
      });
  }

  navigateProjectDetectors() {
    this.router.navigate(['detector/list', this.project._id]);
  }

  navigateProjectRecords() {
    this.router.navigate(['record/list', this.project._id]);
  }

  navigateTrainerPage(){
    if (!this.project)return;
    this.router.navigate(['trainer/page',this.project._id]);
  }

  navigateRecordPage(){
    if (!this.project)return;
    this.router.navigate(['record/page',this.project._id]);
  }

  navigateAutoPage(){
    if (!this.project)return;
    this.router.navigate(['auto/page',this.project._id]);
  }

  navigatePlayerPage(){
    if (!this.project)return;
    this.router.navigate(['player/page',this.project._id]);
  }
}
