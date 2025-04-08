import { Component, Input } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';
import { Project } from '@api/index';
import { ProjectFormComponent } from '../project-form/project-form.component';
import { DetectorListComponent } from '@workspace/detector/detector-list/detector-list.component';
import { RecordListComponent } from '@workspace/record/record-list/record-list.component';

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
    this.ctx.open(DetectorListComponent, { project: this.project }).subscribe();
  }

  navigateProjectRecords() {
    this.ctx.open(RecordListComponent, { project: this.project }).subscribe();
  }
}
