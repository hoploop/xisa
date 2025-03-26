import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { DetectObject, Detector, DetectorSuggestion, DetectText, Record } from '@api/index';
import { FAIconType } from '@constants/icons';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';
import { Frame } from '../record-frame';
import { RecordEventListRecordId200ResponseInner } from '@api/model/record-event-list-record-id200-response-inner';
import { RecordFrameSelectorComponent } from '../record-frame-selector/record-frame-selector.component';
import { RecordVideoComponent } from '../record-video/record-video.component';
import { RecordSuggestionsComponent } from '../record-suggestions/record-suggestions.component';
import { ImageAnnotatorBox } from '@train/image-annotator/image-annotator-box';

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
  suggestions: DetectorSuggestion[] =[];
  boxes: ImageAnnotatorBox[] = [];


  constructor(
    private ctx: ContextService,
    private router: Router,
    route: ActivatedRoute
  ) {
    this.recordId = route.snapshot.paramMap.get('record_id') || undefined;
    this.detectorId = route.snapshot.paramMap.get('detector_id') || undefined;
  }

  ngOnInit(): void {
    this.loadDetector();
    this.load();
    this.loadEvents();
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

  onUpdateFrameBoxes(value: ImageAnnotatorBox[]){
    this.boxes = value;
  }

  onUpdateDetectorSuggestions(value: DetectorSuggestion[]){
    this.suggestions = value;
  }

  onUpdateDetectedObjects(value:DetectObject[]){
    this.objects = value;
  }

  onUpdateDetectedTexts(value:DetectText[]){
    this.texts = value;
  }

  viewSuggestions(){
    this.ctx
      .openModal<undefined>(RecordSuggestionsComponent,{objects:this.objects,texts:this.texts,suggestions: this.suggestions,boxes: this.boxes},{centered:true,size:'lg'})
      .subscribe({
        next: (result) => {
          if (result) {
            this.frame = undefined;
            console.log(result);
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
      .openModal<Frame | undefined>(RecordFrameSelectorComponent,{frames:this.frames},{centered:true,size:'lg'})
      .subscribe({
        next: (result) => {
          if (result) {
            this.frame = undefined;
            console.log(result);
            setTimeout(() => {
              this.frame = result;
            });
          }
        },
        error: (result) => {},
      });
  }

  viewVideo(){
    if (!this.recordId) return;
    this.ctx
    .openModal<undefined>(RecordVideoComponent,{recordId:this.recordId})
    .subscribe({
      next: (result) => {

      },
      error: (result) => {},
    });
  }

  loadDetector(){

    if (!this.detectorId) return;
    this.ctx.api.detector.detectorLoad(this.detectorId).subscribe({next:(result)=>{
      this.detector = result;
    }})
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
    if (this.record && this.record.start && this.record.end){
      let start = new Date(this.record.start).getTime();
      let end = new Date(this.record.end).getTime();
      delta = end-start;

    }
    this.ctx.api.recorder.recorderFrameCount(this.recordId).subscribe({
      next: (result) => {

        this.frames_count = result;
        let deltaFrame = delta/this.frames_count;
        console.log(deltaFrame);
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
          if (evt && evt.timestamp){
            ts = new Date(evt.timestamp);
          }
          if (this.recordId) {
            this.frames.push({
              count: i,
              event: evt,
              record: this.recordId,
              resolved: false,
              milliseconds: ms
            });
          }
          ms += deltaFrame;
        }
        if (this.frames.length > 0){
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
