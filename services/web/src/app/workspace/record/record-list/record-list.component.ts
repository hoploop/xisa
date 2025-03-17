import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FAIconType } from '@constants/icons';
import { ContextService } from '@services/context.service';
import { BehaviorSubject, Observable } from 'rxjs';
import { Record } from '@api/index';
import { BIconType } from '@constants/icons';

@Component({
  selector: 'app-record-list',
  standalone: false,
  templateUrl: './record-list.component.html',
  styleUrl: './record-list.component.scss',
})
export class RecordListComponent implements OnInit {
  projectId?: string;
  FAIconType = FAIconType;
  BIconType = BIconType;
  skip:number = 0;
  limit:number = 0;
  search:string = '';
  total:number = 0;
  records: Record[]=[]
  running?:boolean;
  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);


  constructor(
    private ctx: ContextService,
    private router: Router,
    route: ActivatedRoute
  ) {
    this.projectId = route.snapshot.paramMap.get('project_id') || undefined;
  }

  ngOnInit(): void {
    this.load();
  }

  onChangeSearch(value:string){
    this.search = value;
    this.skip = 0;
    this.load();
  }


  create(){
    this.router.navigateByUrl('/record/controller/'+this.projectId);
  }


  edit(record:Record){
    if (!record._id) return;
    this.router.navigateByUrl('/record/form/'+record._id);
  }

  studio(record:Record){
    if (!record._id) return;
    this.router.navigateByUrl('/record/studio/'+record._id);
  }

  load() {
    if (!this.projectId) return;
    this.ctx.api.record.recordRunning().subscribe({
      next: (result)=>{
        this.running = result;
      },
      error: (result)=>{
        this.running = undefined;
      }
    })

    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant('workspace.record.loadings'));
    this.ctx.api.record.recordListProjectid(this.projectId,this.skip,this.limit,this.search).subscribe(
     { next: (result)=>{
        this.loading.next(undefined);
        this.total = result.total;
        this.records = result.records;
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
  })
  }
}
