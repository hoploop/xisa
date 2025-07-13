import { Component, Input, OnInit } from '@angular/core';
import { Record } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-player-script-preview-modal',
  standalone: false,
  templateUrl: './player-script-preview-modal.component.html',
  styleUrl: './player-script-preview-modal.component.scss',
})
export class PlayerScriptPreviewModalComponent
  extends BaseComponent
  implements OnInit
{
  @Input() record!: Record;
  script: string = '';
  declarative: boolean = false;
  synthetic: boolean = false;
  editorOptions = { language: 'javascript', automaticLayout: true };

  ngOnInit(): void {
    this.generate();
  }

  generate() {
    if (!this.record._id) return;
    this.ctx.api.player
      .playerGenerateScript(this.record._id, this.declarative, this.synthetic)
      .subscribe({
        next: (result) => {
          this.script = result;
        },
        error: (result) => {
          this.log.error(result.error.detail);
        },
      });
  }

  dismiss() {
    this.ctx.dismissModal();
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
