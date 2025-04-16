import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProjectListCardComponent } from './project-list-card/project-list-card.component';
import { UtilsModule } from '@utils/utils.module';
import { TranslateModule } from '@ngx-translate/core';
import { ProjectDetailCardComponent } from './project-detail-card/project-detail-card.component';
import { PipesModule } from '@pipes/pipes.module';
import { DetectorImageListCardComponent } from './detector-image-list-card/detector-image-list-card.component';
import { MomentModule } from 'ngx-moment';
import { DetectorLabelSuggestionCardComponent } from './detector-label-suggestion-card/detector-label-suggestion-card.component';
import { DetectorListCardComponent } from './detector-list-card/detector-list-card.component';
import { DetectorObjectsSummaryCardComponent } from './detector-objects-summary-card/detector-objects-summary-card.component';
import { DetectorSuggestionCardComponent } from './detector-suggestion-card/detector-suggestion-card.component';
import { DetectorTextsSummaryCardComponent } from './detector-texts-summary-card/detector-texts-summary-card.component';
import { DetectorTrainSuggestionCardComponent } from './detector-train-suggestion-card/detector-train-suggestion-card.component';
import { RecordEventCardComponent } from './record-event-card/record-event-card.component';
import { RecordListCardComponent } from './record-list-card/record-list-card.component';
import { RecordFrameScrollerCardComponent } from './record-frame-scroller-card/record-frame-scroller-card.component';
import { RecordStudioCardComponent } from './record-studio-card/record-studio-card.component';
import { RecordFrameCardComponent } from './record-frame-card/record-frame-card.component';
import { FormsModule } from '@angular/forms';
import { MenuCardComponent } from './menu-card/menu-card.component';



@NgModule({
  declarations: [
    ProjectListCardComponent,
    ProjectDetailCardComponent,
    DetectorImageListCardComponent,
    DetectorLabelSuggestionCardComponent,
    DetectorListCardComponent,
    DetectorObjectsSummaryCardComponent,
    DetectorSuggestionCardComponent,
    DetectorTextsSummaryCardComponent,
    DetectorTrainSuggestionCardComponent,
    RecordEventCardComponent,
    RecordListCardComponent,
    RecordFrameScrollerCardComponent,
    RecordStudioCardComponent,
    RecordFrameCardComponent,
    MenuCardComponent
  ],
  imports: [
    CommonModule,
    UtilsModule,
    TranslateModule,
    PipesModule,
    MomentModule,
    FormsModule

  ],
  exports: [
    ProjectListCardComponent,
    ProjectDetailCardComponent,
    DetectorImageListCardComponent,
    DetectorLabelSuggestionCardComponent,
    DetectorListCardComponent,
    DetectorObjectsSummaryCardComponent,
    DetectorSuggestionCardComponent,
    DetectorTextsSummaryCardComponent,
    DetectorTrainSuggestionCardComponent,
    RecordEventCardComponent,
    RecordListCardComponent,
    RecordFrameScrollerCardComponent,
    RecordStudioCardComponent,
    RecordFrameCardComponent,
    MenuCardComponent
  ]
})
export class CardsModule { }
