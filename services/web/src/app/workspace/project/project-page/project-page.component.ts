import { Component, Input } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';
import { Project } from '@api/index';
import { ProjectFormComponent } from '../project-form/project-form.component';

@Component({
  selector: 'app-project-page',
  standalone: false,
  templateUrl: './project-page.component.html',
  styleUrl: './project-page.component.scss',
})
export class ProjectPageComponent extends BaseComponent {
  @Input() project!: Project;

  edit(project: Project) {
    this.ctx
      .openModal<undefined>(ProjectFormComponent, {
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
