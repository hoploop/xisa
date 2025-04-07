import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ContextService } from '@services/context.service';
import { FAIconType, BIconType } from '@constants/icons';
import { BehaviorSubject } from 'rxjs';
import { NGXLogger } from 'ngx-logger';
import { Project,Record } from '@api/index';


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


  constructor(protected ctx:ContextService, protected router:Router,protected route:ActivatedRoute,protected log: NGXLogger){

  }

  protected navigateProjects(){
    this.router.navigate([{outlets:{'primary':'project/list', 'menu':'project/list'}}]);
  }

  protected navigateProjectRecords(project: Project) {
    this.router.navigate([{outlets:{'primary':'record/list/' + project._id}}]);
  }

  protected navigateHome(){
    this.router.navigate([{outlets:{'primary':'welcome','menu':'welcome'}}]);
  }

  protected navigateProjectDetectors(project: Project) {
    this.router.navigate([{outlets:{'primary':'detector/list/' + project._id}}]);
  }

  protected navigateRecordStudio(record:Record,detectorId:string){
    this.router.navigate([{outlets:{'primary':'record/studio/' + record._id + '/' + detectorId}}]

    );
  }

  protected navigateProjectPage(project:Project){
    this.router.navigate([{outlets:{'primary':'project/page/'+project._id,'menu':'project/page/'+project._id}}]);
  }

  protected setError(value:string|undefined){
    this.error.next(value);
  }

  protected setLoading(value:string|undefined){
    this.loading.next(value);
  }

  protected getRouteParam(name:string): string | undefined {
    return this.route.snapshot.paramMap.get(name) || undefined;
  }


}

