import { Component, OnInit } from '@angular/core';
import { Project } from '@api/index';
import { MenuArea } from '@models/menu-area-enum';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-trainer-page',
  standalone: false,
  templateUrl: './trainer-page.component.html',
  styleUrl: './trainer-page.component.scss'
})
export class TrainerPageComponent extends BaseComponent implements OnInit{

  project?:Project;

    ngOnInit(): void {
        this.ctx.beat.area.next(MenuArea.TRAIN);
        let projectId = this.getRouteParam('project_id');
        if (projectId){
          this.ctx.api.project.projectLoad(projectId).subscribe({
            next: (result)=>{
              this.project = result;
              this.ctx.beat.project.next(result);
              this.ctx.beat.area.next(MenuArea.TRAIN);
            },
            error: (result)=>{
              this.log.warn(result.error.detail);
            }
          })
        }
    }



}
