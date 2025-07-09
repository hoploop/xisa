import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProjectRecordCountPipe } from './project-record-count.pipe';
import { ProjectDetectorCountPipe } from './project-detector-count.pipe';
import { DetectorImageLabelCountPipe } from './detector-image-label-count.pipe';
import { DetectorClassFilterPipe } from './detector-class-filter.pipe';
import { DetectorTrainCountPipe } from './detector-train-count.pipe';
import { DetectorImageCountPipe } from './detector-image-count.pipe';
import { DetectorClassCountPipe } from './detector-class-count.pipe';
import { RecordEventNamePipe } from './record-event-name.pipe';
import { RecordEventFilterSyntheticPipe } from './record-event-filter-synthetic.pipe';
import { RecordActionCountPipe } from './record-action-count.pipe';
import { RecordOsNamePipe } from './record-os-name.pipe';
import { RecordFramesCountPipe } from './record-frames-count.pipe';
import { RecordDurationPipe } from './record-duration.pipe';
import { RecordFramePipe } from './record-frame.pipe';
import { RecordEventsCountPipe } from './record-events-count.pipe';
import { RecordVideoPipe } from './record-video.pipe';
import { RecordSizePipe } from './record-size.pipe';
import { RecordActionNamePipe } from './record-action-name.pipe';
import { DetectorLabelRemovablePipe } from './detector-label-removable.pipe';
import { DetectorTrainRunningPipe } from './detector-train-running.pipe';
import { DetectorTrainSessionCountPipe } from './detector-train-session-count.pipe';
import { DetectorImageLabelsPipe } from './detector-image-labels.pipe';
import { DetectorLabelLoadPipe } from './detector-label-load.pipe';



@NgModule({
  declarations: [
    ProjectRecordCountPipe,
    ProjectDetectorCountPipe,
    DetectorImageLabelCountPipe,
    DetectorClassFilterPipe,
    DetectorTrainCountPipe,
    DetectorImageCountPipe,
    DetectorClassCountPipe,
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
    DetectorLabelRemovablePipe,
    DetectorTrainRunningPipe,
    DetectorTrainSessionCountPipe,
    DetectorImageLabelsPipe,
    DetectorLabelLoadPipe,
  ],

  imports: [
    CommonModule
  ],
  exports: [
    ProjectRecordCountPipe,
    ProjectDetectorCountPipe,
    DetectorImageLabelCountPipe,
    DetectorClassFilterPipe,
    DetectorTrainCountPipe,
    DetectorImageCountPipe,
    DetectorClassCountPipe,
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
    DetectorLabelRemovablePipe,
    DetectorTrainRunningPipe,
    DetectorTrainSessionCountPipe,
    DetectorImageLabelsPipe,
    DetectorLabelLoadPipe

  ]
})
export class PipesModule { }
