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
  projectId?:string| null;

    ngOnInit(): void {
        this.ctx.beat.area.next(MenuArea.TRAIN);
        this.projectId = this.getRouteParam('project_id');

    }

    navigateDetectors(){
      if (!this.projectId) return;
      this.router.navigate(['detector/list',this.projectId]);
    }


}
