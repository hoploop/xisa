import { Component } from '@angular/core';
import { LogoutComponent } from '@auth/logout/logout.component';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-menu',
  standalone: false,
  templateUrl: './menu.component.html',
  styleUrl: './menu.component.scss'
})
export class MenuComponent extends BaseComponent{

  logged = this.ctx.beat.auth.logged;


  onResizeTop(event:[number,number]){
    this.ctx.resizeTop.next(event);
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
}
