import { Component, Input, OnInit } from '@angular/core';
import {
  Action,
  DetectContour,
  DetectObject,
  DetectorLabel,
  DetectorSuggestion,
  DetectText,
  RecorderEventList200ResponseInner,
  TrainImageObject,
} from '@api/index';
import { environment } from '@environments/environment';
import { DetectorContourModalComponent } from '@detect/detector-contour-modal/detector-contour-modal.component';
import { DetectorLabelSelectModalComponent } from '@detect/detector-label-select-modal/detector-label-select-modal.component';
import { Frame } from '@record/record-frame';
import { BaseComponent } from '@utils/base/base.component';
import { ImageAnnotatorBox } from '@utils/image-annotator/image-annotator-box';
import { ImageAnnotatorHighlight } from '@utils/image-annotator/image-annotator-highlight';
import { ImageAnnotatorSettings } from '@utils/image-annotator/image-annotator-settings';
import { BehaviorSubject, forkJoin, Observable } from 'rxjs';
import { __values } from 'tslib';
@Component({
  selector: 'app-trainer-lesson-frame-card',
  standalone: false,
  templateUrl: './trainer-lesson-frame-card.component.html',
  styleUrl: './trainer-lesson-frame-card.component.scss',
})
export class TrainerLessonFrameCardComponent
  extends BaseComponent
  implements OnInit
{
  @Input() frame!: Frame;
  trainBoxes = new Map<string, TrainImageObject>();
  actionBoxes = new Map<string, Action>();
  suggestionBoxes = new Map<string, DetectorSuggestion>();
  eventBoxes = new Map<string, RecorderEventList200ResponseInner>();
  suggestionLoading = new BehaviorSubject<boolean>(false);

  contours: DetectContour[] = [];
  objects: DetectObject[] = [];
  texts: DetectText[] = [];
  contoursToggled: boolean = false;
  objectsToggled: boolean = false;
  textsToggled:boolean = false;
  contourNodesToggled: boolean = false;

  visibleSuggestions = new Map<string, DetectorSuggestion>();
  visibleEvents = new Map<string, RecorderEventList200ResponseInner>();
  visibleTrains = new Map<string, TrainImageObject>();
  visibleActions = new Map<string, Action>();
  visibleSuggestionsBoxes = new Map<string, string>();
  visibleTrainsBoxes = new Map<string, string>();
  visibleEventsBoxes = new Map<string, string>();
  visibleActionsBoxes = new Map<string, string>();

  boxes = new BehaviorSubject<ImageAnnotatorBox[]>([]);
  highlights = new BehaviorSubject<ImageAnnotatorHighlight[]>([]);
  imageLoaded = new BehaviorSubject<boolean>(false);
  settings = new BehaviorSubject<ImageAnnotatorSettings>({
    resizeHandleSize: 10,
    showHighlights: true,
    canCreateBox: true,
  });

  toggleContours(){
    if (this.contoursToggled){
      this.contoursToggled = false;
      this.render();
    }else{
      this.contoursToggled = true;
      this.objectsToggled = false;
      this.textsToggled = false;
      this.renderContours();
    }
  }


   toggleObjects(){
    if (this.objectsToggled){
      this.objectsToggled = false;
      this.render();
    }else{
      this.objectsToggled = true;
      this.contoursToggled = false;
      this.textsToggled = false;
      this.renderObjects();
    }
  }


   toggleTexts(){
    if (this.textsToggled){
      this.textsToggled = false;
      this.render();
    }else{
      this.textsToggled = true;
      this.contoursToggled = false;
      this.objectsToggled = false;
      this.renderTexts();

    }
  }

  ngOnInit(): void {
    setTimeout(() => {
      let calls = [];
      calls.push(this.loadSuggestions());
      calls.push(this.loadTrainImages());
      calls.push(this.loadActions());
      calls.push(this.loadContours());
      calls.push(this.loadObjects());
      calls.push(this.loadTexts());


      forkJoin(calls).subscribe((results) => {
        this.render();
      });
    });
  }

  get imageUrl(): string {
    return (
      environment.imageUrl +
      this.frame.record._id +
      '/' +
      this.frame.count.toString()
    );
  }

  boxRemove(box: ImageAnnotatorBox) {
    let boxes = this.boxes.getValue();
    let index = boxes.findIndex((item) => {
      return item.id == box.id;
    });
    if (index != -1) {
      boxes.splice(index, 1);
      this.boxes.next([]);
      setTimeout(() => {
        this.boxes.next(boxes);
      });
    }

    if (this.visibleEventsBoxes.has(box.id)) {
      let crossId = this.visibleEventsBoxes.get(box.id);
      if (crossId) {
        this.visibleEvents.delete(crossId);
      }
      this.visibleEventsBoxes.delete(box.id);
    }
    if (this.visibleSuggestionsBoxes.has(box.id)) {
      let crossId = this.visibleSuggestionsBoxes.get(box.id);
      if (crossId) {
        this.visibleSuggestions.delete(crossId);
      }
      this.visibleSuggestionsBoxes.delete(box.id);
    }
    if (this.visibleTrainsBoxes.has(box.id)) {
      let crossId = this.visibleTrainsBoxes.get(box.id);
      if (crossId) {
        this.visibleTrains.delete(crossId);
      }
      this.visibleTrainsBoxes.delete(box.id);
    }
  }

  boxAdd(box: ImageAnnotatorBox) {
    if (!this.frame.detector._id) return;
    let boxes = this.boxes.getValue();
    boxes.push(box);
     box.doubleClick.subscribe(result=>{
        this.boxDoubleClick(box);
      })
    this.boxes.next(boxes);
    this.ctx
      .openModal<DetectorLabel[] | undefined>(
        DetectorLabelSelectModalComponent,
        { detectorId: this.frame.detector._id},
        {size: 'lg',centered:true}
      )
      .subscribe({
        next: (result) => {
          if (!this.frame.record._id) return;
          if (!this.frame.detector._id) return;

          if (result == undefined || result.length == 0) {
            this.boxRemove(box);
            return;
          }
          let labels = [];
          for (let i = 0; i < result.length; i++) {
            labels.push(result[i].name);
          }

          this.ctx.api.trainer
            .trainerImageObjectCreate({
              recordId: this.frame.record._id,
              detectorId: this.frame.detector._id,
              frame: this.frame.count,
              labels: labels,
              xstart: box.x,
              xend: box.x + box.w,
              ystart: box.y,
              yend: box.y + box.h,
              val: true,
              test: true,
              train: true,
            })
            .subscribe({
              next: (result) => {
                this.trainBoxes.set(box.id, result);
                this.frame.train.push(result);
              },
              error: (result) => {
                this.log.warn(result.error.detail);
              },
            });
        },
        error: (result) => {
          this.boxRemove(box);
        },
      });
  }

  boxClick(box: ImageAnnotatorBox) {}

  contourDetails(contour:DetectContour){
    this.ctx.openModal<undefined>(DetectorContourModalComponent,{contour:contour}).subscribe({
      next: (result)=>{},
      error: (result)=>{}
    });
  }



  boxDoubleClick(box: ImageAnnotatorBox) {
    if (!this.frame.detector._id) return;
    this.ctx
      .openModal<DetectorLabel[] | undefined>(
        DetectorLabelSelectModalComponent,
        { detectorId: this.frame.detector._id, selected: box.labels },
        {size: 'lg',centered:true}
      )
      .subscribe({
        next: (result) => {
          if (result == undefined) {
            this.boxRemove(box);
            if (this.trainBoxes.has(box.id)) {
              let toi = this.trainBoxes.get(box.id);
              if (toi && toi?._id) {
                this.ctx.api.trainer
                  .trainerImageObjectRemove(toi._id)
                  .subscribe({
                    next: (resultb) => {
                      let rmIndex = this.frame.train.findIndex((item) => {
                        return item._id == toi._id;
                      });
                      if (rmIndex != -1) {
                        this.frame.train.splice(rmIndex, 1);
                      }
                    },
                    error: (resultb) => {
                      this.log.error(resultb.error.detail);
                    },
                  });
              }
            }
          } else if (this.trainBoxes.has(box.id)) {
            let toi = this.trainBoxes.get(box.id);
            if (toi && toi._id) {
              this.ctx.api.trainer
                .trainerImageObjectUpdate({
                  id: toi._id,
                  labels: toi.labels || [],
                  val: toi.val || true,
                  test: toi.test || true,
                  train: toi.train || true,
                  xstart: box.x,
                  xend: box.x + box.w,
                  ystart: box.y,
                  yend: box.y + box.h,
                })
                .subscribe({
                  next: (result) => {},
                  error: (result) => {},
                });
            }
          }
        },
      });
  }

  boxUpdate(box: ImageAnnotatorBox) {
    if (this.trainBoxes.has(box.id)) {
      let toi = this.trainBoxes.get(box.id);
      if (toi && toi._id) {
        this.ctx.api.trainer
          .trainerImageObjectUpdate({
            id: toi._id,
            labels: toi.labels || [],
            val: toi.val || true,
            test: toi.test || true,
            train: toi.train || true,
            xstart: box.x,
            xend: box.x + box.w,
            ystart: box.y,
            yend: box.y + box.h,
          })
          .subscribe({
            next: (result) => {},
            error: (result) => {},
          });
      }
    }
  }

  loadSuggestionBoxes(): ImageAnnotatorBox[] {
    let ret: ImageAnnotatorBox[] = [];
    this.suggestionBoxes.clear();
    for (let [key, value] of this.visibleSuggestions) {
      let sug: DetectorSuggestion = value;
      let n = new ImageAnnotatorBox(
        sug.x,
        sug.y,
        sug.w,
        sug.h,
        true,
        false,
        true
      );
      this.suggestionBoxes.set(n.id, sug);
      this.visibleSuggestionsBoxes.set(n.id, key);
      n.defaultBorderColor = 'green';
      n.defaultBorderSize = 2;
      n.selectedBorderSize = 2;
      n.canResize = false;
      n.canMove = false;
      ret.push(n);
    }
    return ret;
  }

  loadEventBoxes(): ImageAnnotatorBox[] {
    if (!this.frame) return [];
    if (!this.frame.hasEvents) return [];

    let ret: ImageAnnotatorBox[] = [];
    this.eventBoxes.clear();
    for (let [key, value] of this.visibleEvents) {
      let evt = value;

      if (evt.position) {
        let x = evt.position[0] - 0.04;
        let y = evt.position[1] - 0.04;
        let w = 0.08;
        let h = 0.08;
        let evt_box = new ImageAnnotatorBox(x, y, w, h,true);
        evt_box.canResize = false;
        evt_box.canMove = false;
        evt_box.showCross = true;
        this.eventBoxes.set(evt_box.id, evt);
        this.visibleEventsBoxes.set(evt_box.id, key);
        ret.push(evt_box);
      }
    }
    return ret;
  }

  loadContourBoxes(): ImageAnnotatorBox[] {
    let ret: ImageAnnotatorBox[] = [];
    for (let contour of this.contours){
      let ctr_box = new ImageAnnotatorBox(contour.x,contour.y,contour.w,contour.h,true);
      ctr_box.canResize = false;
      ctr_box.canMove = false;
      ctr_box.showCross = true;
      ctr_box.doubleClick.subscribe(result=>{
        this.contourDetails(contour);
      })
      ret.push(ctr_box);
    }
    return ret;
  }


  loadObjectBoxes(): ImageAnnotatorBox[] {
    let ret: ImageAnnotatorBox[] = [];
    for (let obj of this.objects){
      let ctr_box = new ImageAnnotatorBox(obj.x,obj.y,obj.w,obj.h,true);
      ctr_box.canResize = false;
      ctr_box.canMove = false;
      ctr_box.showCross = true;
      ret.push(ctr_box);
    }
    return ret;
  }


  loadTextBoxes(): ImageAnnotatorBox[] {
    let ret: ImageAnnotatorBox[] = [];
    for (let txt of this.texts){
      let ctr_box = new ImageAnnotatorBox(txt.x,txt.y,txt.w,txt.h,true);
      ctr_box.canResize = false;
      ctr_box.canMove = false;
      ctr_box.showCross = true;
      ret.push(ctr_box);
    }
    return ret;
  }

  loadTrainBoxes(): ImageAnnotatorBox[] {
    let ret: ImageAnnotatorBox[] = [];
    this.trainBoxes.clear();
    let labelCalls = [];
    for (let [key, value] of this.visibleTrains) {
      let tio: TrainImageObject = value;
      let tioBox = new ImageAnnotatorBox(
        tio.xstart,
        tio.ystart,
        tio.xend - tio.xstart,
        tio.yend - tio.ystart
      );
      tioBox.doubleClick.subscribe(result=>{
        console.log("Double clicked");
        this.boxDoubleClick(tioBox);
      })
      this.trainBoxes.set(tioBox.id, tio);
      this.visibleTrainsBoxes.set(tioBox.id, key);

      tioBox.canResize = true;
      tioBox.canMove = true;
      if (value.labels) {
        labelCalls.push(this.loadTrainBoxLabels(value.labels, tioBox));
      }
      ret.push(tioBox);
    }

    if (labelCalls.length > 0) {
      forkJoin(labelCalls).subscribe((results) => {
        for (let i = 0; i < results.length; i++) {
          ret.push(results[i]);
        }
      });
      return ret;
    } else {
      return ret;
    }
  }

  loadTrainBoxLabels(
    values: string[],
    box: ImageAnnotatorBox
  ): Observable<ImageAnnotatorBox> {
    return new Observable<ImageAnnotatorBox>((observer) => {
      let calls = [];
      for (let i = 0; i < values.length; i++) {
        calls.push(this.loadTrainBoxLabel(values[i]));
      }

      forkJoin(calls).subscribe((results) => {
        for (let j = 0; j < results.length; j++) {
          let cResult = results[j];
          if (cResult) {
            this.log.debug(cResult);
            box.labels.push(cResult);
          }
        }
        observer.next(box);
        observer.complete();
      });
    });
  }

  loadTrainBoxLabel(value: string): Observable<DetectorLabel | undefined> {
    return new Observable<DetectorLabel | undefined>((observer) => {
      if (!this.frame.detector._id) {
        observer.next(undefined);
        observer.complete();
      } else {
        this.ctx.api.detector
          .detectorLabel(this.frame.detector._id, value)
          .subscribe({
            next: (result) => {
              observer.next(result);
              observer.complete();
            },
            error: (result) => {
              observer.next(undefined);
              observer.complete();
            },
          });
      }
    });
  }

  loadActions(): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      if (!this.frame.record._id) {
        observer.next(true);
        observer.complete();
      } else {
        this.ctx.api.recorder
          .recorderActionListByFrame(this.frame.record._id,this.frame.count)
          .subscribe({
            next: (result) => {
              this.frame.actions = result;
              observer.next(true);
              observer.complete();
            },
            error: (result)=>{
              this.log.warn(result.error.detail);
              observer.next(false);
              observer.complete();
            }
          });
      }
    });
  }

  loadTrainImages(): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      if (!this.frame.detector._id || !this.frame.record._id) {
        observer.next(true);
        observer.complete();
      } else {
        this.log.debug(
          'Loading train objects for frame: ' + this.frame.count.toString()
        );
        this.ctx.api.trainer
          .trainerImageObjectList(this.frame.detector._id, this.frame.record._id,this.frame.count)
          .subscribe({
            next: (result) => {
              this.frame.train = result.objects;
              this.log.debug(
                'Loaded train objects: ' + result.objects.length.toString()
              );
              observer.next(true);
              observer.complete();
            },
          });
      }
    });
  }

  loadContours(confidence:number = 0.1): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      if (!this.frame.record._id) {
        observer.next(true);
        observer.complete();
      } else {
        this.ctx.api.detector.detectorContoursFromFrame(this.frame.record._id,this.frame.count,0.2).subscribe({
          next: (result)=>{
            this.contours = result;
            this.log.info(result);
          },
          error: (error)=>{
            this.log.error(error);
          }}
        );
      }});

  }

  loadTexts(confidence:number = 0.1): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      if (!this.frame.record._id) {
        observer.next(true);
        observer.complete();
      } else {
        this.ctx.api.detector.detectorFrameTexts(this.frame.record._id,this.frame.count,0.2).subscribe({
          next: (result)=>{
            this.texts = result;
            this.log.info(result);
          },
          error: (error)=>{
            this.log.error(error);
          }}
        );
      }});

  }



  loadObjects(confidence:number = 0.1): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      if (!this.frame.record._id || !this.frame.detector._id) {
        observer.next(true);
        observer.complete();
      } else {
        this.ctx.api.detector.detectorObjectsFromFrame(this.frame.record._id,this.frame.detector._id,this.frame.count,0.2).subscribe({
          next: (result)=>{
            this.objects = result;
            this.log.info(result);
          },
          error: (error)=>{
            this.log.error(error);
          }}
        );
      }});

  }

  loadSuggestions(confidence: number = 0.1): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      this.log.debug("Loading suggestions");
      this.suggestionLoading.next(true);
      if (!this.frame.record._id) {
        observer.next(true);
        observer.complete();
        this.suggestionLoading.next(false);
      } else {
        let calls = [];
        this.frame.suggestions = [];
        for (let i = 0; i < this.frame.events.length; i++) {
          let eventId = this.frame.events[i]._id;
          if (eventId && this.frame.detector._id) {
            calls.push(
              this.loadSuggestionsByEventId(
                this.frame.detector._id,
                eventId,
                confidence
              )
            );
          }
        }
        if (this.frame.events.length > 0) {
          forkJoin(calls).subscribe((results) => {
            observer.next(true);
            observer.complete();
            this.suggestionLoading.next(false);
          });
        } else {
          this.suggestionLoading.next(false);
        }
      }
    });
  }

  loadSuggestionsByEventId(
    detectorId: string,
    eventId: string,
    confidence: number
  ) {
    return new Observable<boolean>((observer) => {
      this.ctx.api.detector
        .detectorFrameSuggestions(detectorId, eventId, confidence)
        .subscribe({
          next: (result) => {
            this.frame.suggestions = this.frame.suggestions.concat(result);
            observer.next(true);
            observer.complete();
          },
          error: (result) => {
            observer.next(true);
            observer.complete();
          },
        });
    });
  }

  acceptSuggestion(id: string, suggestion: DetectorSuggestion) {
    let pos: number[] | undefined = [];
    if (suggestion.by_position == null) {
      pos = undefined;
    } else {
      pos = [suggestion.by_position.x, suggestion.by_position.y];
    }
    if (this.frame.record._id && this.frame.detector._id)
    this.ctx.api.recorder
      .recorderActionCreate({
        detectorId: this.frame.detector._id,
        recordId: this.frame.record._id,
        eventId: suggestion.event,
        byLabel: suggestion.by_label,
        byText: suggestion.by_text,
        byRegex: suggestion.by_regex,
        byOrder: suggestion.by_order,
        byPosition: pos,
        confidence: suggestion.confidence,
      })
      .subscribe({
        next: (result) => {
          this.frame.actions.push(result);
        },
        error: (result) => {
          this.log.warn(result.error.detail);
        },
      });
  }

  toggleSuggestion(
    id: string,
    suggestion: DetectorSuggestion,
    checked: boolean
  ) {
    this.log.debug('Toggling suggestion');
    if (checked) {
      this.visibleSuggestions.set(id, suggestion);
      this.render();
    } else {
      if (this.visibleSuggestions.has(id)) {
        this.visibleSuggestions.delete(id);
        this.render();
      }
    }
  }

  toggleTrain(id: string, train: TrainImageObject, checked: boolean) {
    this.log.debug('Toggling train');
    if (checked) {
      this.visibleTrains.set(id, train);
      this.render();
    } else {
      if (this.visibleTrains.has(id)) {
        this.visibleTrains.delete(id);
        this.render();
      }
    }
  }

  removeAction(id:string, action: Action){
    let foundIndex = this.frame.actions.findIndex(item=>{return item._id == action._id});
    if (foundIndex !=-1){
      this.frame.actions.splice(foundIndex,1);
    }
  }

  toggleAction(id: string, action: Action, checked: boolean) {
    this.log.debug('Toggling train');
    if (checked) {
      this.visibleActions.set(id, action);
      this.render();
    } else {
      if (this.visibleActions.has(id)) {
        this.visibleActions.delete(id);
        this.render();
      }
    }
  }

  toggleEvent(
    id: string,
    event: RecorderEventList200ResponseInner,
    checked: boolean
  ) {
    this.log.debug('Toggling event');
    if (checked) {
      this.visibleEvents.set(id, event);
      this.render();
    } else {
      if (this.visibleEvents.has(id)) {
        this.visibleEvents.delete(id);
        this.render();
      }
    }
  }

  render() {
    this.log.debug('Rendering');
    // Reset boxes
    this.boxes.next([]);

    // Populate boxes
    let newBoxes: ImageAnnotatorBox[] = [];
    let eventBoxes = this.loadEventBoxes();
    let trainBoxes = this.loadTrainBoxes();
    let suggestionBoxes = this.loadSuggestionBoxes();
    newBoxes = newBoxes.concat(eventBoxes, trainBoxes, suggestionBoxes);

    // Update boxes

    this.boxes.next(newBoxes);
  }

  renderContours(){
    // Reset boxes
    this.boxes.next([]);

    // Populate boxes
    let contourBoxes = this.loadContourBoxes();

    // Update boxes

    this.boxes.next(contourBoxes);
  }

  renderObjects(){
    // Reset boxes
    this.boxes.next([]);

    // Populate boxes
    let objectBoxes = this.loadObjectBoxes();

    // Update boxes

    this.boxes.next(objectBoxes);
  }


  renderTexts(){
    // Reset boxes
    this.boxes.next([]);

    // Populate boxes
    let textBoxes = this.loadTextBoxes();

    // Update boxes

    this.boxes.next(textBoxes);
  }


  removeTrain(value: TrainImageObject){
    let index = this.frame.train.indexOf(value);
    if (index!=-1){
      this.frame.train.splice(index,1);
    }

  }
}
