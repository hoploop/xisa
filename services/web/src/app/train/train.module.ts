import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TrainerCardComponent } from './trainer-card/trainer-card.component';
import { TrainerLessonCardComponent } from './trainer-lesson-card/trainer-lesson-card.component';
import { TrainerLessonFrameCardComponent } from './trainer-lesson-frame-card/trainer-lesson-frame-card.component';
import { TrainerLessonSuggestionCardComponent } from './trainer-lesson-suggestion-card/trainer-lesson-suggestion-card.component';
import { TrainerLessonEventCardComponent } from './trainer-lesson-event-card/trainer-lesson-event-card.component';
import { TrainerLessonTrainCardComponent } from './trainer-lesson-train-card/trainer-lesson-train-card.component';
import { TrainerLessonActionCardComponent } from './trainer-lesson-action-card/trainer-lesson-action-card.component';
import { TrainObjectModalComponent } from './train-object-modal/train-object-modal.component';
import { TrainerLessonPageComponent } from './trainer-lesson-page/trainer-lesson-page.component';
import { TrainerPageComponent } from './trainer-page/trainer-page.component';
import { UtilsModule } from '@utils/utils.module';
import { TranslateModule } from '@ngx-translate/core';
import { RecordModule } from '@record/record.module';
import { DetectModule } from '@detect/detect.module';
import { FormsModule } from '@angular/forms';
import { MomentModule } from 'ngx-moment';



@NgModule({
  declarations: [
    TrainerCardComponent,
    TrainerLessonCardComponent,
    TrainerLessonFrameCardComponent,
    TrainerLessonSuggestionCardComponent,
    TrainerLessonEventCardComponent,
    TrainerLessonTrainCardComponent,
    TrainerLessonActionCardComponent,
    TrainObjectModalComponent,
    TrainerLessonPageComponent,
    TrainerPageComponent,
  ],
  imports: [
    CommonModule,
    UtilsModule,
    TranslateModule,
    RecordModule,
    DetectModule,
    FormsModule,
    MomentModule
  ],
  exports: [
    TrainerCardComponent,
    TrainerLessonCardComponent,
    TrainerLessonFrameCardComponent,
    TrainerLessonSuggestionCardComponent,
    TrainerLessonEventCardComponent,
    TrainerLessonTrainCardComponent,
    TrainObjectModalComponent,
    TrainerLessonActionCardComponent,
    TrainerLessonPageComponent,
    TrainerPageComponent,
  ]
})
export class TrainModule { }
