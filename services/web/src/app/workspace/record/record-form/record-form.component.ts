import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';
import { FAIconType } from '@constants/icons';

@Component({
  selector: 'app-record-form',
  standalone: false,
  templateUrl: './record-form.component.html',
  styleUrl: './record-form.component.scss',
})
export class RecordFormComponent {
  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);
  name: string = '';
  description: string|undefined = '';
  FAIconType = FAIconType;
  recordId?:string;
  projectId?:string;

  constructor(
    private ctx: ContextService,
    private router: Router,
    route: ActivatedRoute
  ) {
    this.recordId = route.snapshot.paramMap.get('record_id') || undefined;
  }

  ngOnInit(): void {
    this.load();
  }

  load(){
    if (!this.recordId) return;
    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant('workspace.record.loading'));
    this.ctx.api.record.recordLoadId(this.recordId).subscribe({
      next: (result)=>{
        this.name = result.name;
        this.description = result.description;
        this.loading.next(undefined);
        this.projectId = result.project;
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }

   remove(){
      if (!this.recordId) return;
      if (!this.projectId) return;
      this.error.next(undefined);

      this.loading.next(this.ctx.translate.instant('workspace.record.removing'));
      this.ctx.api.record.recordRemove(this.recordId).subscribe({
        next: (result)=>{
          this.loading.next(undefined);
          this.router.navigateByUrl('/record/list/'+this.projectId);
        },
        error: (result)=>{
          this.loading.next(undefined);
          this.error.next(result.error.detail);
        }
    })
    }


  cancel(){
    if (!this.projectId) return;
    this.router.navigateByUrl('/record/list'+this.projectId);
  }

  save(){
    if (!this.recordId) return;
    if (!this.projectId) return;
    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant('workspace.record.saving'));
    this.ctx.api.record.recordEdit(this.recordId,this.name,this.description||'').subscribe({
      next: (result)=>{
          this.loading.next(undefined);
          this.router.navigateByUrl('/record/list/'+this.projectId);
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }
}
