import { Component, Input, OnDestroy, OnInit } from '@angular/core';
import { Detector, Project, Record } from '@api/index';
import { AuthLoginModalComponent } from '@modals/auth-login-modal/auth-login-modal.component';
import { AuthLogoutModalComponent } from '@modals/auth-logout-modal/auth-logout-modal.component';
import { AuthRegisterModalComponent } from '@modals/auth-register-modal/auth-register-modal.component';
import { DetectorSelectorModalComponent } from '@modals/detector-selector-modal/detector-selector-modal.component';
import { RecordVideoModalComponent } from '@modals/record-video-modal/record-video-modal.component';
import { MenuArea } from '@models/menu-area-enum';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-menu-card',
  standalone: false,
  templateUrl: './menu-card.component.html',
  styleUrl: './menu-card.component.scss',
})
export class MenuCardComponent
  extends BaseComponent
  implements OnInit, OnDestroy
{
  project?: Project;
  record?: Record;
  area: MenuArea = MenuArea.UNKNOWN;
  logged = this.ctx.beat.auth.logged;
  MenuArea = MenuArea;

  ngOnInit(): void {
    this.check();
    this.subs.add(
      this.ctx.beat.project.subscribe((result) => {
        this.project = result;
      })
    );

    this.subs.add(
      this.ctx.beat.record.subscribe((result) => {
        this.record = result;
      })
    );

    this.subs.add(
      this.ctx.beat.area.subscribe((result) => {
        this.area = result;
      })
    );
  }

  ngOnDestroy(): void {
    this.subs.unsubscribe();
  }

  homeRecord() {
    if (!this.record) return;
    this.router.navigate(['record/page', this.record._id]);
  }

  homeDetector() {
    if (!this.project) return;
    this.router.navigate(['detector/list', this.project._id]);
  }


  train() {
    if (!this.project) return;
    if (!this.record) return;
    this.ctx
      .openModal<Detector | undefined>(DetectorSelectorModalComponent, {
        project: this.project,
      })
      .subscribe({
        next: (result) => {
          if (result) {
            if (this.record) {
              this.router.navigate([
                'trainer/lesson',
                result._id,
                this.record._id,
              ]);
            }
          }
        },
        error: (result) => {},
      });
  }

  video(){
    this.ctx.openModal(RecordVideoModalComponent,{record:this.record},{size:'lg',centered:true}).subscribe({
      next: (result)=>{},
      error: (result)=>{

      }
    })
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
    this.ctx.openModal(AuthLogoutModalComponent, {}).subscribe({
      next: (result) => {
        if (result != undefined) {
        }
      },
      error: (result) => {},
    });
  }

  login() {
    this.ctx
      .openModal<string | undefined>(AuthLoginModalComponent, {})
      .subscribe({
        next: (result) => {
          if (result != undefined) {
          }
        },
        error: (result) => {},
      });
  }

  register() {
    this.ctx.openModal(AuthRegisterModalComponent, {}).subscribe({
      next: (result) => {},
      error: (result) => {},
    });
  }

  navigateHome() {
    this.router.navigate(['']);
  }

  navigateProjects() {
    this.router.navigate(['project/list']);
  }

  navigateProjectPage() {
    if (!this.project) return;
    this.router.navigate(['project/page', this.project._id]);
  }

  navigateProjectDetectors() {
    if (!this.project) return;
    this.router.navigate(['detector/list', this.project._id]);
  }

  navigateProjectRecords() {
    if (!this.project) return;
    this.router.navigate(['record/list', this.project._id]);
  }

  navigateTrainerPage() {
    if (!this.project) return;
    this.router.navigate(['trainer/page', this.project._id]);
  }

  navigatePlayerPage() {
    if (!this.project) return;
    this.router.navigate(['player/page', this.project._id]);
  }

  navigateDetectors() {
    if (!this.project) return;
    this.router.navigate(['detector/list', this.project._id]);
  }

  navigateAutoPage() {
    if (!this.record) return;
    this.router.navigate(['auto/page', this.record._id]);
  }

  navigateRecordPage() {
    if (!this.project) return;
    this.router.navigate(['record/page', this.project._id]);
  }
}
