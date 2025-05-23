import { Component } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-auth-login-modal',
  standalone: false,
  templateUrl: './auth-login-modal.component.html',
  styleUrl: './auth-login-modal.component.scss'
})
export class AuthLoginModalComponent extends BaseComponent {
  username = '';
  password = '';
  valid = new BehaviorSubject<boolean>(false);

  dismiss() {
    this.ctx.closeModal(undefined);
  }

  onUsernameChange(value: string) {
    this.username = value;
    this.validate();
  }

  onPasswordChange(value: string) {
    this.password = value;
    this.validate();
  }

  validate() {
    if (this.username.trim() == '') {
      this.valid.next(false);
      return;
    }

    if (this.password.trim() == '') {
      this.valid.next(false);
      return;
    }

    this.valid.next(true);
  }

  login() {
    if (!this.valid.getValue()) return;
    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant('auth.logging'));

    this.ctx.api.setSession(this.ctx.session);
    this.ctx.api.auth.authLogin(this.username, this.password).subscribe({
      next: (result) => {
        this.ctx.api.setToken(result.access_token);
        this.ctx.beat.auth.logged.next(true);
        this.ctx.closeModal(result.access_token);
      },
      error: (result) => {
        this.loading.next(undefined);
        this.error.next(result.error.detail);
        this.ctx.beat.auth.logged.next(false);
        this.ctx.dismissModal();
      },
    });
  }

  register() {
    //this.registering.next(true);
  }
}
