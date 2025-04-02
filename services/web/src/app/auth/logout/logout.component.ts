import { Component } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrl: './logout.component.scss',
  standalone: false,
})
export class LogoutComponent extends BaseComponent {
  dismiss() {
    this.ctx.closeModal(undefined);
  }

  logout() {
    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant('auth.logging_out'));
    this.ctx.api.auth.authLogout().subscribe({
      next: (result) => {
        this.ctx.api.remToken();
        this.ctx.beat.auth.logged.next(false);
        this.ctx.closeModal(true);
      },
      error: (result) => {
        this.loading.next(undefined);
        this.error.next(result.error.detail);
        this.ctx.dismissModal();
      },
    });
  }
}
