import { Component, OnInit } from '@angular/core';
import { MenuArea } from '@models/menu-area-enum';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-auto-page',
  standalone: false,
  templateUrl: './auto-page.component.html',
  styleUrl: './auto-page.component.scss',
})
export class AutoPageComponent extends BaseComponent implements OnInit {
  ngOnInit(): void {
    this.ctx.beat.area.next(MenuArea.AUTO);
  }
}
