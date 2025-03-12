import { Component } from '@angular/core';
import { BIconType, FAIconType } from '@constants/icons';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-unregister',
  templateUrl: './unregister.component.html',
  styleUrl: './unregister.component.scss',
  standalone: false,
})
export class UnregisterComponent {
  BIconType = BIconType;
  FAIconType = FAIconType;
  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);

  constructor(private ctx: ContextService) {}

  unregister() {
    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant('auth.unregistering'));

    this.ctx.api.auth.authUnregister().subscribe({
      next: (result) => {},
      error: (result) => {
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      },
    });
  }
}
