import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Project } from '@api/index';
import { BIconType, FAIconType } from '@constants/icons';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-project-list',
  standalone: false,
  templateUrl: './project-list.component.html',
  styleUrl: './project-list.component.scss',
})
export class ProjectListComponent implements OnInit {
  BIconType = BIconType;
  skip:number = 0;
  limit:number = 10;
  search:string = '';
  total:number = 0;
  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);
  projects: Project[] = [];

  FAIconType = FAIconType;

  constructor(private ctx:ContextService,private router:Router){}

  ngOnInit(): void {
      this.load();
  }

  onChangeSearch(value:string){
    this.search = value;
    this.skip = 0;
    this.load();
  }

  load(){
    this.loading.next(this.ctx.translate.instant("workspace.project.loadings"));
    this.error.next(undefined);
    this.ctx.api.workspace.workspaceProjectList(this.skip,this.limit,this.search).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.total = result.total;
        this.projects = result.projects;
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }

  records(project:Project){
    console.log('Going to: '+'/record/list/'+project._id);
    this.router.navigateByUrl('/record/list/'+project._id);
  }

  detectors(project:Project){
    this.router.navigateByUrl('/detector/list/'+project._id);
  }

  create(){
    this.router.navigateByUrl('/project/new');
  }

  edit(project:Project){
    this.router.navigateByUrl('/project/edit/'+project._id);
  }


}
