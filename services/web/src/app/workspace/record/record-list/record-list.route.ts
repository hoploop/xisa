import { Component, OnInit } from '@angular/core';
import { RouteComponent } from '@utils/route/route.component';
import { RecordListComponent } from './record-list.component';

@Component({
  selector: 'app-record-list-route',
  standalone: false,
  template: '',
})
export class RecordListRoute extends RouteComponent implements OnInit {
  ngOnInit(): void {
    let projectId = this.getParam('project_id');
    if (!projectId) return;
    this.ctx.api.workspace.workspaceProjectLoad(projectId).subscribe({
      next: (result) => {
        this.ctx.open(RecordListComponent, { project: result }).subscribe();
      },
    });
  }
}
