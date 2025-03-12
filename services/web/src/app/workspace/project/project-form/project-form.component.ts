import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Project } from '@api/index';
import { FAIconType } from '@constants/icons';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-project-form',
  standalone: false,
  templateUrl: './project-form.component.html',
  styleUrl: './project-form.component.scss'
})
export class ProjectFormComponent implements OnInit{
  @Input() id?:string;
  FAIconType = FAIconType;
  valid = new BehaviorSubject<boolean>(false);
  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);
  name:string = '';
  description:string|undefined = '';

  constructor(private ctx:ContextService,private router:Router,route:ActivatedRoute){
    this.id = route.snapshot.paramMap.get('id') || undefined;
  }

  ngOnInit(): void {
      this.load();
  }

  validate(){
    if (this.name.trim()==''){
      this.valid.next(false);
      return;
    }

    this.valid.next(true);
  }

  cancel(){
    this.router.navigateByUrl('project/list');
  }

  onNameChange(value:string){
    this.name = value;
    this.validate();
  }

  onDescriptionChange(value:string){
    this.description = value;
    this.validate();
  }

  load(){
    if (!this.id) return;
    this.loading.next(this.ctx.translate.instant("workspace.project.loadings"));
    this.error.next(undefined);
    this.ctx.api.project.projectLoad(this.id).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.name = result.name;
        this.description = result.description;
        this.validate();
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }

  save(){
    if (!this.id){
      this.create();
    }else{
      this.update();
    }

  }

  create(){
    this.loading.next(this.ctx.translate.instant("workspace.project.saving"));
    this.error.next(undefined);
    this.ctx.api.project.projectCreate(this.name,this.description).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.name = result.name;
        this.description = result.description;
        this.router.navigateByUrl('/project/list');
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }

  remove(){
    if (!this.id) return;
    this.loading.next(this.ctx.translate.instant("workspace.project.removing"));
    this.error.next(undefined);
    this.ctx.api.project.projectDelete(this.id).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.router.navigateByUrl('/project/list');
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }

  update(){
    if (!this.id) return;
    this.loading.next(this.ctx.translate.instant("workspace.project.saving"));
    this.error.next(undefined);
    this.ctx.api.project.projectUpdate(this.id,this.name,this.description).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.name = result.name;
        this.description = result.description;
        this.router.navigateByUrl('/project/list');
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }
}
