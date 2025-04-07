import { Component, Input } from '@angular/core';
import { Detector, Project } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-detector-form',
  standalone: false,
  templateUrl: './detector-form.component.html',
  styleUrl: './detector-form.component.scss'
})
export class DetectorFormComponent extends BaseComponent {
  @Input() project!: Project;
  @Input() detector!: Detector;
  @Input() origin?:Detector;
  valid = new BehaviorSubject<boolean>(false);


  dismiss(){
    this.ctx.dismissModal();
  }


  ngOnInit(): void {

  }

  validate(){
    if (this.detector.name.trim()==''){
      this.valid.next(false);
      return;
    }

    this.valid.next(true);
  }

  cancel(){
    this.ctx.dismissModal();
  }

  onNameChange(value:string){
    this.detector.name = value;
    this.validate();
  }

  onDescriptionChange(value:string){
    this.detector.description = value;
    this.validate();
  }

  save(){
    if (!this.detector._id){
      this.create();
    }else{
      this.update();
    }

  }

  create(){
    if (!this.project) return;
    if (!this.project._id) return;
    this.log.info("Creating detector");
    this.loading.next(this.ctx.translate.instant("workspace.detector.saving"));
    this.error.next(undefined);

    this.log.debug('Checking if origin is specified')
    let originId = undefined;
    if (this.origin && this.origin._id){
      originId = this.origin._id;
    }
    this.ctx.api.detector.detectorCreate(this.project._id,this.detector.name,originId,this.detector.description|| '').subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.detector.name = result.name;
        this.detector.description = result.description || '';
        this.ctx.closeModal(this.detector);
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }

  remove(){
    if (!this.detector._id) return;
    this.loading.next(this.ctx.translate.instant("workspace.detector.removing"));
    this.error.next(undefined);
    this.ctx.api.detector.detectorRemove(this.detector._id).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.ctx.closeModal(undefined);
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }

  update(){
    if (!this.detector._id) return;
    this.loading.next(this.ctx.translate.instant("workspace.detector.saving"));
    this.error.next(undefined);
    this.ctx.api.detector.detectorUpdate(this.detector._id,this.detector.name,this.detector.description|| '').subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.ctx.closeModal(this.detector);
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }
}
