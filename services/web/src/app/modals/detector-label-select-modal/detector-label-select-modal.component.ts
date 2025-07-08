import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { DetectorLabel } from '@api/index';
import { FAIconType } from '@constants/icons';
import { BaseComponent } from '@utils/base/base.component';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-detector-label-select-modal',
  standalone: false,
  templateUrl: './detector-label-select-modal.component.html',
  styleUrl: './detector-label-select-modal.component.scss',
})
export class DetectorLabelSelectModalComponent
  extends BaseComponent
  implements OnInit
{
  @Input() detectorId?: string;

  @Input() enableCreate: boolean = true;
  @Input() selected: DetectorLabel[] = [];
  @Output() selectedChange = new EventEmitter<DetectorLabel[]>();
  total: number = 0;
  skip: number = 0;
  limit: number = 10;
  search: string = '';
  labels: DetectorLabel[] = [];
  adding = new BehaviorSubject<FAIconType>(FAIconType.search);


  ngOnInit(): void {
    setTimeout(() => {
      this.load();
    });
  }



  addNewLabel() {
    if (!this.detectorId) return;
    if (this.adding.getValue() != FAIconType.plus) return;
    if (this.search.trim()=='') return;
    this.loading.next(this.ctx.translate.instant('detector.class.adding'));
    this.error.next(undefined);
    this.ctx.api.detector
      .detectorLabelAdd(this.detectorId, this.search)
      .subscribe({
        next: (result) => {
          this.loading.next(undefined);
          this.search = '';
          this.adding.next(FAIconType.search);
          this.labels.push(result);
        },
        error: (result) => {
          this.error.next(result.error.detail);
          this.loading.next(undefined);
        },
      });
  }

  removeLabel(value:DetectorLabel){
    if (!value._id) return;
    this.ctx.api.detector.detectorLabelRemove(value._id).subscribe({
      next: (result)=>{
        let foundIndex = this.labels.findIndex(item=> item._id == value._id);
        if (foundIndex!=-1){
          this.labels.splice(foundIndex,1);
        }
      },
      error: (result)=>{}
    })
  }

  onChangeSearch(value: string) {
    this.skip = 0;
    this.search = value;
    this.load();
  }

  onSkipChange(value: number) {
    this.skip = value;
    this.load();
  }

  onLimitChange(value: number) {
    this.limit = value;
    this.load();
  }

  onSearchChange(value: string) {
    this.skip = 0;
    this.search = value;
    this.load();
  }

  submit() {
    this.ctx.closeModal(this.selected);
  }

  remove(){
    this.ctx.closeModal(undefined);
  }

  select(label: DetectorLabel) {
    let found = this.selected.findIndex((item) => item._id === label._id);
    if (found == -1) {
      this.selected.push(label);
      this.selectedChange.next(this.selected);
    }

    found = this.labels.findIndex((item)=> item._id == label._id);
    if (found!=-1){
      this.labels.splice(found,1);
    }
  }

  unselect(label: DetectorLabel) {
    let found = this.selected.findIndex((item) => item._id === label._id);
    if (found != -1) {
      this.selected.splice(found, 1);
      this.selectedChange.next(this.selected);
    }
    found = this.labels.findIndex((item)=> item._id == label._id);
    if (found==-1){
      this.labels.push(label);
    }
  }

  load() {
    if (!this.detectorId) return;
    this.loading.next(this.ctx.translate.instant('detector.class.loadings'));
    this.error.next(undefined);
    let flattenExclude: string[] = [];
    for (let i = 0; i < this.selected.length; i++){
      flattenExclude.push(this.selected[i].name);
    }
    this.ctx.api.detector
      .detectorLabelList(this.detectorId, this.skip, this.limit, this.search,flattenExclude)
      .subscribe({
        next: (result) => {
          this.total = result.total;
          this.labels = result.labels;
          this.loading.next(undefined);
          if (this.total == 0 && this.search.trim() !=''){
            this.adding.next(FAIconType.plus);
          }else{
            this.adding.next(FAIconType.search);
          }
        },
        error: (result) => {
          this.error.next(result.error.detail);
          this.loading.next(undefined);
        },
      });
  }

  dismiss() {
    this.ctx.dismissModal();
  }
}
