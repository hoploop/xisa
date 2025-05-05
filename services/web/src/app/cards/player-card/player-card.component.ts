import { Component, Input, OnInit } from '@angular/core';
import { PlayerRawExecutionModalComponent } from '@modals/player-raw-execution-modal/player-raw-execution-modal.component';
import { BaseComponent } from '@utils/base/base.component';
import { Record } from '@api/index';
import 'brace';
import 'brace/mode/text';
import 'brace/theme/github';

@Component({
  selector: 'app-player-card',
  standalone: false,
  templateUrl: './player-card.component.html',
  styleUrl: './player-card.component.scss'
})
export class PlayerCardComponent extends BaseComponent implements OnInit{

  @Input() record!:Record;
  preview: string = '';
  declarative: boolean = false;
  synthetic: boolean = false;
  editorOptions = { language: 'javascript', automaticLayout: true };
  script?:string;


  ngOnInit(): void {
      this.generate();
      this.load();
  }

  generate(){
    if (!this.record._id) return;
    this.ctx.api.player.playerGenerateScript(this.record._id,this.declarative,this.synthetic).subscribe({
      next: (result)=>{
        this.preview = result;
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

  load(){
    if (!this.record._id) return;
    this.ctx.api.player.playerScriptExist(this.record._id).subscribe({
      next: (result)=>{
        if (result && this.record._id){
          this.ctx.api.player.playerScriptLoad(this.record._id).subscribe({
            next: (resultb)=>{
              this.script = resultb;
              this.log.info(resultb);
            },
            error: (resultb)=>{
              this.log.error(resultb.error.detail);
            }
          })
        }
      },
      error: (result)=>{
        this.log.error(result.error.detail);
      }
    })
  }

  savePreview(){
    if (!this.record._id) return;
    this.ctx.api.player.playerUpdateScript(this.record._id,this.preview).subscribe({
      next: (result)=>{
        this.load();
      },
      error: (result)=>{
        this.log.error(result.error.detail);
      }
    })
  }

  executePreview() {
    if (this.script != '') {
      const execution = this.ctx.newUID;
      this.ctx.openModal(PlayerRawExecutionModalComponent,{execution: execution},{size:'lg',centered:true}).subscribe({
        next: (result)=>{},
        error: (result)=>{}
      })

      this.ctx.api.player
        .playerRunRawScript({ script: this.preview,execution: execution})
        .subscribe({
          next: (result) => {},
          error: (result) => {
            this.log.error(result.error.detail);
          },
        });
    }
  }
}
