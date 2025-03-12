import { Component, Input, OnInit } from '@angular/core';
import { DetectorImage } from '@api/index';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-detector-image-list',
  standalone: false,
  templateUrl: './detector-image-list.component.html',
  styleUrl: './detector-image-list.component.scss',
})
export class DetectorImageListComponent implements OnInit {

  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);
  @Input() detectorId?: string;
  images: DetectorImage[] = []
  total: number = 0;
  skip:number = 0;
  limit:number = 10;

  constructor(private ctx:ContextService){}

  ngOnInit(): void {
      this.load();
  }

  load(){
    if (!this.detectorId) return;
    this.loading.next(this.ctx.translate.instant("workspace.detector.image.loadings"));
    this.error.next(undefined);
    this.ctx.api.detector.detectorImageListId(this.detectorId,this.skip,this.limit).subscribe({
      next: (result)=>{
        this.total = result.total;
        this.images = result.images;
        this.loading.next(undefined);
      },
      error: (result)=>{
        this.error.next(result.error.detail);
        this.loading.next(undefined);
      }
    })
  }
}
