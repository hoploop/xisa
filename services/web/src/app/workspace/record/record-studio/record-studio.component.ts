import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import {
  DetectObject,
  Detector,
  DetectorLabel,
  DetectorSuggestion,
  DetectText,
  Record,
  TrainLesson,
} from '@api/index';
import { FAIconType } from '@constants/icons';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';
import { Frame } from '../record-frame';
import { RecordEventListRecordId200ResponseInner } from '@api/model/record-event-list-record-id200-response-inner';
import { RecordFrameSelectorComponent } from '../record-frame-selector/record-frame-selector.component';
import { RecordVideoComponent } from '../record-video/record-video.component';
import { RecordSuggestionsComponent } from '../record-suggestions/record-suggestions.component';
import { ImageAnnotatorBox } from '@train/image-annotator/image-annotator-box';
import { RecordTrainingComponent } from '../record-training/record-training.component';

@Component({
  selector: 'app-record-studio',
  standalone: false,
  templateUrl: './record-studio.component.html',
  styleUrl: './record-studio.component.scss',
})
export class RecordStudioComponent implements OnInit {
  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);
  name: string = '';
  description: string | undefined = '';
  FAIconType = FAIconType;
  recordId?: string;
  projectId?: string;
  record?: Record;
  frames_count: number = 0;
  frames: Frame[] = [];
  frame?: Frame = undefined;
  events: RecordEventListRecordId200ResponseInner[] = [];
  detector?: Detector;
  detectorId?: string;
  objects: DetectObject[] = [];
  texts: DetectText[] = [];
  suggestions: DetectorSuggestion[] = [];
  boxes: ImageAnnotatorBox[] = [];
  lesson?: TrainLesson;
  suggestionsTotal: number = 0;
  totalTrainingObjects = 0;

  constructor(
    private ctx: ContextService,
    private router: Router,
    route: ActivatedRoute
  ) {
    this.recordId = route.snapshot.paramMap.get('record_id') || undefined;
    this.detectorId = route.snapshot.paramMap.get('detector_id') || undefined;
  }

  ngOnInit(): void {
    setTimeout(()=>{
      this.loadDetector();
    this.load();
    this.loadLesson();
    this.loadEvents();
    });

  }

  load() {
    if (!this.recordId) return;
    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant('workspace.record.loading'));
    this.ctx.api.recorder.recorderLoad(this.recordId).subscribe({
      next: (result) => {
        this.record = result;
        this.projectId = result.project;
        this.loading.next(undefined);
      },
      error: (result) => {
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      },
    });
  }

  calculateSuggestions() {
    setTimeout(()=>{
      let tot = this.suggestions.length;
      this.boxes.forEach((box) => {
        tot += box.labels.length;
      });
      this.suggestionsTotal = tot;
    })

  }

  calculateTrainingObjects() {
    setTimeout(()=>{
    this.totalTrainingObjects = 0;
    this.boxes.forEach((box) => {
      box.labels.forEach((label) => {
        if (!this.labelIsDetected(label)) {
          this.totalTrainingObjects += 1;
        }
      });
    });});
  }

  labelIsDetected(value: DetectorLabel): boolean {
    if (!this.objects) return false;
    for (let i = 0; i < this.objects.length; i++) {
      let obj = this.objects[i];
      if (obj.name == value.name) {
        return true;
      }
    }
    return false;
  }

  onUpdateFrameBoxes(value: ImageAnnotatorBox[]) {
    this.boxes = value;
    this.calculateSuggestions();
    this.calculateTrainingObjects();
  }

  onUpdateDetectorSuggestions(value: DetectorSuggestion[]) {
    this.suggestions = value;
    this.calculateSuggestions();
  }

  onUpdateDetectedObjects(value: DetectObject[]) {
    this.objects = value;
    this.calculateSuggestions();
    this.calculateTrainingObjects();
  }

  onUpdateDetectedTexts(value: DetectText[]) {
    this.texts = value;
    this.calculateSuggestions();
    this.calculateTrainingObjects();
  }

  viewSuggestions() {
    this.ctx
      .openModal<undefined>(
        RecordSuggestionsComponent,
        {
          suggestions: this.suggestions,
          boxes: this.boxes,
          lesson: this.lesson,
          frame: this.frame?.count,
        },
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

  selectFrame() {
    this.ctx
      .openModal<Frame | undefined>(
        RecordFrameSelectorComponent,
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

  viewTrain() {
    this.ctx
      .openModal<undefined>(
        RecordTrainingComponent,
        {
          objects: this.objects,
          texts: this.texts,
          boxes: this.boxes,
          lesson: this.lesson,
          frame: this.frame?.count,
        },
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

  viewVideo() {
    if (!this.recordId) return;
    this.ctx
      .openModal<undefined>(RecordVideoComponent, { recordId: this.recordId })
      .subscribe({
        next: (result) => {},
        error: (result) => {},
      });
  }

  loadLesson() {
    if (!this.recordId) return;
    this.ctx.api.trainer.trainerLesson(this.recordId).subscribe({
      next: (result) => {
        this.lesson = result;
      },
    });
  }

  loadDetector() {
    if (!this.detectorId) return;
    this.ctx.api.detector.detectorLoad(this.detectorId).subscribe({
      next: (result) => {
        this.detector = result;
      },
    });
  }

  loadEvents() {
    if (!this.recordId) return;
    this.ctx.api.recorder.recorderEventList(this.recordId).subscribe({
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
    if (!this.recordId) return;
    let delta = 0;
    if (this.record && this.record.start && this.record.end) {
      let start = new Date(this.record.start).getTime();
      let end = new Date(this.record.end).getTime();
      delta = end - start;
    }
    this.ctx.api.recorder.recorderFrameCount(this.recordId).subscribe({
      next: (result) => {
        this.frames_count = result;
        let deltaFrame = delta / this.frames_count;
        let ms = 0;
        for (let i = 0; i < this.frames_count; i++) {
          let evt = undefined;

          for (let j = 0; j < this.events.length; j++) {
            if (this.events[j].frame == i) {
              evt = this.events[j];
              break;
            }
          }
          let ts = new Date();
          if (evt && evt.timestamp) {
            ts = new Date(evt.timestamp);
          }
          if (this.recordId) {
            this.frames.push({
              count: i,
              event: evt,
              record: this.recordId,
              resolved: false,
              milliseconds: ms,
            });
          }
          ms += deltaFrame;
        }
        if (this.frames.length > 0) {
          this.frame = this.frames[0];
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
