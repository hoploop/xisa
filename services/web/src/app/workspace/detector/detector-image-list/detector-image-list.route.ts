import { Component, OnInit } from '@angular/core';
import { RouteComponent } from '@utils/route/route.component';
import { DetectorImageListComponent } from './detector-image-list.component';
import { DetectorImageMode } from '@api/model/detector-image-mode';

@Component({
  selector: 'app-detector-image-list-route',
  standalone: false,
  template: '',
})
export class DetectorImageListRoute extends RouteComponent implements OnInit {
  DetectorImageMode = DetectorImageMode;

  ngOnInit(): void {
    let detectorId = this.getParam('detector_id');
    if (!detectorId) return;
    this.ctx.api.detector.detectorLoad(detectorId).subscribe({
      next: (result) => {
        this.ctx.open(DetectorImageListComponent, { detector: result }).subscribe();
      },
    });
  }
}
