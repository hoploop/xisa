import { Component, OnInit } from '@angular/core';
import { MenuArea } from '@models/menu-area-enum';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-player-page',
  standalone: false,
  templateUrl: './player-page.component.html',
  styleUrl: './player-page.component.scss',
})
export class PlayerPageComponent extends BaseComponent implements OnInit {
  ngOnInit(): void {
    this.ctx.beat.area.next(MenuArea.PLAY);
  }
}
