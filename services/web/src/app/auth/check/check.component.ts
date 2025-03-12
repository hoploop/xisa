import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';
import { FAIconType } from '@constants/icons';
import { Router } from '@angular/router';

@Component({
  selector: 'app-check',
  templateUrl: './check.component.html',
  styleUrl: './check.component.scss',
  standalone: false,
})
export class CheckComponent implements OnInit {
  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);

  FAIconType = FAIconType;

  constructor(private ctx: ContextService,private router:Router) {}

  ngOnInit(): void {
    this.check();
  }

  check() {
    this.error.next(undefined);
    let token = this.ctx.api.getToken();
    if (token == null) {
      this.router.navigateByUrl('/login');
      this.ctx.beat.auth.logged.next(false);
      return;
    }
    this.ctx.api.setToken(token);
    console.log('Checking token: '+token);
    this.loading.next(this.ctx.translate.instant('auth.checking'));
    this.ctx.api.auth.authCheck().subscribe({
      next: (result) => {
        this.loading.next(undefined);
        this.ctx.beat.auth.logged.next(true);
        this.router.navigateByUrl('/logged');
      },
      error: (result) => {
        this.loading.next(undefined);
        this.error.next(result.error.detail);
        this.ctx.api.remToken();
        this.ctx.beat.auth.logged.next(false);
        this.router.navigateByUrl('/login');
      },
    });
  }
}
