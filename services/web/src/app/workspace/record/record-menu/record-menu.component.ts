import { Component, OnInit } from '@angular/core';
import { Project } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-menu',
  standalone: false,
  templateUrl: './record-menu.component.html',
  styleUrl: './record-menu.component.scss'
})
export class RecordMenuComponent extends BaseComponent implements OnInit{
  project?: Project;

  ngOnInit(): void {
    let projectId = this.route.snapshot.paramMap.get('project_id');
    if (!projectId) return;
    this.ctx.api.workspace.workspaceProjectLoad(projectId).subscribe({
      next: (result)=>{
        this.project = result;
      }
    })
  }



  projects(){

  }

}
