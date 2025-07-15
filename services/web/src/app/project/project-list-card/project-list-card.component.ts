import { Component, OnInit } from '@angular/core';
import { Project } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { ProjectFormModalComponent } from '@project/project-form-modal/project-form-modal.component';

@Component({
  selector: 'app-project-list-card',
  standalone: false,
  templateUrl: './project-list-card.component.html',
  styleUrl: './project-list-card.component.scss',
})
export class ProjectListCardComponent extends BaseComponent implements OnInit {
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
    this.loading.next(this.ctx.translate.instant('project.loadings'));
    this.error.next(undefined);
    this.ctx.api.project
      .projectList(this.skip, this.limit, this.search)
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

  create() {
    this.ctx
      .openModal<Project | undefined>(ProjectFormModalComponent, {
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
}
