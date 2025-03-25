import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { BIconType } from '@constants/icons';
import { FAIconType } from '@constants/icons';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-record-controller',
  standalone: false,
  templateUrl: './record-controller.component.html',
  styleUrl: './record-controller.component.scss',
})
export class RecordControllerComponent implements OnInit{
  BIconType = BIconType;
  FAIconType = FAIconType;
  running?: boolean;
  name: string = new Date().toISOString();
  description:string = '';
  projectId?: string;
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

  load(){
    this.ctx.api.recorder.recorderRunning().subscribe({
      next: (result)=>{
        this.running = result;
      },
      error: (result)=>{
        this.error.next(result.error.detail);
      }
    })
  }

  start() {
    if (!this.projectId) return;
    this.ctx.api.recorder.recorderStart(this.projectId,this.name,this.description).subscribe({
      next: (result)=>{
        this.running = true;
      },
      error: (result)=>{
        this.error.next(result.error.detail);
      }
    })
  }

  stop() {
    if (!this.projectId) return;
    this.ctx.api.recorder.recorderStop().subscribe({
      next: (result)=>{
        this.running = false;
        this.cancel();
      },
      error: (result)=>{
        this.error.next(result.error.detail);
      }
    })
  }



  cancel() {
    this.router.navigateByUrl('/record/list/' + this.projectId);
  }
}
