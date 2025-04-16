import { Component, OnInit } from '@angular/core';
import { MenuArea } from '@models/menu-area-enum';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-page',
  standalone: false,
  templateUrl: './record-page.component.html',
  styleUrl: './record-page.component.scss'
})
export class RecordPageComponent extends BaseComponent implements OnInit {
  projectId?:string | null;

  ngOnInit(): void {
      this.projectId = this.getRouteParam('project_id');
      this.ctx.beat.area.next(MenuArea.RECORD);
  }
  navigateVideoList(){
    if (!this.projectId) return;
    this.router.navigate(['record/list',this.projectId])

  }
}
