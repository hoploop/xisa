import { Component, Input } from '@angular/core';
import { Project } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-project-detail-card',
  standalone: false,
  templateUrl: './project-detail-card.component.html',
  styleUrl: './project-detail-card.component.scss',
})
export class ProjectDetailCardComponent extends BaseComponent {
  @Input() project!: Project;

  goToProject() {
    this.router.navigate(['project/page',this.project._id]);
    this.ctx.beat.project.next(this.project);
  }
}
