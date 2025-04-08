import { Component } from '@angular/core';
import { LoginComponent } from '@auth/login/login.component';
import { RegisterComponent } from '@auth/register/register.component';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-welcome',
  standalone: false,
  templateUrl: './welcome.component.html',
  styleUrl: './welcome.component.scss'
})
export class WelcomeComponent extends BaseComponent{

  login(){
    this.ctx.openModal<string|undefined>(LoginComponent,{}).subscribe({
      next: (result)=>{ if (result!=undefined){

      }},
      error: (result)=>{}
    })
  }

  register(){
    this.ctx.openModal(RegisterComponent,{}).subscribe({
      next: (result)=>{},
      error: (result)=>{}
    })
  }
}
