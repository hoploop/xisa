import { Component } from '@angular/core';
import { LoginComponent } from '@auth/login/login.component';
import { LogoutComponent } from '@auth/logout/logout.component';
import { RegisterComponent } from '@auth/register/register.component';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-template-menu',
  standalone: false,
  templateUrl: './template-menu.component.html',
  styleUrl: './template-menu.component.scss'
})
export class TemplateMenuComponent extends BaseComponent{
  home(){
    this.router.navigate([{outlets:{'primary':'welcome','menu':'welcome'}}]);
  }
  logged = this.ctx.beat.auth.logged;


  projects(){
    this.router.navigate([{outlets:{'primary':'project/list','menu':'project/list'}}]);
  }

  logout(){
    this.ctx.openModal(LogoutComponent,{}).subscribe({
      next:(result)=>{
        if (result!=undefined){
          this.router.navigateByUrl('/welcome');
        }
      },
      error:(result)=>{}
    })
  }

   login(){
      this.ctx.openModal<string|undefined>(LoginComponent,{}).subscribe({
        next: (result)=>{ if (result!=undefined){
          this.router.navigateByUrl('/project/list');
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
