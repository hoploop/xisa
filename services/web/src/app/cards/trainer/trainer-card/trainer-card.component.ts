import { Component, Input } from '@angular/core';
import { Detector, Project } from '@api/index';
import { DetectorSelectorModalComponent } from '@modals/detector/detector-selector-modal/detector-selector-modal.component';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-trainer-card',
  standalone: false,
  templateUrl: './trainer-card.component.html',
  styleUrl: './trainer-card.component.scss'
})
export class TrainerCardComponent extends BaseComponent {
  @Input() project!:Project;

  navigateDetectors(){
    if (!this.project) return;
    this.router.navigate(['detector/list',this.project._id]);
  }

  selectDetector(){
    this.ctx.openModal<Detector|undefined>(DetectorSelectorModalComponent,{project:this.project}).subscribe({
      next: (result)=>{
        if (result){
          this.router.navigate(['detector/page',result._id]);
        }
      },
      error: (result)=>{
        this.log.warn(result.error.detail);
      }
    })
  }
}
