import { Component, OnInit } from '@angular/core';
import { Project } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-list-page',
  standalone: false,
  templateUrl: './detector-list-page.component.html',
  styleUrl: './detector-list-page.component.scss'
})
export class DetectorListPageComponent extends BaseComponent implements OnInit {
  project?: Project;
  ngOnInit(): void {
      let projectId = this.getRouteParam('project_id');
      if (projectId){
        this.ctx.api.project.projectLoad(projectId).subscribe({
          next: (result)=>{
            this.project = result;
          },
          error: (result)=>{
            this.log.warn(result.error.detail);
          }
        })
      }
  }
}
