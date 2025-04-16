import { Component, OnInit } from '@angular/core';
import { Project } from '@api/index';
import { MenuArea } from '@models/menu-area-enum';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-menu-page',
  standalone: false,
  templateUrl: './menu-page.component.html',
  styleUrl: './menu-page.component.scss'
})
export class MenuPageComponent extends BaseComponent {
  project?:Project;
  area:MenuArea = MenuArea.UNKNOWN;

}
