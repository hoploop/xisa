import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ContourSettingsComponent } from './contour-settings/contour-settings.component';
import { DetectorFormModalComponent } from '@detect/detector-form-modal/detector-form-modal.component';
import { DetectorLabelSelectModalComponent } from './detector-label-select-modal/detector-label-select-modal.component';
import { DetectorLearnModalComponent } from './detector-learn-modal/detector-learn-modal.component';
import { DetectorSelectorModalComponent } from './detector-selector-modal/detector-selector-modal.component';
import { DetectorSettingsModalComponent } from './detector-settings-modal/detector-settings-modal.component';
import { DetectorSuggestionListModalComponent } from './detector-suggestion-list-modal/detector-suggestion-list-modal.component';
import { DetectorTextSettingsModalComponent } from './detector-text-settings-modal/detector-text-settings-modal.component';
import { DetectorTrainLabModalComponent } from './detector-train-lab-modal/detector-train-lab-modal.component';
import { DetectorContourModalComponent } from './detector-contour-modal/detector-contour-modal.component';
import { DetectorObjectModalComponent } from './detector-object-modal/detector-object-modal.component';
import { DetectorTextModalComponent } from './detector-text-modal/detector-text-modal.component';
import { DetectorLabelSuggestionCardComponent } from './detector-label-suggestion-card/detector-label-suggestion-card.component';
import { DetectorListCardComponent } from './detector-list-card/detector-list-card.component';
import { DetectorObjectsSummaryCardComponent } from './detector-objects-summary-card/detector-objects-summary-card.component';
import { DetectorSuggestionCardComponent } from './detector-suggestion-card/detector-suggestion-card.component';
import { DetectorTextsSummaryCardComponent } from './detector-texts-summary-card/detector-texts-summary-card.component';
import { DetectorTrainSuggestionCardComponent } from './detector-train-suggestion-card/detector-train-suggestion-card.component';
import { DetectorImageListCardComponent } from './detector-image-list-card/detector-image-list-card.component';
import { DetectorImageCardComponent } from './detector-image-card/detector-image-card.component';
import { DetectorTrainSessionListCardComponent } from './detector-train-session-list-card/detector-train-session-list-card.component';
import { DetectorImageLabelCountPipe } from './detector-image-label-count.pipe';
import { DetectorClassFilterPipe } from './detector-class-filter.pipe';
import { DetectorTrainCountPipe } from './detector-train-count.pipe';
import { DetectorImageCountPipe } from './detector-image-count.pipe';
import { DetectorClassCountPipe } from './detector-class-count.pipe';
import { DetectorLabelRemovablePipe } from './detector-label-removable.pipe';
import { DetectorTrainRunningPipe } from './detector-train-running.pipe';
import { DetectorTrainSessionCountPipe } from './detector-train-session-count.pipe';
import { DetectorImageLabelsPipe } from './detector-image-labels.pipe';
import { DetectorLabelLoadPipe } from './detector-label-load.pipe';
import { DetectorTrainSessionListPageComponent } from './detector-train-session-list-page/detector-train-session-list-page.component';
import { DetectorImageListPageComponent } from './detector-image-list-page/detector-image-list-page.component';
import { DetectorListPageComponent } from './detector-list-page/detector-list-page.component';
import { DetectorPageComponent } from './detector-page/detector-page.component';
import { UtilsModule } from '@utils/utils.module';
import { TranslateModule } from '@ngx-translate/core';
import { MomentModule } from 'ngx-moment';
import { FormsModule } from '@angular/forms';
import { RecordModule } from '@record/record.module';
import { DetectorCardComponent } from './detector-card/detector-card.component';

@NgModule({
  declarations: [
    ContourSettingsComponent,
    DetectorFormModalComponent,
    DetectorLabelSelectModalComponent,
    DetectorLearnModalComponent,
    DetectorSelectorModalComponent,
    DetectorSettingsModalComponent,
    DetectorSuggestionListModalComponent,
    DetectorTextSettingsModalComponent,
    DetectorTrainLabModalComponent,
    DetectorContourModalComponent,
    DetectorObjectModalComponent,
    DetectorTextModalComponent,
    DetectorImageListCardComponent,
    DetectorLabelSuggestionCardComponent,
    DetectorListCardComponent,
    DetectorObjectsSummaryCardComponent,
    DetectorSuggestionCardComponent,
    DetectorTextsSummaryCardComponent,
    DetectorTrainSuggestionCardComponent,
    DetectorImageCardComponent,
    DetectorTrainSessionListCardComponent,
    DetectorImageLabelCountPipe,
    DetectorClassFilterPipe,
    DetectorTrainCountPipe,
    DetectorImageCountPipe,
    DetectorClassCountPipe,
    DetectorLabelRemovablePipe,
    DetectorTrainRunningPipe,
    DetectorTrainSessionCountPipe,
    DetectorImageLabelsPipe,
    DetectorLabelLoadPipe,
    DetectorTrainSessionListPageComponent,
    DetectorImageListPageComponent,
    DetectorListPageComponent,
    DetectorPageComponent,
    DetectorCardComponent,
  ],
  imports: [
    CommonModule,
    UtilsModule,
    TranslateModule,
    FormsModule,
    MomentModule,
    RecordModule,
  ],
  exports: [
    ContourSettingsComponent,
    DetectorFormModalComponent,
    DetectorLabelSelectModalComponent,
    DetectorLearnModalComponent,
    DetectorSelectorModalComponent,
    DetectorSettingsModalComponent,
    DetectorSuggestionListModalComponent,
    DetectorTextSettingsModalComponent,
    DetectorTrainLabModalComponent,
    DetectorContourModalComponent,
    DetectorObjectModalComponent,
    DetectorTextModalComponent,
    DetectorImageListCardComponent,
    DetectorLabelSuggestionCardComponent,
    DetectorListCardComponent,
    DetectorObjectsSummaryCardComponent,
    DetectorSuggestionCardComponent,
    DetectorTextsSummaryCardComponent,
    DetectorTrainSuggestionCardComponent,
    DetectorImageCardComponent,
    DetectorTrainSessionListCardComponent,
    DetectorCardComponent,
    DetectorImageLabelCountPipe,
    DetectorClassFilterPipe,
    DetectorTrainCountPipe,
    DetectorImageCountPipe,
    DetectorClassCountPipe,
    DetectorLabelRemovablePipe,
    DetectorTrainRunningPipe,
    DetectorTrainSessionCountPipe,
    DetectorImageLabelsPipe,
    DetectorLabelLoadPipe,
    DetectorTrainSessionListPageComponent,
    DetectorImageListPageComponent,
    DetectorListPageComponent,
    DetectorPageComponent,
  ],
})
export class DetectModule {}
