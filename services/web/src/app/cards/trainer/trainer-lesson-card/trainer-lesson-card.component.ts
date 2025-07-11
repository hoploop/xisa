import { Component, Input, OnInit } from '@angular/core';
import {
  Detector,
  Record,
  Project,
  RecorderEventList200ResponseInner,
  DetectorSuggestion,
  TrainImageObject,
  DetectorLabel,
} from '@api/index';
import { Frame } from '@models/record-frame';
import { BaseComponent } from '@utils/base/base.component';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-trainer-lesson-card',
  standalone: false,
  templateUrl: './trainer-lesson-card.component.html',
  styleUrl: './trainer-lesson-card.component.scss',
})
export class TrainerLessonCardComponent
  extends BaseComponent
  implements OnInit
{
  @Input() detector!: Detector;
  @Input() record!: Record;
  @Input() project!: Project;
  marginBottom = new BehaviorSubject<number>(0);

  frames: Frame[] = [];
  frame = new BehaviorSubject<Frame | undefined>(undefined);
  suggestions: DetectorSuggestion[] = [];
  visibleSuggestions: DetectorSuggestion[] = [];
  visibleTrainImages: TrainImageObject[] = [];
  events: RecorderEventList200ResponseInner[] = [];

  ngOnInit(): void {
    setTimeout(() => {
      this.loadEvents();
    });
  }

  onResize(value: [number, number]) {
    this.marginBottom.next(value[1]);
  }

  selectFrame(frame: Frame) {
    this.log.debug('Selected frame: ' + frame.count.toString());
    this.frame.next(undefined);
    setTimeout(() => {
      this.frame.next(frame);
    }, 5);
  }

  loadEvents() {
    if (!this.record._id) return;
    this.ctx.api.recorder.recorderEventList(this.record._id).subscribe({
      next: (result) => {
        this.events = result;
        this.loading.next(undefined);
        this.loadFrames();
      },
      error: (result) => {
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      },
    });
  }

  loadFrames() {
    if (!this.record._id) return;
    let delta = 0;
    if (this.record && this.record.start && this.record.end) {
      let start = new Date(this.record.start).getTime();
      let end = new Date(this.record.end).getTime();
      delta = end - start;
    }
    this.ctx.api.recorder.recorderFrameCount(this.record._id).subscribe({
      next: (result) => {
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
            this.record,
            this.detector,
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
          this.frame.next(this.frames[0]);
        }
        this.loading.next(undefined);
      },
      error: (result) => {
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      },
    });
  }
}
