import { Component, Input, OnInit } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';
import { Record } from '@api/index';
@Component({
  selector: 'app-auto-card',
  standalone: false,
  templateUrl: './auto-card.component.html',
  styleUrl: './auto-card.component.scss'
})
export class AutoCardComponent extends BaseComponent implements OnInit{

  @Input() record!:Record;
  script: string = '';
  declarative: boolean = false;
  synthetic: boolean = false;
  editorOptions = { language: 'javascript', automaticLayout: true };


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

        this.log.warn(result.error.detail);
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }

  toggleDeclarative() {
    this.declarative = !this.declarative;
    this.generate();
  }

  toggleSynthetic() {
    this.synthetic = !this.synthetic;
    this.generate();
  }

  execute() {
    if (this.script != '') {
      this.ctx.api.player
        .playerRunRawScript({ script: this.script })
        .subscribe({
          next: (result) => {},
          error: (result) => {
            this.log.error(result.error.detail);
          },
        });
    }
  }
}
