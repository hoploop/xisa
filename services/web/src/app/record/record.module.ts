import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RecordEventCardComponent } from './record-event-card/record-event-card.component';
import { RecordListCardComponent } from './record-list-card/record-list-card.component';
import { RecordFrameScrollerCardComponent } from './record-frame-scroller-card/record-frame-scroller-card.component';
import { RecordCardComponent } from './record-card/record-card.component';
import { RecordActionModalComponent } from './record-action-modal/record-action-modal.component';
import { RecordFrameSelectorModalComponent } from './record-frame-selector-modal/record-frame-selector-modal.component';
import { RecordFormModalComponent } from './record-form-modal/record-form-modal.component';
import { RecordControllerModalComponent } from './record-controller-modal/record-controller-modal.component';
import { RecordVideoModalComponent } from './record-video-modal/record-video-modal.component';
import { RecordEventModalComponent } from './record-event-modal/record-event-modal.component';
import { RecordEventNamePipe } from './record-event-name.pipe';
import { RecordActionNamePipe } from './record-action-name.pipe';
import { RecordVideoPipe } from './record-video.pipe';
import { RecordFramePipe } from './record-frame.pipe';
import { RecordEventsCountPipe } from './record-events-count.pipe';
import { RecordDurationPipe } from './record-duration.pipe';
import { RecordFramesCountPipe } from './record-frames-count.pipe';
import { RecordSizePipe } from './record-size.pipe';
import { RecordOsNamePipe } from './record-os-name.pipe';
import { RecordActionCountPipe } from './record-action-count.pipe';
import { RecordEventFilterSyntheticPipe } from './record-event-filter-synthetic.pipe';
import { RecordListPageComponent } from './record-list-page/record-list-page.component';
import { RecordPageComponent } from './record-page/record-page.component';
import { UtilsModule } from '@utils/utils.module';
import { TranslateModule } from '@ngx-translate/core';
import { FormsModule } from '@angular/forms';
import { MomentModule } from 'ngx-moment';

@NgModule({
  declarations: [
    RecordEventCardComponent,
    RecordListCardComponent,
    RecordFrameScrollerCardComponent,
    RecordCardComponent,
    RecordControllerModalComponent,
    RecordFormModalComponent,
    RecordFrameSelectorModalComponent,
    RecordActionModalComponent,
    RecordVideoModalComponent,
    RecordEventModalComponent,
    RecordEventNamePipe,
    RecordActionNamePipe,
    RecordVideoPipe,
    RecordFramePipe,
    RecordEventsCountPipe,
    RecordDurationPipe,
    RecordFramesCountPipe,
    RecordSizePipe,
    RecordOsNamePipe,
    RecordActionCountPipe,
    RecordEventFilterSyntheticPipe,
    RecordListPageComponent,
    RecordPageComponent,
  ],
  imports: [
    CommonModule,
    UtilsModule,
    TranslateModule,
    FormsModule,
    MomentModule,
  ],
  exports: [
    RecordEventCardComponent,
    RecordListCardComponent,
    RecordFrameScrollerCardComponent,
    RecordCardComponent,
    RecordControllerModalComponent,
    RecordFormModalComponent,
    RecordFrameSelectorModalComponent,
    RecordActionModalComponent,
    RecordVideoModalComponent,
    RecordEventModalComponent,
    RecordEventNamePipe,
    RecordActionNamePipe,
    RecordVideoPipe,
    RecordFramePipe,
    RecordEventsCountPipe,
    RecordDurationPipe,
    RecordFramesCountPipe,
    RecordSizePipe,
    RecordOsNamePipe,
    RecordActionCountPipe,
    RecordEventFilterSyntheticPipe,
    RecordListPageComponent,
    RecordPageComponent,
  ],
})
export class RecordModule {}
