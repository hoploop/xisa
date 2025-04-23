import { Component, Input } from '@angular/core';
import { Project } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-card',
  standalone: false,
  templateUrl: './record-card.component.html',
  styleUrl: './record-card.component.scss'
})
export class RecordCardComponent extends BaseComponent{
  @Input() project!:Project;

  navigateVideoList(){
    if (!this.project) return;
    this.router.navigate(['record/list',this.project._id])

  }
}
