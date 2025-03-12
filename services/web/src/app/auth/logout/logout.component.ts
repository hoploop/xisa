import { Component } from '@angular/core';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';
import { BIconType } from '@constants/icons';
import { Router } from '@angular/router';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrl: './logout.component.scss',
  standalone: false,
})
export class LogoutComponent {
  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);
  BIconType = BIconType;

  constructor(private ctx: ContextService,private router: Router) {}

  logout() {
    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant('auth.logging_out'));
    this.ctx.api.auth.authLogout().subscribe({
      next: (result)=>{
        this.ctx.api.remToken();
        this.ctx.beat.auth.logged.next(false);
        this.router.navigateByUrl('login');
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }
}
