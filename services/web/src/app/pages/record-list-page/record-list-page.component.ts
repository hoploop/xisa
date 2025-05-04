import { Component, OnInit } from '@angular/core';
import { Project } from '@api/index';
import { MenuArea } from '@models/menu-area-enum';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-list-page',
  standalone: false,
  templateUrl: './record-list-page.component.html',
  styleUrl: './record-list-page.component.scss',
})
export class RecordListPageComponent extends BaseComponent implements OnInit {
  project?: Project;
  ngOnInit(): void {
    let projectId = this.getRouteParam('project_id');
    if (projectId) {
      this.ctx.api.project.projectLoad(projectId).subscribe({
        next: (result) => {
          this.project = result;
          this.ctx.beat.project.next(result);
          this.ctx.beat.area.next(MenuArea.PROJECT);
          this.ctx.beat.record.next(undefined);
        },
        error: (result) => {
          this.log.warn(result.error.detail);
        },
      });
    }
  }
}
