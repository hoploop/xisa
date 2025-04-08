import { Component, Input, OnDestroy, OnInit } from '@angular/core';
import { Project } from '@api/index';
import { LoginComponent } from '@auth/login/login.component';
import { LogoutComponent } from '@auth/logout/logout.component';
import { RegisterComponent } from '@auth/register/register.component';
import { BaseComponent } from '@utils/base/base.component';
import { DetectorListComponent } from '@workspace/detector/detector-list/detector-list.component';
import { ProjectListComponent } from '@workspace/project/project-list/project-list.component';
import { ProjectPageComponent } from '@workspace/project/project-page/project-page.component';
import { RecordListComponent } from '@workspace/record/record-list/record-list.component';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-menu',
  standalone: false,
  templateUrl: './menu.component.html',
  styleUrl: './menu.component.scss'
})
export class MenuComponent extends BaseComponent implements OnInit, OnDestroy {
  @Input() project?:Project;
  logged = this.ctx.beat.auth.logged;
  subs = new Subscription();

  ngOnInit(): void {
    this.check();

    this.subs.add(this.ctx.beat.menu.project.subscribe(result=>{
      this.project = result;
    }))
  }

  ngOnDestroy(): void {
      this.subs.unsubscribe();
  }

  check() {
    this.error.next(undefined);
    let token = this.ctx.api.getToken();
    if (token == null) {
      this.ctx.beat.auth.logged.next(false);
      return;
    }
    this.ctx.api.setToken(token);
    this.loading.next(this.ctx.translate.instant('auth.checking'));
    this.ctx.api.auth.authCheck().subscribe({
      next: (result) => {
        this.loading.next(undefined);
        this.ctx.beat.auth.logged.next(true);
      },
      error: (result) => {
        this.loading.next(undefined);
        this.error.next(result.error.detail);
        this.ctx.api.remToken();
        this.ctx.beat.auth.logged.next(false);
      },
    });
  }

  logout() {
    this.ctx.openModal(LogoutComponent, {}).subscribe({
      next: (result) => {
        if (result != undefined) {
        }
      },
      error: (result) => {},
    });
  }

  login() {
    this.ctx.openModal<string | undefined>(LoginComponent, {}).subscribe({
      next: (result) => {
        if (result != undefined) {
        }
      },
      error: (result) => {},
    });
  }

  register() {
    this.ctx.openModal(RegisterComponent, {}).subscribe({
      next: (result) => {},
      error: (result) => {},
    });
  }


  navigateProjects() {
      this.ctx.open(ProjectListComponent).subscribe();
      this.ctx.beat.menu.project.next(undefined);
    }

    navigateProjectPage() {
      if (!this.project) return;
      this.ctx.open(ProjectPageComponent, { project: this.project }).subscribe();
    }

    navigateProjectDetectors() {
      if (!this.project) return;
      this.ctx.open(DetectorListComponent, { project: this.project }).subscribe();
    }

    navigateProjectRecords() {
      if (!this.project) return;
      this.ctx.open(RecordListComponent, { project: this.project }).subscribe();
    }
}
