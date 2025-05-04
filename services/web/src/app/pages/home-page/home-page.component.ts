import { Component, OnInit } from '@angular/core';
import { MenuArea } from '@models/menu-area-enum';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-home-page',
  standalone: false,
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.scss'
})
export class HomePageComponent extends BaseComponent implements OnInit{

  ngOnInit(): void {
      this.ctx.beat.area.next(MenuArea.UNKNOWN);
      this.ctx.beat.project.next(undefined);
      this.ctx.beat.record.next(undefined);
  }
}
