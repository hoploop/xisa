import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Detector, Record } from '@api/index';
import { FAIconType } from '@constants/icons';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';
import { Frame } from '../record-frame';
import { DetectorSelectorComponent } from '@workspace/detector/detector-selector/detector-selector.component';
import { RecordEventListRecordId200ResponseInner } from '@api/model/record-event-list-record-id200-response-inner';



@Component({
  selector: 'app-record-studio',
  standalone: false,
  templateUrl: './record-studio.component.html',
  styleUrl: './record-studio.component.scss'
})
export class RecordStudioComponent implements OnInit {
  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);
  name: string = '';
  description: string|undefined = '';
  FAIconType = FAIconType;
  recordId?:string;
  projectId?:string;
  record?:Record;
  frames_count:number = 0;
  frames: Frame[] = [];
  frame?:Frame = undefined;
  events: RecordEventListRecordId200ResponseInner[] = [];
  detector?:Detector;

  constructor(
    private ctx: ContextService,
    private router: Router,
    route: ActivatedRoute
  ) {
    this.recordId = route.snapshot.paramMap.get('record_id') || undefined;
  }

  ngOnInit(): void {
    this.load();
    this.loadEvents();
  }

  load(){
    if (!this.recordId) return;
    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant('workspace.record.loading'));
    this.ctx.api.record.recordLoadRecorderid(this.recordId).subscribe({
      next: (result)=>{
        this.record = result;
        this.projectId = result.project;
        this.loading.next(undefined);
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }

  selectFrame(frame:Frame){
    console.log('Frame selected');
    this.frame=undefined;
    setTimeout(()=>{
      this.frame = frame;
    })

  }

  loadEvents(){
    if (!this.recordId) return;
    this.ctx.api.record.recordEventListRecordid(this.recordId).subscribe({
      next: (result)=>{
        this.events = result;
        this.loading.next(undefined);
        this.countFrames();
        console.log(result);
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }

  selectDetector(){
    this.ctx.openModal<Detector|undefined>(DetectorSelectorComponent,{projectId:this.projectId,detector:this.detector}).subscribe({
      next: (result)=>{
        if (result){
          this.detector = result;
        }
      },
      error: (result)=>{
      }
    });
  }

  countFrames(){
    if (!this.recordId) return;
    this.ctx.api.record.recordFrameCountRecordid(this.recordId).subscribe({
      next: (result)=>{
        this.frames_count = result;
        for (let i = 0; i < this.frames_count; i++){
          let evt= undefined;
          for (let j = 0; j < this.events.length; j++){
            if (this.events[j].frame == i){
              evt = this.events[j];
              break;
            }
          }
          if (this.recordId){
            this.frames.push({count: i,event: evt,record:this.recordId,resolved:false})
          }

        }
        this.loading.next(undefined);
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }
}
