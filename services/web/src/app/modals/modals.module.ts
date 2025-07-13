import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProjectFormModalComponent } from './project-form-modal/project-form-modal.component';
import { UtilsModule } from '@utils/utils.module';
import { FormsModule } from '@angular/forms';
import { TranslateModule } from '@ngx-translate/core';
import { DetectorFormModalComponent } from './detector/detector-form-modal/detector-form-modal.component';
import { DetectorLabelSelectModalComponent } from './detector/detector-label-select-modal/detector-label-select-modal.component';
import { PipesModule } from '@pipes/pipes.module';
import { DetectorLearnModalComponent } from './detector/detector-learn-modal/detector-learn-modal.component';
import { DetectorSelectorModalComponent } from './detector/detector-selector-modal/detector-selector-modal.component';
import { DetectorSettingsModalComponent } from './detector/detector-settings-modal/detector-settings-modal.component';
import { DetectorSuggestionListModalComponent } from './detector/detector-suggestion-list-modal/detector-suggestion-list-modal.component';
import { CardsModule } from '@cards/cards.module';
import { DetectorTextSettingsModalComponent } from './detector/detector-text-settings-modal/detector-text-settings-modal.component';
import { RecordActionModalComponent } from './record/record-action-modal/record-action-modal.component';
import { DetectorObjectModalComponent } from './detector/detector-object-modal/detector-object-modal.component';
import { DetectorTextModalComponent } from './detector/detector-text-modal/detector-text-modal.component';
import { RecordEventModalComponent } from './record/record-event-modal/record-event-modal.component';
import { AutoSuggestionModalComponent } from './auth/auto-suggestion-modal/auto-suggestion-modal.component';
import { TrainObjectModalComponent } from './train-object-modal/train-object-modal.component';
import { RecordControllerModalComponent } from './record/record-controller-modal/record-controller-modal.component';
import { RecordFormModalComponent } from './record/record-form-modal/record-form-modal.component';
import { RecordFrameSelectorModalComponent } from './record/record-frame-selector-modal/record-frame-selector-modal.component';
import { PlayerScriptPreviewModalComponent } from './player/player-script-preview-modal/player-script-preview-modal.component';
import { RecordVideoModalComponent } from './record/record-video-modal/record-video-modal.component';
import { AuthCheckModalComponent } from './auth/auth-check-modal/auth-check-modal.component';
import { AuthLoginModalComponent } from './auth/auth-login-modal/auth-login-modal.component';
import { AuthLogoutModalComponent } from './auth/auth-logout-modal/auth-logout-modal.component';
import { AuthRegisterModalComponent } from './auth/auth-register-modal/auth-register-modal.component';
import { AuthUnregisterModalComponent } from './auth/auth-unregister-modal/auth-unregister-modal.component';
import { PlayerRawExecutionModalComponent } from './player/player-raw-execution-modal/player-raw-execution-modal.component';
import { OperatorChatModalComponent } from './operator-chat-modal/operator-chat-modal.component';
import { AceModule } from 'ngx-ace-wrapper';
import { DetectorTrainLabModalComponent } from './detector/detector-train-lab-modal/detector-train-lab-modal.component';
import { DetectorContourModalComponent } from './detector/detector-contour-modal/detector-contour-modal.component';

@NgModule({
  declarations: [
    ProjectFormModalComponent,
    DetectorFormModalComponent,
    DetectorLabelSelectModalComponent,
    DetectorLearnModalComponent,
    DetectorSelectorModalComponent,
    DetectorSettingsModalComponent,
    DetectorSuggestionListModalComponent,
    DetectorTextSettingsModalComponent,
    RecordActionModalComponent,
    DetectorObjectModalComponent,
    DetectorTextModalComponent,
    RecordEventModalComponent,
    AutoSuggestionModalComponent,
    TrainObjectModalComponent,
    RecordControllerModalComponent,
    RecordFormModalComponent,
    RecordFrameSelectorModalComponent,
    PlayerScriptPreviewModalComponent,
    RecordVideoModalComponent,
    AuthCheckModalComponent,
    AuthLoginModalComponent,
    AuthLogoutModalComponent,
    AuthRegisterModalComponent,
    AuthUnregisterModalComponent,
    PlayerRawExecutionModalComponent,
    OperatorChatModalComponent,
    DetectorTrainLabModalComponent,
    DetectorContourModalComponent,
  ],
  imports: [
    CommonModule,
    UtilsModule,
    FormsModule,
    TranslateModule,
    PipesModule,
    CardsModule,
    AceModule

  ],
  exports: [
    ProjectFormModalComponent,
    DetectorFormModalComponent,
    DetectorLabelSelectModalComponent,
    DetectorLearnModalComponent,
    DetectorSelectorModalComponent,
    DetectorSettingsModalComponent,
    DetectorSuggestionListModalComponent,
    DetectorTextSettingsModalComponent,
    RecordActionModalComponent,
    DetectorObjectModalComponent,
    DetectorTextModalComponent,
    RecordEventModalComponent,
    AutoSuggestionModalComponent,
    TrainObjectModalComponent,
    RecordControllerModalComponent,
    RecordFormModalComponent,
    RecordFrameSelectorModalComponent,
    PlayerScriptPreviewModalComponent,
    RecordVideoModalComponent,
    AuthCheckModalComponent,
    AuthLoginModalComponent,
    AuthLogoutModalComponent,
    AuthRegisterModalComponent,
    AuthUnregisterModalComponent,
    PlayerRawExecutionModalComponent,
    OperatorChatModalComponent,
    DetectorTrainLabModalComponent,
    DetectorContourModalComponent
  ],
})
export class ModalsModule {}
