import { Component, Input, OnInit } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';
import {Record} from '@api/index';

@Component({
  selector: 'app-record-script-preview',
  standalone: false,
  templateUrl: './record-script-preview.component.html',
  styleUrl: './record-script-preview.component.scss'
})
export class RecordScriptPreviewComponent extends BaseComponent implements OnInit{
  @Input() record!: Record;
  script: string = '';
  declarative: boolean = false;
  synthetic: boolean = false;

  ngOnInit(): void {
      this.generate();
  }

  generate(){
    if (!this.record._id) return;
      this.ctx.api.player.playerGenerateScript(this.record._id,this.declarative,this.synthetic).subscribe({
        next: (result)=>{
          this.script = result;
        },
        error: (result)=>{
          this.log.error(result.error.detail);
        }
      })
  }

  dismiss(){
    this.ctx.dismissModal();

  }

  toggleDeclarative(){
    this.declarative = !this.declarative;
    this.generate();
  }

  toggleSynthetic(){
    this.synthetic = !this.synthetic;
    this.generate();
  }
}
