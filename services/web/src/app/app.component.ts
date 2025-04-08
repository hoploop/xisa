import { AfterViewInit, Component, ComponentRef, ElementRef, Renderer2, ViewChild, ViewContainerRef } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { ContextService } from './services/context.service';
import { MenuComponent } from './menu/menu.component';

@Component({
  selector: 'app-root',
  standalone: false,
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent implements AfterViewInit {
  @ViewChild('main', { read: ViewContainerRef }) mainContainer!: ViewContainerRef;
  @ViewChild(MenuComponent) menuContainer!: MenuComponent;


  title = 'web';
  logged = new BehaviorSubject<boolean|undefined>(undefined);
  registering = new BehaviorSubject<boolean|undefined>(undefined);
  topMargin = new BehaviorSubject<number>(0);

  constructor(private ctx:ContextService,private renderer: Renderer2){

  }

  onResizeTop(event:[number,number]){
    this.ctx.resizeTop.next(event);
  }

  ngAfterViewInit() {
    this.ctx.initialize(this.mainContainer);

    this.ctx.resizeTop.subscribe(result=>{
      this.topMargin.next(result[1]);
    })

    this.ctx.beat.auth.logged.subscribe(result=>{
      if (result){
        let token = this.ctx.api.getToken();
        if (token){
          this.ctx.ws.connect(token,this.ctx.session);
        }

      }else{
        this.ctx.ws.close();
      }
    })


  }


}
