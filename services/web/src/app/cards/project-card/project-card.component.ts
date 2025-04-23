import { Component, Input } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';
import { Project } from '@api/index';
import { ProjectFormModalComponent } from '@modals/project-form-modal/project-form-modal.component';

@Component({
  selector: 'app-project-card',
  standalone: false,
  templateUrl: './project-card.component.html',
  styleUrl: './project-card.component.scss'
})
export class ProjectCardComponent extends BaseComponent{

  @Input() project!:Project;

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
