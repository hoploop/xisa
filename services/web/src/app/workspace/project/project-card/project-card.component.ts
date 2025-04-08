import { Component, Input } from '@angular/core';
import { Project } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { ProjectPageComponent } from '../project-page/project-page.component';

@Component({
  selector: 'app-project-card',
  standalone: false,
  templateUrl: './project-card.component.html',
  styleUrl: './project-card.component.scss',
})
export class ProjectCardComponent extends BaseComponent {
  @Input() project!: Project;

  goToProject() {
    this.ctx.open(ProjectPageComponent, { project: this.project }).subscribe();
    this.ctx.beat.menu.project.next(this.project);
  }
}
