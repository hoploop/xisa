import { Component, Input } from '@angular/core';
import { DetectorClass } from '@api/index';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-detector-class-list',
  standalone: false,
  templateUrl: './detector-class-list.component.html',
  styleUrl: './detector-class-list.component.scss'
})
export class DetectorClassListComponent {
 loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);
  @Input() detectorId?: string;
  classes: DetectorClass[] = []
  total: number = 0;
  skip:number = 0;
  limit:number = 10;
  search:string = '';

  constructor(private ctx:ContextService){}

  ngOnInit(): void {
      this.load();
  }

  onChangeSearch(value:string){
    this.skip = 0;
    this.search = value;
    this.load();
  }

  onSkipChange(value:number){
    this.skip = value;
    this.load();
  }

  onLimitChange(value:number){
    this.limit = value;
    this.load();
  }

  load(){
    if (!this.detectorId) return;
    this.loading.next(this.ctx.translate.instant("workspace.detector.class.loadings"));
    this.error.next(undefined);
    this.ctx.api.detector.detectorClassListDetectorid(this.detectorId,this.skip,this.limit,this.search).subscribe({
      next: (result)=>{
        this.total = result.total;
        this.classes = result.classes;
        this.loading.next(undefined);
      },
      error: (result)=>{
        this.error.next(result.error.detail);
        this.loading.next(undefined);
      }
    })
  }
}
