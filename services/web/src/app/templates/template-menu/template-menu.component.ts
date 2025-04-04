import { Component } from '@angular/core';
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
}
