import { Component } from '@angular/core';
import { ContextService } from '@services/context.service';

@Component({
  selector: 'app-menu',
  standalone: false,
  templateUrl: './menu.component.html',
  styleUrl: './menu.component.scss'
})
export class MenuComponent {

  constructor(private ctx:ContextService){

  }
  onResizeTop(event:[number,number]){
    this.ctx.resizeTop.next(event);
  }
}
