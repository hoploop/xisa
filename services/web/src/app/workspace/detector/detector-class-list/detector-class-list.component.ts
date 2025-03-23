import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { DetectorClass } from '@api/index';
import { ContextService } from '@services/context.service';
import { BaseComponent } from '@utils/base/base.component';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-detector-class-list',
  standalone: false,
  templateUrl: './detector-class-list.component.html',
  styleUrl: './detector-class-list.component.scss'
})
export class DetectorClassListComponent extends BaseComponent implements OnInit {
  @Input() detectorId?: string;
  classes: DetectorClass[] = []
  @Input() enableCreate:boolean = true;
  @Input() selected: DetectorClass[] = [];
  @Output() selectedChange = new EventEmitter<DetectorClass[]>();
  total: number = 0;
  skip:number = 0;
  limit:number = 10;
  search:string = '';

  newClass: string = '';
  newClassValid: boolean = false;



  ngOnInit(): void {
    setTimeout(()=>{
      this.load();
    });

  }

  onNewClassChange(value:string){
    this.newClass = value;
    if (this.newClass.trim()!=''){
      this.newClassValid = true;
    }
  else{
      this.newClassValid=false;
  }
  }

  addNewClass(){
    if (!this.detectorId) return;
    this.loading.next(this.ctx.translate.instant("workspace.detector.class.adding"));
    this.error.next(undefined);
    this.ctx.api.detector.detectorClassAddDetectorid(this.detectorId,this.newClass).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.load();
      },
      error: (result)=>{
        this.error.next(result.error.detail);
        this.loading.next(undefined);
      }
    })
  }

  onChangeSearch(value:string){
    this.skip = 0;
    this.search = value;
    this.load();
  }

  onSkipChange(value:number){
    this.skip = value;
    this.load();
  }

  onLimitChange(value:number){
    this.limit = value;
    this.load();
  }

  onSearchChange(value:string){
    this.skip = 0;
    this.search = value;
    this.load();
  }

  submit(){
    this.ctx.closeModal(this.selected);
  }

  select(clazz: DetectorClass){
    let found = this.selected.findIndex(item=> item._id === clazz._id);
    if (found!=-1){
      this.selected.splice(found,1);
    }else{
      this.selected.push(clazz);
    }
    this.selectedChange.next(this.selected);
    this.load();

  }

  load(){
    if (!this.detectorId) return;
    this.loading.next(this.ctx.translate.instant("workspace.detector.class.loadings"));
    this.error.next(undefined);
    this.ctx.api.detector.detectorClassListDetectorid(this.detectorId,this.skip,this.limit,this.search).subscribe({
      next: (result)=>{
        this.total = result.total;
        this.classes = result.classes;
        this.loading.next(undefined);
      },
      error: (result)=>{
        this.error.next(result.error.detail);
        this.loading.next(undefined);
      }
    })
  }

  dismiss(){
    this.ctx.closeModal(undefined);
  }
}
