import { Component, OnInit } from '@angular/core';
import {
  Action,
  Detector,
  DetectorLabel,
  Record,
  RecorderEventList200ResponseInner,
  TrainLesson,
} from '@api/index';
import { Frame } from '../record-frame';
import { RecordFrameSelectorComponent } from '../record-frame-selector/record-frame-selector.component';
import { RecordVideoComponent } from '../record-video/record-video.component';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-studio',
  standalone: false,
  templateUrl: './record-studio.component.html',
  styleUrl: './record-studio.component.scss',
})
export class RecordStudioComponent extends BaseComponent implements OnInit {

  name: string = '';
  description: string | undefined = '';
  recordId?: string;
  projectId?: string;
  record?: Record;
  frames: Frame[] = [];
  frame?: Frame = undefined;
  events: RecorderEventList200ResponseInner[] = [];
  detector?: Detector;
  detectorId?: string;
  syntheticEvents: boolean = false;
  lesson?: TrainLesson;



  ngOnInit(): void {
    this.recordId = this.route.snapshot.paramMap.get('record_id') || undefined;
    this.detectorId = this.route.snapshot.paramMap.get('detector_id') || undefined;
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

  loadTrainImageObjects(){
    if (!this.frame) return;
    this.loading.next(this.ctx.translate.instant('workspace.detector.training.loading_objects'));
    setTimeout(()=>{
      if (!this.lesson || !this.lesson._id || !this.frame) return;
      this.ctx.api.trainer.trainerLessonImageObjectList(this.lesson._id,this.frame.count).subscribe({
        next: (result)=>{
          this.loading.next(undefined);
          if (this.frame)
          this.frame.train = result.objects;
        },
        error: (result)=>{
          this.loading.next(undefined);
          this.error.next(result.error.detail);
        }
      })
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


  previousFrame(){
    if (!this.frame) return;
    let temp = this.frames[this.frame.count-1];
    this.frame = undefined;
            setTimeout(() => {
              this.frame = temp;
            });
  }

  nextFrame(){
    if (!this.frame) return;
    let temp = this.frames[this.frame.count+1];
    this.frame = undefined;
            setTimeout(() => {
              this.frame = temp;
            });
  }

  viewVideo() {
    if (!this.recordId) return;
    this.ctx
      .openModal<undefined>(RecordVideoComponent, { recordId: this.recordId },{size:'lg',centered:true})
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
        this.loadActions();
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
    if (!this.lesson) return;
    let delta = 0;
    if (this.record && this.record.start && this.record.end) {
      let start = new Date(this.record.start).getTime();
      let end = new Date(this.record.end).getTime();
      delta = end - start;
    }
    this.ctx.api.recorder.recorderFrameCount(this.lesson.record).subscribe({
      next: (result) => {
        if (this.lesson){
        let totalFrames = result;
        let deltaFrame = delta / totalFrames;
        let ms = 0;
        for (let i = 0; i < totalFrames; i++) {
          let evt = undefined;

          let pushed = false;
          for (let j = 0; j < this.events.length; j++) {
            if (this.events[j].frame == i) {
              evt = this.events[j];
              this.frames.push({
                count: i,
                event: evt,
                action:undefined,
                milliseconds: ms,
                suggestions: [],
                lesson: this.lesson,
                train: [],
                objects:[],
                texts: []
              });
              pushed=true;
            }
          }

          if (!pushed){
            this.frames.push({
              count: i,
              event: evt,
              action:undefined,
              milliseconds: ms,
              suggestions: [],
              lesson: this.lesson,
              train: [],
              objects:[],
              texts: []
            });
          }



          ms += deltaFrame;
        }
        if (this.frames.length > 0) {
          this.frame = this.frames[0];
        }
        this.loading.next(undefined);
        this.loadTrainImageObjects();
      }},
      error: (result) => {
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      },
    });
  }

  loadActions(){
    if (!this.lesson) return;
    this.ctx.api.recorder.recorderActionList(this.lesson.record,undefined,0,-1).subscribe({
      next: (result)=>{
        for (let i = 0; i < result.actions.length; i++){
          let action:Action = result.actions[i];

          this.frames.forEach((frame, index)=>{

            if (frame.event && frame.event._id == action.event){
              this.frames[index].action = action;
            }
          })
        }
      }
    })
  }


}
