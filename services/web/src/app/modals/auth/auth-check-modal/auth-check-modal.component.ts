import { Component, OnInit } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-auth-check-modal',
  standalone: false,
  templateUrl: './auth-check-modal.component.html',
  styleUrl: './auth-check-modal.component.scss'
})
export class AuthCheckModalComponent extends BaseComponent implements OnInit {

  ngOnInit(): void {
    this.check();
  }

  check() {
    this.error.next(undefined);
    let token = this.ctx.api.getToken();
    if (token == null) {
      this.ctx.beat.auth.logged.next(false);
      return;
    }
    this.ctx.api.setToken(token);
    this.loading.next(this.ctx.translate.instant('auth.checking'));
    this.ctx.api.auth.authCheck().subscribe({
      next: (result) => {
        this.loading.next(undefined);
        this.ctx.beat.auth.logged.next(true);

      },
      error: (result) => {
        this.loading.next(undefined);
        this.error.next(result.error.detail);
        this.ctx.api.remToken();
        this.ctx.beat.auth.logged.next(false);

      },
    });
  }
}
