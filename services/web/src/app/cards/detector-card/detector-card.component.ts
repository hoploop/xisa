import { Component, Input, OnInit } from '@angular/core';
import { Detector, Record } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-card',
  standalone: false,
  templateUrl: './detector-card.component.html',
  styleUrl: './detector-card.component.scss'
})
export class DetectorCardComponent extends BaseComponent implements OnInit {
  @Input() detector!:Detector;
  search:string = '';
  limit:number = 10;
  total:number = 0;
  records: Record[] = [];
  page: number = 1;

  ngOnInit(): void {
      this.loadRecords();
  }

  onChangeSearch(value:string){
    this.search = value;
    this.loadRecords();
  }

  onPageChange(value:number){
    this.page = value;
    this.loadRecords();
  }

  loadRecords(){
    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant('recorder.loadings'));
    this.ctx.api.recorder
      .recorderList(this.detector.project, (this.page-1)*this.limit, this.limit, this.search)
      .subscribe({
        next: (result) => {
          this.loading.next(undefined);
          this.total = result.total;
          this.records = result.records;
          this.log.debug('Records loaded: '+this.total.toString());
        },
        error: (result) => {
          this.loading.next(undefined);
          this.error.next(result.error.detail);
        },
      });
  }

  train(record:Record){
    this.router.navigate(['trainer/lesson',this.detector._id,record._id]);
  }
}
