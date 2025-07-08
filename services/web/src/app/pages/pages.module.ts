import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomePageComponent } from './home-page/home-page.component';
import { ProjectListPageComponent } from './project-list-page/project-list-page.component';
import { AuthLoginRequiredPageComponent } from './auth-login-required-page/auth-login-required-page.component';
import { CardsModule } from '@cards/cards.module';
import { ProjectPageComponent } from './project-page/project-page.component';
import { UtilsModule } from '@utils/utils.module';
import { TranslateModule } from '@ngx-translate/core';
import { PipesModule } from '@pipes/pipes.module';
import { DetectorImageListPageComponent } from './detector-image-list-page/detector-image-list-page.component';
import { DetectorListPageComponent } from './detector-list-page/detector-list-page.component';
import { RecordListPageComponent } from './record-list-page/record-list-page.component';
import { RecordPageComponent } from './record-page/record-page.component';
import { PlayerPageComponent } from './player-page/player-page.component';
import { TrainerPageComponent } from './trainer-page/trainer-page.component';
import { MenuPageComponent } from './menu-page/menu-page.component';
import { DetectorPageComponent } from './detector-page/detector-page.component';
import { TrainerLessonPageComponent } from './trainer-lesson-page/trainer-lesson-page.component';



@NgModule({
  declarations: [
    HomePageComponent,
    ProjectListPageComponent,
    AuthLoginRequiredPageComponent,
    ProjectPageComponent,
    DetectorImageListPageComponent,
    DetectorListPageComponent,
    RecordListPageComponent,
    RecordPageComponent,
    PlayerPageComponent,
    TrainerPageComponent,
    MenuPageComponent,
    DetectorPageComponent,
    TrainerLessonPageComponent
  ],
  imports: [
    CommonModule,
    CardsModule,
    UtilsModule,
    TranslateModule,
    PipesModule
],
  exports: [
    HomePageComponent,
    ProjectListPageComponent,
    AuthLoginRequiredPageComponent,
    ProjectPageComponent,
    DetectorImageListPageComponent,
    DetectorListPageComponent,
    RecordListPageComponent,
    RecordPageComponent,
    PlayerPageComponent,
    TrainerPageComponent,
    MenuPageComponent,
    DetectorPageComponent,
    TrainerLessonPageComponent
  ]
})
export class PagesModule { }
