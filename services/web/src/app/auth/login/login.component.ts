import { Component, EventEmitter, Output } from '@angular/core';
import { ContextService } from '@services/context.service';
import { BIconType, FAIconType } from '@constants/icons';
import { BehaviorSubject } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss',
  standalone: false,
})
export class LoginComponent {
  username = '';
  password = '';
  BIconType = BIconType;
  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);
  valid = new BehaviorSubject<boolean>(false);

  FAIconType = FAIconType;

  constructor(private ctx: ContextService,private router:Router) {}



  onUsernameChange(value:string){
    this.username = value;
    this.validate();
  }

  onPasswordChange(value:string){
    this.password = value;
    this.validate();
  }

  validate(){
    if (this.username.trim() == ''){
      this.valid.next(false);
      return;
    }

    if (this.password.trim()==''){
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
    this.ctx.api.auth.authLogin(this.username,this.password).subscribe({
      next: (result)=>{
        this.ctx.api.setToken(result.access_token);
        this.ctx.beat.auth.logged.next(true);
        this.router.navigateByUrl('/');
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
        this.ctx.beat.auth.logged.next(false);
      }
    })
  }

  register(){
    //this.registering.next(true);

  }
}
