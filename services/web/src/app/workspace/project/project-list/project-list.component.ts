import { Component, OnInit } from '@angular/core';
import { Project } from '@api/index';
import { ProjectFormComponent } from '../project-form/project-form.component';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-project-list',
  standalone: false,
  templateUrl: './project-list.component.html',
  styleUrl: './project-list.component.scss',
})
export class ProjectListComponent extends BaseComponent implements OnInit {
  skip: number = 0;
  limit: number = 10;
  search: string = '';
  total: number = 0;
  projects: Project[] = [];

  ngOnInit(): void {
    this.load();
  }

  onChangeSearch(value: string) {
    this.search = value;
    this.skip = 0;
    this.load();
  }

  load() {
    this.loading.next(this.ctx.translate.instant('workspace.project.loadings'));
    this.error.next(undefined);
    this.ctx.api.workspace
      .workspaceProjectList(this.skip, this.limit, this.search)
      .subscribe({
        next: (result) => {
          this.loading.next(undefined);
          this.total = result.total;
          this.projects = result.projects;
        },
        error: (result) => {
          this.loading.next(undefined);
          this.error.next(result.error.detail);
        },
      });
  }

  records(project: Project) {
    this.router.navigateByUrl('/record/list/' + project._id);
  }

  detectors(project: Project) {
    this.router.navigateByUrl('/detector/list/' + project._id);
  }

  create() {
    this.ctx
      .openModal<Project | undefined>(ProjectFormComponent, {
        project: {
          name: '',
          description: '',
        },
      })
      .subscribe({
        next: (result) => {
          if (result) {
            this.load();
          }
        },
        error: (result) => {},
      });
  }

  edit(project: Project) {
    this.ctx
      .openModal<undefined>(ProjectFormComponent, {
        project: project,
      })
      .subscribe({
        next: (result) => {
          this.load();
        },
        error: (result) => {},
      });
  }
}
