import { Component, Input, OnInit } from '@angular/core';
import { RecorderEventList200ResponseInner,Record, Detector, TrainLesson, DetectorLabel, Action } from '@api/index';
import { PlayerScriptPreviewModalComponent } from '@modals/player-script-preview-modal/player-script-preview-modal.component';
import { RecordFrameSelectorModalComponent } from '@modals/record-frame-selector-modal/record-frame-selector-modal.component';
import { RecordVideoModalComponent } from '@modals/record-video-modal/record-video-modal.component';
import { BaseComponent } from '@utils/base/base.component';
import { TreeNode } from '@utils/tree-node/tree-node.component';
import { Frame } from '@models/record-frame';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-record-studio-card',
  standalone: false,
  templateUrl: './record-studio-card.component.html',
  styleUrl: './record-studio-card.component.scss'
})
export class RecordStudioCardComponent  extends BaseComponent implements OnInit {
  @Input() record!: Record;
  nodes: TreeNode[] = [];
  selectedNode?:TreeNode;
  frames: Frame[] = [];
  frame?: Frame = undefined;
  events: RecorderEventList200ResponseInner[] = [];
  syntheticEvents: boolean = false;
  lesson?: TrainLesson;
  detector?: Detector;
  bottomSpace = new BehaviorSubject<number>(0);
  detectionLoading = new BehaviorSubject<boolean>(false);

  ngOnInit(): void {
    setTimeout(() => {
      this.loadDetector();
      this.loadLesson();
      this.loadEvents();
    });
  }

  onSelectNode(node:TreeNode){
    this.selectedNode = node;
  }

  loadTrainImageObjects() {
    if (!this.frame) return;
    this.loading.next(
      this.ctx.translate.instant('detector.training.loading_objects')
    );
    setTimeout(() => {
      if (!this.lesson || !this.lesson._id || !this.frame) return;
      this.ctx.api.trainer
        .trainerLessonImageObjectList(this.lesson._id, this.frame.count)
        .subscribe({
          next: (result) => {
            this.loading.next(undefined);
            if (this.frame) this.frame.train = result.objects;
          },
          error: (result) => {
            this.loading.next(undefined);
            this.error.next(result.error.detail);
          },
        });
    });
  }

  labelIsDetected(value: DetectorLabel): boolean {
    if (!this.frame) return false;
    for (let i = 0; i < this.frame.objects.length; i++) {
      let obj = this.frame.objects[i];
      if (obj.name == value.name) {
        return true;
      }
    }
    return false;
  }

  selectFrame() {
    this.ctx
      .openModal<Frame | undefined>(
        RecordFrameSelectorModalComponent,
        { frames: this.frames },
        { centered: true, size: 'lg' }
      )
      .subscribe({
        next: (result) => {
          if (result) {
            this.frame = undefined;
            setTimeout(() => {
              this.frame = result;
            });
          }
        },
        error: (result) => {},
      });
  }

  previewScript() {
    this.ctx
      .openModal<undefined>(
        PlayerScriptPreviewModalComponent,
        { record: this.record },
        { centered: true, size: 'lg' }
      )
      .subscribe({
        next: (result) => {},
        error: (result) => {},
      });
  }

  previousFrame() {
    if (!this.frame) return;
    let temp = this.frames[this.frame.count - 1];
    this.frame = undefined;
    setTimeout(() => {
      this.frame = temp;
    });
  }

  nextFrame() {
    if (!this.frame) return;
    let temp = this.frames[this.frame.count + 1];
    this.frame = undefined;
    setTimeout(() => {
      this.frame = temp;
    });
  }

  selectSpecificFrame(value: Frame) {
    this.frame = undefined;
    setTimeout(() => {
      this.frame = value;
    });
  }

  onResizeBottom(value: [number, number]) {
    this.bottomSpace.next(value[1]);
  }

  viewVideo() {
    if (!this.record._id) return;
    this.ctx
      .openModal<undefined>(
        RecordVideoModalComponent,
        { record: this.record },
        { size: 'lg', centered: true }
      )
      .subscribe({
        next: (result) => {},
        error: (result) => {},
      });
  }

  loadLesson() {
    if (!this.record._id) return;
    this.ctx.api.trainer.trainerLesson(this.record._id).subscribe({
      next: (result) => {
        this.lesson = result;
        this.loadActions();
      },
    });
  }

  updateDetectionLoading(value: boolean) {
    setTimeout(() => {
      this.detectionLoading.next(!value);
    });
  }

  loadDetector() {
    if (!this.lesson) return;
    if (!this.lesson.detector) return;
    this.ctx.api.detector.detectorLoad(this.lesson.detector).subscribe({
      next: (result) => {
        this.detector = result;
      },
    });
  }

  loadEvents() {
    if (!this.record._id) return;
    this.ctx.api.recorder.recorderEventList(this.record._id).subscribe({
      next: (result) => {
        this.events = result;
        this.loading.next(undefined);
        this.countFrames();
      },
      error: (result) => {
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      },
    });
  }

  countFrames() {
    if (!this.lesson) return;
    let delta = 0;
    if (this.record && this.record.start && this.record.end) {
      let start = new Date(this.record.start).getTime();
      let end = new Date(this.record.end).getTime();
      delta = end - start;
    }
    this.ctx.api.recorder.recorderFrameCount(this.lesson.record).subscribe({
      next: (result) => {
        if (this.lesson) {
          let totalFrames = result;
          let deltaFrame = delta / totalFrames;
          let ms = 0;
          for (let i = 0; i < totalFrames; i++) {
            let newFrame: Frame = new Frame(
              i,
              [],
              [],
              ms,
              [],
              [],
              this.lesson,
              [],
              []
            );

            for (let j = 0; j < this.events.length; j++) {
              if (this.events[j].frame == i) {
                let newEvent = this.events[j];
                newFrame.events.push(newEvent);
              }
            }

            this.frames.push(newFrame);

            ms += deltaFrame;
          }
          if (this.frames.length > 0) {
            this.frame = this.frames[0];
          }
          this.loading.next(undefined);
          this.loadTrainImageObjects();
        }
      },
      error: (result) => {
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      },
    });
  }

  loadActions() {
    if (!this.lesson) return;
    this.ctx.api.recorder
      .recorderActionList(this.lesson.record, undefined, 0, -1)
      .subscribe({
        next: (result) => {
          for (let i = 0; i < result.actions.length; i++) {
            let action: Action = result.actions[i];

            this.frames.forEach((frame, index) => {
              frame.events.forEach((evt, eindex) => {
                if (evt._id && evt._id == action.event) {
                  this.frames[index].actions.push(action);
                }
              });
            });
          }
        },
      });
  }
}
