import { Component, Input } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-train-session-list-card',
  standalone: false,
  templateUrl: './detector-train-session-list-card.component.html',
  styleUrl: './detector-train-session-list-card.component.scss'
})
export class DetectorTrainSessionListCardComponent extends BaseComponent {
  @Input() detector!: Detector;
  total = 0;
  limit = 10;
  page = 1;
  skip = 0;
  search = "";

  onnPageChange(value:number){
    this.skip = (value-1) * this.limit;
    this.page = value;
    this.load();
  }

  onChangeSearch(value:string){
    this.search = value;
    this.skip = 0;
    this.load();
  }

  load(){
      this.ctx.api.trainer.trainerSessionList()
  }
}
