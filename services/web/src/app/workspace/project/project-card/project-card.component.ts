import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Project } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { ProjectFormComponent } from '../project-form/project-form.component';

@Component({
  selector: 'app-project-card',
  standalone: false,
  templateUrl: './project-card.component.html',
  styleUrl: './project-card.component.scss'
})
export class ProjectCardComponent extends BaseComponent {
  @Input() project!:Project;

  goToProject(){
      this.navigateProjectPage(this.project);
  }

}
