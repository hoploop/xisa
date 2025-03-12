import { Component, EventEmitter, Output } from '@angular/core';
import { BIconType, FAIconType } from '@constants/icons';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrl: './register.component.scss',
  standalone: false,
})
export class RegisterComponent {
  username = '';
  password = '';
  email = '';
  BIconType = BIconType;
  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);
  valid = new BehaviorSubject<boolean>(false);

  FAIconType = FAIconType;

  constructor(private ctx: ContextService) {}

  validate(){
    if (this.username.trim() == ''){
      this.valid.next(false);
      return;
    }

    if (this.password.trim() == ''){
      this.valid.next(false);
      return;
    }

    if (this.email.trim() == ''){
      this.valid.next(false);
      return;
    }

    this.valid.next(true);
  }

  onUsernameChange(value:string){
    this.username = value;
    this.validate();
  }

  onEmailChange(value:string){
    this.email = value;
    this.validate();
  }

  onPasswordChange(value:string){
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
        next: (result) => {

        },
        error: (result) => {
          this.loading.next(undefined);
          this.error.next(result.error.detail);
        },
      });
  }
}
