import { Component } from '@angular/core';
import { ContextService } from '@services/context.service';
import { FAIconType, BIconType } from '@constants/icons';
import { BehaviorSubject, Subscription } from 'rxjs';
import { NGXLogger } from 'ngx-logger';
import { NGIconType } from '@constants/icons';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-base',
  standalone: false,
  templateUrl: './base.component.html',
  styleUrl: './base.component.scss',
})
export class BaseComponent {
  FAIconType = FAIconType;
  BIconType = BIconType;
  NGIconType = NGIconType;
  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);
  subs = new Subscription();

  constructor(
    protected ctx: ContextService,
    protected log: NGXLogger,
    protected router: Router,
    protected route: ActivatedRoute,
    protected http: HttpClient
  ) {}

  protected setError(value: string | undefined) {
    this.error.next(value);
  }

  protected setLoading(value: string | undefined) {
    this.loading.next(value);
  }

  protected getRouteParam(value: string): string | null {
    return this.route.snapshot.paramMap.get(value);
  }
}
