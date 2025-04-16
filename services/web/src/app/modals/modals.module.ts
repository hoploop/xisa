import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProjectFormModalComponent } from './project-form-modal/project-form-modal.component';
import { UtilsModule } from '@utils/utils.module';
import { FormsModule } from '@angular/forms';
import { TranslateModule } from '@ngx-translate/core';
import { DetectorFormModalComponent } from './detector-form-modal/detector-form-modal.component';
import { DetectorLabelSelectModalComponent } from './detector-label-select-modal/detector-label-select-modal.component';
import { PipesModule } from '@pipes/pipes.module';
import { DetectorLearnModalComponent } from './detector-learn-modal/detector-learn-modal.component';
import { DetectorSelectorModalComponent } from './detector-selector-modal/detector-selector-modal.component';
import { DetectorSettingsModalComponent } from './detector-settings-modal/detector-settings-modal.component';
import { DetectorSuggestionListModalComponent } from './detector-suggestion-list-modal/detector-suggestion-list-modal.component';
import { CardsModule } from '@cards/cards.module';
import { DetectorTextSettingsModalComponent } from './detector-text-settings-modal/detector-text-settings-modal.component';
import { RecordActionModalComponent } from './record-action-modal/record-action-modal.component';
import { DetectorObjectModalComponent } from './detector-object-modal/detector-object-modal.component';
import { DetectorTextModalComponent } from './detector-text-modal/detector-text-modal.component';
import { RecordEventModalComponent } from './record-event-modal/record-event-modal.component';
import { AutoSuggestionModalComponent } from './auto-suggestion-modal/auto-suggestion-modal.component';
import { TrainObjectModalComponent } from './train-object-modal/train-object-modal.component';
import { RecordControllerModalComponent } from './record-controller-modal/record-controller-modal.component';
import { RecordFormModalComponent } from './record-form-modal/record-form-modal.component';
import { RecordFrameSelectorModalComponent } from './record-frame-selector-modal/record-frame-selector-modal.component';
import { PlayerScriptPreviewModalComponent } from './player-script-preview-modal/player-script-preview-modal.component';
import { RecordVideoModalComponent } from './record-video-modal/record-video-modal.component';
import { MonacoEditorModule } from 'ngx-monaco-editor-v2';
import { AuthCheckModalComponent } from './auth-check-modal/auth-check-modal.component';
import { AuthLoginModalComponent } from './auth-login-modal/auth-login-modal.component';
import { AuthLogoutModalComponent } from './auth-logout-modal/auth-logout-modal.component';
import { AuthRegisterModalComponent } from './auth-register-modal/auth-register-modal.component';
import { AuthUnregisterModalComponent } from './auth-unregister-modal/auth-unregister-modal.component';

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
  ],
  imports: [
    CommonModule,
    UtilsModule,
    FormsModule,
    TranslateModule,
    PipesModule,
    MonacoEditorModule,
    CardsModule
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
  ],
})
export class ModalsModule {}
