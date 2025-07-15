import { Component } from '@angular/core';
import { MenuArea } from '@home/menu-area-enum';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-home-card',
  standalone: false,
  templateUrl: './home-card.component.html',
  styleUrl: './home-card.component.scss',
})
export class HomeCardComponent extends BaseComponent {
  navigateProjects() {
    this.router.navigate(['project/list']);
    this.ctx.beat.area.next(MenuArea.PROJECTS);
  }
}
