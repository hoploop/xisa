import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ContextService } from '@services/context.service';
import { FAIconType, BIconType } from '@constants/icons';
import { BehaviorSubject } from 'rxjs';


@Component({
  selector: 'app-base',
  standalone: false,
  templateUrl: './base.component.html',
  styleUrl: './base.component.scss'
})
export class BaseComponent {
  FAIconType = FAIconType;
  BIconType = BIconType;
  loading = new BehaviorSubject<string|undefined>(undefined);
  error = new BehaviorSubject<string|undefined>(undefined);


  constructor(protected ctx:ContextService, protected router:Router,protected route:ActivatedRoute){

  }

  protected setError(value:string|undefined){
    this.error.next(value);
  }

  protected setLoading(value:string|undefined){
    this.loading.next(value);
  }
}
