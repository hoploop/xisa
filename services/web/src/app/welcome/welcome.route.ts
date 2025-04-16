import { Component, OnInit } from '@angular/core';
import { RouteComponent } from '@utils/route/route.component';
import { WelcomeComponent } from './welcome.component';

@Component({
  selector: 'app-welcome-route',
  standalone: false,
  template: '',
})
export class WelcomeRoute extends RouteComponent implements OnInit {
  ngOnInit(): void {
    this.ctx.open(WelcomeComponent).subscribe();
  }
}
