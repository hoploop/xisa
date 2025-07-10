import { Component } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-train-session-list-card',
  standalone: false,
  templateUrl: './detector-train-session-list-card.component.html',
  styleUrl: './detector-train-session-list-card.component.scss'
})
export class DetectorTrainSessionListCardComponent extends BaseComponent {
  total = 0;
  limit = 10;
  page = 1;
  skip = 0;

  onnPageChange(value:number){
    this.skip = (value-1) * this.limit;
    this.page = value;
    this.load();
  }

  load(){

  }
}
