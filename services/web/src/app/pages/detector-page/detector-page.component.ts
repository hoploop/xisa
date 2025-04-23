import { Component, OnInit } from '@angular/core';
import { Detector, Project } from '@api/index';
import { MenuArea } from '@models/menu-area-enum';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-page',
  standalone: false,
  templateUrl: './detector-page.component.html',
  styleUrl: './detector-page.component.scss'
})
export class DetectorPageComponent extends BaseComponent implements OnInit {
  detector?:Detector;
  project?:Project;

  ngOnInit(): void {

    let detectorId = this.getRouteParam('detector_id');
    if (detectorId){
      this.loadDetector(detectorId);
    }
  }

  loadProject(id:string){
    this.ctx.api.project.projectLoad(id).subscribe(
      {
        next: (result)=>{
          this.project = result;
          this.ctx.beat.project.next(result);
          this.ctx.beat.area.next(MenuArea.TRAIN);
        },
        error: (result)=>{
          this.log.warn(result.error.detail);
        }
      }
    )
  }

  loadDetector(id:string){
    this.ctx.api.detector.detectorLoad(id).subscribe({
      next: (result)=>{
        this.detector = result;
        this.loadProject(result.project);

      },
      error: (result)=>{
        this.log.warn(result.error.detail);
      }
    })
  }
}
