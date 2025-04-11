import { Component, OnInit } from '@angular/core';
import { RouteComponent } from '@utils/route/route.component';
import { ProjectPageComponent } from './project-page.component';

@Component({
  selector: 'app-project-page-route',
  standalone: false,
  template: '',
})
export class ProjectPageRoute extends RouteComponent implements OnInit {
  ngOnInit(): void {
    let projectId = this.getParam('project_id');
    if (!projectId) return;
    this.ctx.api.workspace.workspaceProjectLoad(projectId).subscribe({
      next: (result) => {
        this.ctx.beat.menu.project.next(result);
        this.ctx.open(ProjectPageComponent, { project: result }).subscribe();
      },
    });
  }
}
