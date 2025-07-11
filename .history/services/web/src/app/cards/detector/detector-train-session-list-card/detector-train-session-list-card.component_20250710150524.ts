import { Component, Input, OnInit } from '@angular/core';
import { Detector, TrainSession, TrainSessionStatus } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-train-session-list-card',
  standalone: false,
  templateUrl: './detector-train-session-list-card.component.html',
  styleUrl: './detector-train-session-list-card.component.scss'
})
export class DetectorTrainSessionListCardComponent extends BaseComponent implements OnInit {
  @Input() detector!: Detector;
  total = 0;
  limit = 10;
  page = 1;
  skip = 0;
  search = "";
  sessions: TrainSession[] = [];
  TrainSessionStatus = TrainSessionStatus;
  ngOnInit(): void {
      this.load();
  }

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

  back(){

  }

  remove(session:TrainSession){
    if (!session._id) return;
    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant("trainer.session.removing"));
    this.ctx.api.trainer.trainerSessionRemove(session._id).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.load();
      },
      error: (result)=>{
        this.loading.next(undefined);
          this.error.next(result.error.detail);
      }
    })

  }
}
