import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UtilsModule } from '@utils/utils.module';
import { ProjectFormComponent } from './project/project-form/project-form.component';
import { ProjectListComponent } from './project/project-list/project-list.component';
import { FormsModule } from '@angular/forms';
import { TranslateModule } from '@ngx-translate/core';
import { RecordListComponent } from './record/record-list/record-list.component';
import { RecordControllerComponent } from './record/record-controller/record-controller.component';
import { MomentModule } from 'ngx-moment';
import { RecordEventsCountPipe } from './record/record-events-count.pipe';
import { RecordDurationPipe } from './record/record-duration.pipe';
import { RecordFramesCountPipe } from './record/record-frames-count.pipe';
import { RecordSizePipe } from './record/record-size.pipe';
import { ProjectRecordCountPipe } from './project/project-record-count.pipe';
import { RecordFormComponent } from './record/record-form/record-form.component';
import { DetectorListComponent } from './detector/detector-list/detector-list.component';
import { ProjectDetectorCountPipe } from './project/project-detector-count.pipe';
import { DetectorFormComponent } from './detector/detector-form/detector-form.component';
import { DetectorImageCountPipe } from './detector/detector-image-count.pipe';
import { DetectorClassCountPipe } from './detector/detector-class-count.pipe';
import { DetectorLearnComponent } from './detector/detector-learn/detector-learn.component';
import { DetectorImageListComponent } from './detector/detector-image-list/detector-image-list.component';
import { RecordStudioComponent } from './record/record-studio/record-studio.component';
import { RecordVideoPipe } from './record/record-video.pipe';
import { RecordFramePipe } from './record/record-frame.pipe';
import { RecordEventPickerComponent } from './record/record-event-picker/record-event-picker.component';
import { RecordFrameComponent } from './record/record-frame/record-frame.component';
import { DetectorSelectorComponent } from './detector/detector-selector/detector-selector.component';
import { RecordVideoComponent } from './record/record-video/record-video.component';
import { DetectorClassFilterPipe } from './detector/detector-class-filter.pipe';
import { TrainModule } from "../train/train.module";
import { DetectorSuggestionComponent } from './detector/detector-suggestion/detector-suggestion.component';
import { DetectorLabelSelectComponent } from './detector/detector-label-select/detector-label-select.component';
import { DetectorLabelSuggestionComponent } from './detector/detector-label-suggestion/detector-label-suggestion.component';
import { DetectorLabelTrainComponent } from './detector/detector-label-train/detector-label-train.component';
import { DetectorObjectsSummaryComponent } from './detector/detector-objects-summary/detector-objects-summary.component';
import { DetectorTextsSummaryComponent } from './detector/detector-texts-summary/detector-texts-summary.component';
import { DetectorSummaryComponent } from './detector/detector-summary/detector-summary.component';
import { TemplatesModule } from '@templates/templates.module';
import { RecordFrameSelectorComponent } from './record/record-frame-selector/record-frame-selector.component';
import { RecordSuggestionsComponent } from './record/record-suggestions/record-suggestions.component';



@NgModule({
  declarations: [
    ProjectFormComponent,
    ProjectListComponent,
    RecordListComponent,
    RecordControllerComponent,
    RecordEventsCountPipe,
    RecordDurationPipe,
    RecordFramesCountPipe,
    RecordSizePipe,
    ProjectRecordCountPipe,
    RecordFormComponent,
    DetectorListComponent,
    ProjectDetectorCountPipe,
    DetectorFormComponent,
    DetectorImageCountPipe,
    DetectorClassCountPipe,
    DetectorLearnComponent,
    DetectorImageListComponent,
    RecordStudioComponent,
    RecordVideoPipe,
    RecordFramePipe,
    RecordEventPickerComponent,
    RecordFrameComponent,
    DetectorSelectorComponent,
    RecordVideoComponent,
    DetectorClassFilterPipe,
    DetectorSuggestionComponent,
    DetectorLabelSelectComponent,
    DetectorLabelSuggestionComponent,
    DetectorLabelTrainComponent,
    DetectorObjectsSummaryComponent,
    DetectorTextsSummaryComponent,
    DetectorSummaryComponent,
    RecordFrameSelectorComponent,
    RecordSuggestionsComponent,
  ],
  imports: [
    CommonModule,
    UtilsModule,
    FormsModule,
    TranslateModule,
    TemplatesModule,
    MomentModule,
    TrainModule
],
  exports: [
    ProjectListComponent,
    ProjectFormComponent,
    RecordListComponent,
    RecordFormComponent,
    RecordControllerComponent,
    DetectorListComponent
  ]
})
export class WorkspaceModule { }
