import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProjectListCardComponent } from './project-list-card/project-list-card.component';
import { ProjectDetailCardComponent } from './project-detail-card/project-detail-card.component';
import { ProjectFormModalComponent } from './project-form-modal/project-form-modal.component';
import { ProjectDetectorCountPipe } from './project-detector-count.pipe';
import { ProjectRecordCountPipe } from './project-record-count.pipe';
import { ProjectListPageComponent } from './project-list-page/project-list-page.component';
import { ProjectPageComponent } from './project-page/project-page.component';
import { UtilsModule } from '@utils/utils.module';
import { TranslateModule } from '@ngx-translate/core';
import { MomentModule } from 'ngx-moment';
import { FormsModule } from '@angular/forms';
import { RecordModule } from '@record/record.module';

@NgModule({
  declarations: [
    ProjectListCardComponent,
    ProjectRecordCountPipe,
    ProjectDetectorCountPipe,
    ProjectDetailCardComponent,
    ProjectFormModalComponent,
    ProjectPageComponent,
    ProjectListPageComponent,
  ],
  imports: [
    CommonModule,
    UtilsModule,
    TranslateModule,
    FormsModule,
    MomentModule,
    RecordModule
  ],
  exports: [
    ProjectListCardComponent,
    ProjectDetailCardComponent,
    ProjectFormModalComponent,
    ProjectRecordCountPipe,
    ProjectDetectorCountPipe,
    ProjectPageComponent,
    ProjectListPageComponent,
  ],
})
export class ProjectModule {}
