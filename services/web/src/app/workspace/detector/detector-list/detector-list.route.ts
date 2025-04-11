import { Component, OnInit } from '@angular/core';
import { RouteComponent } from '@utils/route/route.component';
import { DetectorListComponent } from './detector-list.component';

@Component({
  selector: 'app-detector-list-route',
  standalone: false,
  template: '',
})
export class DetectorListRoute extends RouteComponent implements OnInit {
  ngOnInit(): void {
    let projectId = this.getParam('project_id');
    if (!projectId) return;
    this.ctx.api.workspace.workspaceProjectLoad(projectId).subscribe({
      next: (result) => {
        this.ctx.open(DetectorListComponent, { project: result }).subscribe();
      },
    });
  }
}
