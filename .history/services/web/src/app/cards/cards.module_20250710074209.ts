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
import { FormsModule } from '@angular/forms';
import { MenuCardComponent } from './menu-card/menu-card.component';
import { DetectorCardComponent } from './detector-card/detector-card.component';
import { HomeCardComponent } from './home-card/home-card.component';
import { PlayerCardComponent } from './player-card/player-card.component';
import { ProjectCardComponent } from './project-card/project-card.component';
import { RecordCardComponent } from './record-card/record-card.component';
import { TrainerCardComponent } from './trainer-card/trainer-card.component';
import { TrainerLessonCardComponent } from './trainer-lesson-card/trainer-lesson-card.component';
import { TrainerLessonFrameCardComponent } from './trainer-lesson-frame-card/trainer-lesson-frame-card.component';
import { TrainerLessonSuggestionCardComponent } from './trainer-lesson-suggestion-card/trainer-lesson-suggestion-card.component';
import { TrainerLessonEventCardComponent } from './trainer-lesson-event-card/trainer-lesson-event-card.component';
import { TrainerLessonTrainCardComponent } from './trainer-lesson-train-card/trainer-lesson-train-card.component';
import { TrainerLessonActionCardComponent } from './trainer-lesson-action-card/trainer-lesson-action-card.component';
import { AceEditorModule } from 'ngx-ace-editor-wrapper';
import { AceModule } from 'ngx-ace-wrapper';
import { DetectorTrainSessionListCardComponent } from './detector-train-session-list-card/detector-train-session-list-card.component';


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
    MenuCardComponent,
    DetectorCardComponent,
    HomeCardComponent,
    PlayerCardComponent,
    ProjectCardComponent,
    RecordCardComponent,
    TrainerCardComponent,
    TrainerLessonCardComponent,
    TrainerLessonFrameCardComponent,
    TrainerLessonSuggestionCardComponent,
    TrainerLessonEventCardComponent,
    TrainerLessonTrainCardComponent,
    TrainerLessonActionCardComponent,
    DetectorTrainSessionListCardComponent
  ],
  imports: [
    CommonModule,
    UtilsModule,
    TranslateModule,
    PipesModule,
    MomentModule,
    FormsModule,
    AceEditorModule,
    AceModule


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
    MenuCardComponent,
    DetectorCardComponent,
    HomeCardComponent,
    PlayerCardComponent,
    ProjectCardComponent,
    RecordCardComponent,
    TrainerCardComponent,
    TrainerLessonCardComponent,
    TrainerLessonFrameCardComponent,
    TrainerLessonSuggestionCardComponent,
    TrainerLessonEventCardComponent,
    TrainerLessonTrainCardComponent,
    TrainerLessonActionCardComponent
  ]
})
export class CardsModule { }
