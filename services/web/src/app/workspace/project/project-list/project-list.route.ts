import { Component, OnInit } from "@angular/core";
import { RouteComponent } from "@utils/route/route.component";
import { ProjectListComponent } from "./project-list.component";

@Component({
  selector: 'app-project-list-route',
  standalone: false,
  template: ''
})
export class ProjectListRoute extends RouteComponent implements OnInit {

  ngOnInit(): void {
      this.ctx.beat.menu.project.next(undefined);
      this.ctx.open(ProjectListComponent).subscribe();

  }


}
