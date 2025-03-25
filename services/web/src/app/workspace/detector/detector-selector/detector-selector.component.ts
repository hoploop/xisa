import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Detector } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-selector',
  standalone: false,
  templateUrl: './detector-selector.component.html',
  styleUrl: './detector-selector.component.scss'
})
export class DetectorSelectorComponent extends BaseComponent implements OnInit{
  @Input() projectId?:string;
  @Input() detector?:Detector;
  @Input() class:string='';
  @Input() enableCreate: boolean = false;

  search: string = '';
  skip:number = 0;
  limit:number = 10;
  detectors: Detector[] = [];
  total:number = 0;

  ngOnInit(): void {
      this.load();
  }

  select(value:Detector){
    this.detector = value;
    this.ctx.closeModal(this.detector);
  }

  onSearchChange(value:string){
    this.skip = 0;
    this.search = value;
    this.load();
  }

  create(){

  }

  dismiss(){
    this.ctx.closeModal(undefined);
  }

  load(){
    if (!this.projectId) return;
    this.setError(undefined);
    this.setLoading(this.ctx.translate.instant("workspace.detector.loadings"));
    this.ctx.api.detector.detectorList(this.projectId,this.skip,this.limit,this.search).subscribe({
      next: (result)=>{
        this.total = result.total;
        this.detectors = result.detectors;
        this.setLoading(undefined);
      },
      error: (result)=>{
        this.setLoading(undefined);
        this.setError(result.error.detail);
      }
    })
  }

}
