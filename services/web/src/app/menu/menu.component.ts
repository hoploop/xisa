import { Component, Input, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Project } from '@api/index';
import { LoginComponent } from '@auth/login/login.component';
import { LogoutComponent } from '@auth/logout/logout.component';
import { RegisterComponent } from '@auth/register/register.component';
import { ContextService } from '@services/context.service';
import { BaseComponent } from '@utils/base/base.component';
import { DetectorListComponent } from '@workspace/detector/detector-list/detector-list.component';
import { ProjectListComponent } from '@workspace/project/project-list/project-list.component';
import { ProjectPageComponent } from '@workspace/project/project-page/project-page.component';
import { RecordListComponent } from '@workspace/record/record-list/record-list.component';
import { NGXLogger } from 'ngx-logger';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-menu',
  standalone: false,
  templateUrl: './menu.component.html',
  styleUrl: './menu.component.scss',
})
export class MenuComponent extends BaseComponent implements OnInit, OnDestroy {
  @Input() project?: Project;
  logged = this.ctx.beat.auth.logged;
  subs = new Subscription();



  ngOnInit(): void {
    this.check();

    this.subs.add(
      this.ctx.beat.menu.project.subscribe((result) => {
        this.project = result;
      })
    );
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
    this.router.navigate(['project/list']);
  }

  navigateProjectPage() {
    if (!this.project) return;
    this.router.navigate(['project/page',this.project._id])
  }

  navigateProjectDetectors() {
    if (!this.project) return;
    this.router.navigate(['detector/list',this.project._id]);

  }

  navigateProjectRecords() {
    if (!this.project) return;
    this.router.navigate(['record/list',this.project._id]);
  }
}
