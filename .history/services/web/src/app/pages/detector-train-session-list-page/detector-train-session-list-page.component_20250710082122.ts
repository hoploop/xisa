import { Component, OnInit } from '@angular/core';
import { Detector } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-train-session-list-page',
  standalone: false,
  templateUrl: './detector-train-session-list-page.component.html',
  styleUrl: './detector-train-session-list-page.component.scss',
})
export class DetectorTrainSessionListPageComponent
  extends BaseComponent
  implements OnInit
{
  detector?: Detector;
  ngOnInit(): void {
    let detectorId = this.getRouteParam('detector_id');
    if (detectorId) {
      this.loadDetector(detectorId);
    }
  }

  loadDetector(id: string) {
    this.ctx.api.detector.detectorLoad(id).subscribe({
      next: (result) => {
        this.detector = result;
      },
      error: (result) => {
        this.log.warn(result.error.detail);
      },
    });
  }
}
