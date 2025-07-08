import {
  AfterViewInit,
  Component,
  OnInit,
} from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { ContextService } from './services/context.service';

@Component({
  selector: 'app-root',
  standalone: false,
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent implements AfterViewInit, OnInit {
  loaded = false;
  logged = new BehaviorSubject<boolean | undefined>(undefined);
  registering = new BehaviorSubject<boolean | undefined>(undefined);
  topMargin = new BehaviorSubject<number>(0);
  bottomMargin = new BehaviorSubject<number>(0);

  constructor(private ctx: ContextService) {}

  onResizeTop(event: [number, number]) {
    this.ctx.resizeTop.next(event);
  }

  onResizeBottom(event: [number, number]) {
    this.ctx.resizeBottom.next(event);
  }

  ngOnInit(): void {

  }

  ngAfterViewInit() {

    this.ctx.resizeTop.subscribe((result) => {
      this.topMargin.next(result[1]);
    });

    this.ctx.resizeBottom.subscribe((result) => {
      this.bottomMargin.next(result[1]);
    });

    this.ctx.beat.auth.logged.subscribe((result) => {
      if (result) {
        let token = this.ctx.api.getToken();
        if (token) {
          this.ctx.ws.connect(token, this.ctx.session);
        }
      } else {
        this.ctx.ws.close();
      }
    });

    this.ctx.translate.use('en').subscribe((result) => {
      this.loaded = true;
    });
  }
}
