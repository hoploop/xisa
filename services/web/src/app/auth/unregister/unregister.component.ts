import { Component } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-unregister',
  templateUrl: './unregister.component.html',
  styleUrl: './unregister.component.scss',
  standalone: false,
})
export class UnregisterComponent extends BaseComponent {
  dismiss() {
    this.ctx.closeModal(undefined);
  }

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
