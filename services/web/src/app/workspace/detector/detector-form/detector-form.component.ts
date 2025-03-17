import { Component, Input } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FAIconType } from '@constants/icons';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-detector-form',
  standalone: false,
  templateUrl: './detector-form.component.html',
  styleUrl: './detector-form.component.scss'
})
export class DetectorFormComponent {
  FAIconType = FAIconType;
  valid = new BehaviorSubject<boolean>(false);
  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);
  name:string = '';
  description:string|undefined = '';
  projectId?:string;
  id?:string;

  constructor(private ctx:ContextService,private router:Router,route:ActivatedRoute){
    this.projectId = route.snapshot.paramMap.get('project_id') || undefined;
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
    this.router.navigateByUrl('/detector/list/'+this.projectId);
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
    this.loading.next(this.ctx.translate.instant("workspace.detector.loading"));
    this.error.next(undefined);
    this.ctx.api.detector.detectorLoadDetectorid(this.id).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.name = result.name;
        this.description = result.description || '';
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
    if (!this.projectId) return;
    this.loading.next(this.ctx.translate.instant("workspace.detector.saving"));
    this.error.next(undefined);
    this.ctx.api.detector.detectorCreateProjectid(this.projectId,this.name,undefined,this.description).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.name = result.name;
        this.description = result.description || '';
        this.router.navigateByUrl('/detector/list/'+this.projectId);
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }

  remove(){
    if (!this.id) return;
    if (!this.projectId) return;
    this.loading.next(this.ctx.translate.instant("workspace.detector.removing"));
    this.error.next(undefined);
    this.ctx.api.detector.detectorRemove(this.id).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.router.navigateByUrl('/detector/list/'+this.projectId);
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }

  update(){
    if (!this.id) return;
    this.loading.next(this.ctx.translate.instant("workspace.detector.saving"));
    this.error.next(undefined);
    this.ctx.api.detector.detectorUpdate(this.id,this.name,this.description|| '').subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.name = result.name;
        this.description = result.description || '';
        this.router.navigateByUrl('/detector/list/'+this.projectId);
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }
}
