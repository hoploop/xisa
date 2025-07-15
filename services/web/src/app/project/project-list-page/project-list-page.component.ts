import { Component, OnInit } from '@angular/core';
import { MenuArea } from '@home/menu-area-enum';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-project-list-page',
  standalone: false,
  templateUrl: './project-list-page.component.html',
  styleUrl: './project-list-page.component.scss',
})
export class ProjectListPageComponent extends BaseComponent implements OnInit {
  ngOnInit(): void {
    this.ctx.beat.project.next(undefined);
    this.ctx.beat.record.next(undefined);
    this.ctx.beat.area.next(MenuArea.PROJECTS);
  }
}
