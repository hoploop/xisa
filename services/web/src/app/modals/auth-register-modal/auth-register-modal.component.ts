import { Component } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-auth-register-modal',
  standalone: false,
  templateUrl: './auth-register-modal.component.html',
  styleUrl: './auth-register-modal.component.scss'
})
export class AuthRegisterModalComponent extends BaseComponent {
  username = '';
  password = '';
  email = '';

  valid = new BehaviorSubject<boolean>(false);

  dismiss() {
    this.ctx.closeModal(undefined);
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

    if (this.email.trim() == '') {
      this.valid.next(false);
      return;
    }

    this.valid.next(true);
  }

  onUsernameChange(value: string) {
    this.username = value;
    this.validate();
  }

  onEmailChange(value: string) {
    this.email = value;
    this.validate();
  }

  onPasswordChange(value: string) {
    this.password = value;
    this.validate();
  }

  register() {
    if (!this.valid.getValue()) return;
    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant('auth.registering'));

    this.ctx.api.setSession(this.ctx.session);
    this.ctx.api.auth
      .authRegister({
        username: this.username,
        email: this.email,
        password: this.password,
      })
      .subscribe({
        next: (result) => {},
        error: (result) => {
          this.loading.next(undefined);
          this.error.next(result.error.detail);
        },
      });
  }
}
