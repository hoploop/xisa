import { Component, Input, OnInit } from '@angular/core';
import { Project } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-project-form',
  standalone: false,
  templateUrl: './project-form.component.html',
  styleUrl: './project-form.component.scss'
})
export class ProjectFormComponent extends BaseComponent implements OnInit{
  @Input() project!:Project;
  valid = new BehaviorSubject<boolean>(false);

  dismiss(){
    this.ctx.dismissModal();
  }

  ngOnInit(): void {
      this.validate()
  }

  validate(){
    if (this.project.name.trim()==''){
      this.valid.next(false);
      return;
    }

    this.valid.next(true);
  }

  cancel(){
    this.ctx.dismissModal();
  }

  onNameChange(value:string){
    this.project.name = value;
    this.validate();
  }

  onDescriptionChange(value:string){
    this.project.description = value;
    this.validate();
  }

  save(){
    if (!this.project._id){
      this.create();
    }else{
      this.update();
    }

  }

  create(){
    this.loading.next(this.ctx.translate.instant("project.saving"));
    this.error.next(undefined);
    this.ctx.api.project.projectCreate(this.project.name,this.project.description).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.project.name = result.name;
        this.project.description = result.description;
        this.ctx.closeModal(this.project);
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }

  remove(){
    if (!this.project._id) return;
    this.loading.next(this.ctx.translate.instant("project.removing"));
    this.error.next(undefined);
    this.ctx.api.project.projectDelete(this.project._id).subscribe({
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
    if (!this.project._id) return;
    this.loading.next(this.ctx.translate.instant("project.saving"));
    this.error.next(undefined);
    this.ctx.api.project.projectUpdate(this.project._id,this.project.name,this.project.description).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.ctx.closeModal(this.project);
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }
}
