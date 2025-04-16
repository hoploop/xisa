import { Component, OnInit } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-project-list-page',
  standalone: false,
  templateUrl: './project-list-page.component.html',
  styleUrl: './project-list-page.component.scss',
})
export class ProjectListPageComponent extends BaseComponent implements OnInit {
  ngOnInit(): void {
    this.ctx.beat.menu.project.next(undefined);
  }
}
