import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { DetectorTrainingSession } from '@api/index';
import { FAIconType } from '@constants/icons';
import { ContextService } from '@services/context.service';
import { BehaviorSubject, filter, map, Subscription } from 'rxjs';

@Component({
  selector: 'app-detector-learn',
  standalone: false,
  templateUrl: './detector-learn.component.html',
  styleUrl: './detector-learn.component.scss',
})
export class DetectorLearnComponent implements OnInit, OnDestroy {
  FAIconType = FAIconType;
  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);
  subs = new Subscription();
  detectorId?: string;
  progress: number = -1;
  constructor(
    private ctx: ContextService,
    private router: Router,
    route: ActivatedRoute
  ) {
    this.detectorId = route.snapshot.paramMap.get('detector_id') || undefined;
  }

  train(){
    if (!this.detectorId) return;
    this.progress = 0;
    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant('workspace.detector.training'));
    this.ctx.api.detector.detectorTrain(this.detectorId,3).subscribe({
      next: (result)=>{},
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }

  ngOnInit(): void {
    let filtered = this.ctx.ws.messages$.pipe(filter(msg => msg.type == 'detector.training.session' && msg.detector == this.detectorId));
    this.subs.add(filtered.subscribe({
      next: (result)=>{
          let res = result as DetectorTrainingSession;
            this.progress =  Math.round((res.epoch_progress / res.epoch_total)*100);
            if (this.progress >=99){
              this.loading.next(undefined);
            }

      }
    }));

  }

  ngOnDestroy(): void {
    this.subs.unsubscribe();
  }
}
