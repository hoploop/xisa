import { Component, OnInit } from '@angular/core';
import { Detector } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-image-list-page',
  standalone: false,
  templateUrl: './detector-image-list-page.component.html',
  styleUrl: './detector-image-list-page.component.scss',
})
export class DetectorImageListPageComponent
  extends BaseComponent
  implements OnInit
{
  detector?: Detector;

  ngOnInit(): void {
    let detectorId = this.getRouteParam('detector_id');
    if (detectorId) {
      this.ctx.api.detector.detectorLoad(detectorId).subscribe({
        next: (result) => {
          this.detector = result;
        },
        error: (result) => {
          this.log.warn(result.error.detail);
        },
      });
    }
  }
}
