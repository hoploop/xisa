import { Component, Input, OnInit } from '@angular/core';
import { TrainSession } from '@api/index';
import { environment } from '@environments/environment';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-train-lab-modal',
  standalone: false,
  templateUrl: './detector-train-lab-modal.component.html',
  styleUrl: './detector-train-lab-modal.component.scss',
})
export class DetectorTrainLabModalComponent extends BaseComponent implements OnInit {
  @Input() session!: TrainSession;
  url?:string = undefined;
  dismiss() {
    this.ctx.dismissModal();
  }

  ngOnInit(): void {
    if (this.session.results){
      this.url = environment.resultsUrl+this.session.results+'/results.png';
    }

  }


}
