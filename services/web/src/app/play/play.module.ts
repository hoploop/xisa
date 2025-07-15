import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PlayerScriptPreviewModalComponent } from './player-script-preview-modal/player-script-preview-modal.component';
import { PlayerRawExecutionModalComponent } from './player-raw-execution-modal/player-raw-execution-modal.component';
import { PlayerCardComponent } from './player-card/player-card.component';
import { PlayerPageComponent } from './player-page/player-page.component';
import { UtilsModule } from '@utils/utils.module';
import { TranslateModule } from '@ngx-translate/core';
import { MomentModule } from 'ngx-moment';
import { FormsModule } from '@angular/forms';
import { AceModule } from 'ngx-ace-wrapper';

@NgModule({
  declarations: [
    PlayerScriptPreviewModalComponent,
    PlayerRawExecutionModalComponent,
    PlayerCardComponent,
    PlayerPageComponent,
  ],
  imports: [
    CommonModule,
    UtilsModule,
    TranslateModule,
    FormsModule,
    MomentModule,
    AceModule
  ],
  exports: [
    PlayerScriptPreviewModalComponent,
    PlayerRawExecutionModalComponent,
    PlayerCardComponent,
    PlayerPageComponent,
  ],
})
export class PlayModule {}
