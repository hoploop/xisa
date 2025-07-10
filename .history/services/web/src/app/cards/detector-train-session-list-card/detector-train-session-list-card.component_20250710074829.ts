import { Component, Input } from '@angular/core';
import { Detector, TrainSession } from '@api/index';
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
  sessions: TrainSession[] = [];

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
    if (!this.detector._id) return;
      this.error.next(undefined);
      this.ctx.api.trainer.trainerSessionList(this.detector._id,this.skip,this.limit).subscribe({
        next: (result)=>{
          this.loading.next(undefined);
          this.total = result.total;
          this.sessions = result.sessions;
        },
        error: (result)=>{
          this.loading.next(undefined);
          this.error.next(result.error.detail);
        }
      })
  }
}
