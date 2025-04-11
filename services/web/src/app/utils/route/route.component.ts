import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ContextService } from '@services/context.service';
import { NGXLogger } from 'ngx-logger';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-route',
  standalone: false,
  templateUrl: './route.component.html',
  styleUrl: './route.component.scss',
})
export class RouteComponent {
  constructor(
    protected ctx: ContextService,
    protected router: Router,
    protected route: ActivatedRoute,
    protected log: NGXLogger
  ) {}

  protected getParam(value: string): string | null {
    return this.route.snapshot.paramMap.get(value);
  }

  protected open(componentType:any,values= {}){
    this.ctx.open(componentType,values);
  }
}
