import { Component, Input, OnDestroy, OnInit } from '@angular/core';
import { PlayerStepSession } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { filter } from 'rxjs';

@Component({
  selector: 'app-player-raw-execution-modal',
  standalone: false,
  templateUrl: './player-raw-execution-modal.component.html',
  styleUrl: './player-raw-execution-modal.component.scss'
})
export class PlayerRawExecutionModalComponent extends BaseComponent implements OnInit, OnDestroy {
  @Input() execution!:string;
  messages: PlayerStepSession[] = [];

  dismiss(){
    this.ctx.dismissModal();
  }

   ngOnInit(): void {
      let filtered = this.ctx.ws.messages$.pipe(
        filter(
          (msg) =>
            msg.type == 'player.step.session' &&
            msg.execution == this.execution
        )
      );
      this.subs.add(
        filtered.subscribe({
          next: (result) => {
            let res = result as PlayerStepSession;
            this.messages.push(res);
          },
        })
      );
    }

    ngOnDestroy(): void {
      this.subs.unsubscribe();
    }

    normalizeProgress(step: PlayerStepSession):number {
      return Math.round(
        (step.progress / step.total) * 100);
    }
}
