import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { ContextService } from '@services/context.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthGuard implements CanActivate {
  constructor(private ctx: ContextService, private router: Router) {}

  canActivate(): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      if (this.ctx.beat.auth.logged.getValue() == true) {
        observer.next(true);
      } else {
        let token = this.ctx.api.getToken();
        if (token == null) {
          this.router.navigateByUrl('/login');
          this.ctx.beat.auth.logged.next(false);
          observer.next(false);
        } else {
          this.ctx.api.setToken(token);
          console.log('Checking token: ' + token);
          this.ctx.api.auth.authCheck().subscribe({
            next: (result) => {
              this.ctx.beat.auth.logged.next(true);
              this.ctx.api.setSession(this.ctx.session);
              observer.next(true);
            },
            error: (result) => {
              this.ctx.api.remToken();
              this.ctx.beat.auth.logged.next(false);
              this.router.navigateByUrl('/login');
              observer.next(false);
            },
          });
        }
      }
    });
  }
}
