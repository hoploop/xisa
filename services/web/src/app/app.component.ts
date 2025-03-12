import { AfterViewInit, Component, ElementRef, Renderer2, ViewChild } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { ContextService } from './services/context.service';

@Component({
  selector: 'app-root',
  standalone: false,
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent implements AfterViewInit {
  @ViewChild('navbar', { static: false }) navbar!: ElementRef;

  title = 'web';
  logged = new BehaviorSubject<boolean|undefined>(undefined);
  registering = new BehaviorSubject<boolean|undefined>(undefined);

  constructor(private ctx:ContextService,private renderer: Renderer2){

  }

  ngAfterViewInit() {
    this.adjustPadding();
    window.addEventListener('resize', () => this.adjustPadding()); // Adjust padding on window resize

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


  adjustPadding() {
    if (this.navbar) {
      const navbarHeight = this.navbar.nativeElement.offsetHeight;
      this.renderer.setStyle(document.body, 'padding-top', `${navbarHeight}px`);
    }
  }
}
