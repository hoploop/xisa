import { Component, OnInit } from '@angular/core';
import { Detector } from '@api/index';
import { MenuArea } from '@models/menu-area-enum';
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
          this.ctx.api.project.projectLoad(result.project).subscribe({
            next: (resultb)=>{
              this.ctx.beat.project.next(resultb);
              this.ctx.beat.record.next(undefined);
              this.ctx.beat.area.next(MenuArea.PROJECT);
            }
          })

        },
        error: (result) => {
          this.log.warn(result.error.detail);
        },
      });
    }
  }
}
