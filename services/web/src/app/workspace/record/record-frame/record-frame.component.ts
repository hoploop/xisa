import {
  AfterViewInit,
  Component,
  Input,
  OnDestroy,
  OnInit,
  Output,
} from '@angular/core';
import { Frame } from '../record-frame';
import {
  DetectorLabel,
  DetectorSuggestion,
  KeyComboPressEventTypeEnum,
  KeyPressEventTypeEnum,
  KeyReleaseEventTypeEnum,
  MousePressEvent,
  MouseReleaseEvent,
  MouseClickEvent,
  MouseDoubleClickEvent,
  DetectObject,
  DetectText,
  TrainLesson,
  Action,
  MouseClickEventTypeEnum,
  RecorderEventList200ResponseInner,
  MousePressEventTypeEnum,
  MouseReleaseEventTypeEnum,
  MouseDoubleClickEventTypeEnum,
} from '@api/index';
import { environment } from '@environments/environment';
import { BaseComponent } from '@utils/base/base.component';
import { ImageAnnotatorBox } from '@utils/image-annotator/image-annotator-box';
import { ImageAnnotatorSettings } from '@utils/image-annotator/image-annotator-settings';
import { BehaviorSubject, forkJoin, Observable, of, Subscription } from 'rxjs';
import { DetectorLabelSelectComponent } from '@workspace/detector/detector-label-select/detector-label-select.component';
import { ImageAnnotatorHighlight } from '@utils/image-annotator/image-annotator-highlight';
import { TrainImageObject } from '@api/model/train-image-object';
import { RecordBoxDetectedObjectComponent } from '../record-box-detected-object/record-box-detected-object.component';
import { RecordBoxDetectedTextComponent } from '../record-box-detected-text/record-box-detected-text.component';
import { RecordBoxEventComponent } from '../record-box-event/record-box-event.component';
import { RecordBoxTrainObjectComponent } from '../record-box-train-object/record-box-train-object.component';
import { RecordBoxEventResult } from '../record-box-event/record-box-event-result';
import { RecordBoxDetectedTextResult } from '../record-box-detected-text/record-box-detected-text-result';
import { RecordBoxDetectedObjectResult } from '../record-box-detected-object/record-box-detected-object-result';
import { RecordBoxSuggestionComponent } from '../record-box-suggestion/record-box-suggestion.component';
import { DetectorSettingsComponent } from '@workspace/detector/detector-settings/detector-settings.component';
import { RecordActionComponent } from '../record-action/record-action.component';
import { RecordEventTypes } from '../record-event-types.enum';

@Component({
  selector: 'app-record-frame',
  standalone: false,
  templateUrl: './record-frame.component.html',
  styleUrl: './record-frame.component.scss',
})
export class RecordFrameComponent
  extends BaseComponent
  implements AfterViewInit, OnInit, OnDestroy
{
  @Input() frame!: Frame;
  @Input() lesson!: TrainLesson;
  boxes = new BehaviorSubject<ImageAnnotatorBox[]>([]);
  highlights = new BehaviorSubject<ImageAnnotatorHighlight[]>([]);

  textBoxes = new Map<string, DetectText>();
  objectBoxes = new Map<string, DetectObject>();
  trainBoxes = new Map<string, TrainImageObject>();
  eventBoxes = new Map<string, RecorderEventList200ResponseInner>();
  suggestionBoxes = new Map<string, DetectorSuggestion>();
  textsVisible = false;
  objectsVisible = false;
  trainVisible = false;
  eventsVisible = false;
  suggestionsVisible = false;
  actionsVisible = false;
  @Output() fullyLoaded = new BehaviorSubject<boolean>(false);

  subs = new Subscription();
  settings = new BehaviorSubject<ImageAnnotatorSettings>({
    resizeHandleSize: 10,
    showHighlights: true,
    canCreateBox: false,
  });

  RecordEventTypes = RecordEventTypes;

  toggleTexts() {
    this.textsVisible = !this.textsVisible;
    this.render();
  }

  toggleObjects() {
    this.objectsVisible = !this.objectsVisible;
    this.render();
  }

  toggleSuggestions() {
    this.suggestionsVisible = !this.suggestionsVisible;
    this.render();
  }

  toggleActions() {
    this.actionsVisible = !this.actionsVisible;
    this.render();
  }

  toggleTrain() {
    this.trainVisible = !this.trainVisible;

    // Update the image annotator so that it can create new box according to the train visibility
    let currentSettings = this.settings.getValue();
    currentSettings.canCreateBox = this.trainVisible;
    this.settings.next(currentSettings);

    // Render the image annotator box again
    this.render();
  }

  toggleEvents() {
    this.eventsVisible = !this.eventsVisible;
    this.render();
  }

  get imageUrl(): string {
    return (
      environment.imageUrl +
      this.frame.lesson.record +
      '/' +
      this.frame.count.toString()
    );
  }

  ngOnDestroy(): void {
    this.subs.unsubscribe();
  }

  ngOnInit(): void {
    this.subs.add(this.boxes.subscribe((result) => {}));
  }

  boxDetail(box: ImageAnnotatorBox) {
    if (this.suggestionBoxes.has(box.id)) {
      let suggestion: DetectorSuggestion | undefined = this.suggestionBoxes.get(
        box.id
      );
      if (suggestion) {
        this.suggestionDetail(box, suggestion);
      }
    } else if (this.objectBoxes.has(box.id)) {
      let obj: DetectObject | undefined = this.objectBoxes.get(box.id);
      if (obj) {
        this.detectObjectDetail(box, obj);
      }
    } else if (this.textBoxes.has(box.id)) {
      let text: DetectText | undefined = this.textBoxes.get(box.id);
      if (text) {
        this.detectTextDetail(box, text);
      }
    } else if (this.eventBoxes.has(box.id)) {
      let event: RecorderEventList200ResponseInner | undefined =
        this.eventBoxes.get(box.id);
      if (event) {
        this.eventDetail(box, event);
      }
    } else if (this.trainBoxes.has(box.id)) {
      let toi: TrainImageObject | undefined = this.trainBoxes.get(box.id);
      if (toi) {
        this.detectTrainObjectDetail(box, toi);
      }
    } else {
      if (!this.lesson._id) return;
      this.ctx.api.trainer
        .trainerLessonImageObject({
          lessonId: this.lesson._id,
          frame: this.frame.count,
          labels: [],
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
            this.detectTrainObjectDetail(box, result);
          },
          error: (result) => {
            this.log.warn(result.error.detail);
          },
        });
    }
  }

  boxUpdate(box: ImageAnnotatorBox) {
    if (this.trainBoxes.has(box.id)) {
      let toi = this.trainBoxes.get(box.id);
      if (toi && toi._id) {
        this.ctx.api.trainer
          .trainerLessonImageObjectUpdate({
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

  detectTrainObjectDetail(box: ImageAnnotatorBox, train: TrainImageObject) {
    this.ctx
      .openModal<undefined>(RecordBoxTrainObjectComponent, {
        box: box,
        train: train,
        lesson: this.lesson,
        frame: this.frame,
      })
      .subscribe({
        next: (result) => {
          this.render();
        },
        error: (result) => {},
      });
  }

  detectorSettings() {
    if (!this.lesson.detector) return;
    this.ctx.api.detector.detectorLoad(this.lesson.detector).subscribe({
      next: (result) => {
        this.ctx
          .openModal<undefined>(DetectorSettingsComponent, {
            detector: result,
          })
          .subscribe({
            next: (result) => {},
            error: (result) => {},
          });
      },
    });
  }

  eventDetail(
    box: ImageAnnotatorBox,
    event: RecorderEventList200ResponseInner
  ) {
    this.ctx
      .openModal<RecordBoxEventResult | undefined>(RecordBoxEventComponent, {
        box: box,
        event: event,
      })
      .subscribe({
        next: (result) => {},
        error: (result) => {},
      });
  }

  detectTextDetail(box: ImageAnnotatorBox, text: DetectText) {
    this.ctx
      .openModal<RecordBoxDetectedTextResult | undefined>(
        RecordBoxDetectedTextComponent,
        {
          box: box,
          text: text,
        }
      )
      .subscribe({
        next: (result) => {},
        error: (result) => {},
      });
  }

  detectObjectDetail(box: ImageAnnotatorBox, obj: DetectObject) {
    this.ctx
      .openModal<RecordBoxDetectedObjectResult | undefined>(
        RecordBoxDetectedObjectComponent,
        {
          box: box,
          obj: obj,
        }
      )
      .subscribe({
        next: (result) => {},
        error: (result) => {},
      });
  }

  suggestionDetail(box: ImageAnnotatorBox, suggestion: DetectorSuggestion) {
    this.ctx
      .openModal<Action>(
        RecordBoxSuggestionComponent,
        {
          box: box,
          suggestion: suggestion,
          lesson: this.lesson,
        },
        { size: 'lg' }
      )
      .subscribe({
        next: (result) => {
          this.loadActions();
          this.frame.actions.push(result);
        },
        error: (result) => {},
      });
  }

  selectClasses(box: ImageAnnotatorBox) {
    this.ctx
      .openModal<DetectorLabel[] | undefined>(DetectorLabelSelectComponent, {
        detectorId: this.frame.lesson.detector,
        selected: box.labels,
      })
      .subscribe({
        next: (result) => {
          this.render();
        },
        error: (result) => {},
      });
  }

  ngAfterViewInit(): void {
    setTimeout(() => {
      this.load();
    });
  }
  openAction(action: Action) {
    this.ctx
      .openModal<undefined | Action>(
        RecordActionComponent,
        {
          action: action,
        },
        { size: 'lg' }
      )
      .subscribe({
        next: (result) => {
          this.loadActions();
        },
        error: (result) => {},
      });
  }

  detectObjects(): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      if (!this.frame.lesson.detector) {
        observer.next(true);
        observer.complete();
        this.log.debug("Object detection completed with no detector specified");
        return;
      }
      this.ctx.api.detector
        .detectorObjectsFromFrame(
          this.frame.lesson.record,
          this.frame.lesson.detector,
          this.frame.count,
          0.1
        )
        .subscribe({
          next: (result) => {
            this.frame.objects = result;
            observer.next(true);
            observer.complete();
            this.log.debug("Object detection completed");
          },
          error: (result) => {
            observer.next(true);
            observer.complete();
            this.log.debug("Object detection completed");
          },
        });
    });
  }

  accept(suggestion: DetectorSuggestion) {}

  loadSuggestion(index: number): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      if (index > this.frame.events.length - 1) {
        observer.next(true);
        observer.complete();
        return;
      }
      let event = this.frame.events[index];
      if (!event._id) {
        observer.next(true);
        observer.complete();
        return;
      }

      if (!this.frame.lesson.detector) {
        observer.next(true);
        observer.complete();
        return;
      }

      this.ctx.api.detector
        .detectorFrameSuggestions(this.frame.lesson.detector, event._id, 0.1)
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

  loadSuggestions(): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      if (!this.frame.hasEvents){
        observer.next(true);
        observer.complete();
        this.log.debug("Suggestions loaded");
        return;
      }
      this.frame.suggestions = [];
      let calls = [];
      for (let i = 0; i < this.frame.events.length; i++) {
        calls.push(this.loadSuggestion(i));
      }



      forkJoin(calls).subscribe((results) => {
        observer.next(true);
        observer.complete();
        this.log.debug("Suggestions loaded");
      });
    });
  }

  detectTexts(): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      this.loading.next(
        this.ctx.translate.instant('workspace.record.frame.loading')
      );
      this.ctx.api.detector
        .detectorFrameTexts(this.frame.lesson.record, this.frame.count, 0.1)
        .subscribe({
          next: (result) => {
            this.frame.texts = result;
            this.loading.next(undefined);
            observer.next(true);
            observer.complete();
            this.log.debug("Text detection completed");
          },
          error: (result) => {
            observer.next(true);
            observer.complete();
            this.log.debug("Text detection completed");
          },
        });
    });
  }

  render() {
    // Reset boxes
    this.boxes.next([]);

    // Populate boxes
    let newBoxes: ImageAnnotatorBox[] = [];
    let eventBoxes = this.loadEventBoxes();
    let objectBoxes = this.loadObjectBoxes();
    let textBoxes = this.loadTextBoxes();
    let trainBoxes = this.loadTrainBoxes();
    let suggestionBoxes = this.loadSuggestionBoxes();
    newBoxes = newBoxes.concat(
      eventBoxes,
      objectBoxes,
      textBoxes,
      trainBoxes,
      suggestionBoxes
    );

    // Update boxes

    this.boxes.next(newBoxes);
  }

  loadSuggestionBoxes(): ImageAnnotatorBox[] {
    let ret: ImageAnnotatorBox[] = [];
    if (!this.suggestionsVisible) return [];
    this.suggestionBoxes.clear();
    for (let i = 0; i < this.frame.suggestions.length; i++) {
      let sug: DetectorSuggestion = this.frame.suggestions[i];
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
      n.defaultBorderColor = 'green';
      n.defaultBorderSize = 2;
      n.selectedBorderSize = 2;
      n.canResize = false;
      n.canMove = false;
      ret.push(n);
    }
    return ret;
  }

  loadObjectBoxes(): ImageAnnotatorBox[] {
    let ret: ImageAnnotatorBox[] = [];
    if (!this.objectsVisible) return [];
    this.objectBoxes.clear();
    for (let i = 0; i < this.frame.objects.length; i++) {
      let obj: DetectObject = this.frame.objects[i];
      let objBox = new ImageAnnotatorBox(obj.x, obj.y, obj.w, obj.h);
      this.objectBoxes.set(objBox.id, obj);
      objBox.canResize = false;
      objBox.canMove = false;
      ret.push(objBox);
    }
    return ret;
  }

  loadTextBoxes(): ImageAnnotatorBox[] {
    let ret: ImageAnnotatorBox[] = [];
    if (!this.textsVisible) return [];
    this.textBoxes.clear();
    for (let i = 0; i < this.frame.texts.length; i++) {
      let text: DetectText = this.frame.texts[i];
      let textBox = new ImageAnnotatorBox(text.x, text.y, text.w, text.h, true);
      this.textBoxes.set(textBox.id, text);
      textBox.canResize = false;
      textBox.canMove = false;
      ret.push(textBox);
    }
    return ret;
  }

  loadTrainBoxes(): ImageAnnotatorBox[] {
    let ret: ImageAnnotatorBox[] = [];
    if (!this.trainVisible) return [];
    this.trainBoxes.clear();
    for (let i = 0; i < this.frame.train.length; i++) {
      let tio: TrainImageObject = this.frame.train[i];
      let tioBox = new ImageAnnotatorBox(
        tio.xstart,
        tio.ystart,
        tio.xend - tio.xstart,
        tio.yend - tio.ystart
      );
      this.trainBoxes.set(tioBox.id, tio);
      tioBox.canResize = true;
      tioBox.canMove = true;
      ret.push(tioBox);
    }
    return ret;
  }

  loadEventBoxes(): ImageAnnotatorBox[] {
    if (!this.eventsVisible) return [];
    if (!this.frame) return [];
    if (!this.frame.hasEvents) return [];

    let ret: ImageAnnotatorBox[] = [];
    for (let i = 0; i < this.frame.events.length; i++) {
      let event = this.frame.events[i];
      this.eventBoxes.clear();
      switch (event.type) {
        case KeyComboPressEventTypeEnum.KeyComboPress:
          break;
        case KeyPressEventTypeEnum.KeyPress:
          break;
        case KeyReleaseEventTypeEnum.KeyRelease:
          break;
        case MouseClickEventTypeEnum.MouseClick:
          let evt = event as MouseClickEvent;
          if (evt.position) {
            let x = evt.position[0] - 20;
            let y = evt.position[1] - 20;
            let w = 40;
            let h = 40;
            let evt_box = new ImageAnnotatorBox(x, y, w, h);
            evt_box.canResize = false;
            evt_box.canMove = false;
            evt_box.showCross = true;
            this.eventBoxes.set(evt_box.id, event);
            ret.push(evt_box);
          }

          break;
        case MouseDoubleClickEventTypeEnum.MouseDoubleClick:
          let evt4 = event as MouseDoubleClickEvent;
          if (evt4.position) {
            let x = evt4.position[0] - 20;
            let y = evt4.position[1] - 20;
            let w = 40;
            let h = 40;
            let evt_box = new ImageAnnotatorBox(x, y, w, h);
            evt_box.canResize = false;
            evt_box.canMove = false;
            evt_box.showCross = true;
            this.eventBoxes.set(evt_box.id, event);
            ret.push(evt_box);
          }

          break;
        case MousePressEventTypeEnum.MousePress:
          let evt2 = event as MousePressEvent;
          if (evt2.position) {
            let x = evt2.position[0] - 20;
            let y = evt2.position[1] - 20;
            let w = 40;
            let h = 40;
            let evt_box = new ImageAnnotatorBox(x, y, w, h);
            evt_box.canResize = false;
            evt_box.canMove = false;
            evt_box.showCross = true;
            this.eventBoxes.set(evt_box.id, event);
            ret.push(evt_box);
          }
          break;
        case MouseReleaseEventTypeEnum.MouseRelease:
          let evt3 = event as MouseReleaseEvent;
          if (evt3.position) {
            let x = evt3.position[0] - 20;
            let y = evt3.position[1] - 20;
            let w = 40;
            let h = 40;
            let evt_box = new ImageAnnotatorBox(x, y, w, h);
            evt_box.canResize = false;
            evt_box.canMove = false;
            evt_box.showCross = true;
            this.eventBoxes.set(evt_box.id, event);
            ret.push(evt_box);
          }
          break;
        default:
          break;
      }
    }
    return ret;
  }

  load() {
    this.loading.next(
      this.ctx.translate.instant('workspace.record.frame.loading')
    );
    this.joinedLoad();

    this.loading.next(undefined);
  }

  joinedLoad() {
    this.fullyLoaded.next(false);

    let sources: Observable<any>[] = [
      this.loadActions(),
      this.detectObjects(),
      this.detectTexts(),
      this.loadSuggestions(),
    ];
    forkJoin(sources).subscribe((results) => {
      this.fullyLoaded.next(true);
    });
  }

  loadActions(): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      if (!this.frame.hasEvents) {
        observer.next(true);
        observer.complete();
        this.log.debug("Actions loaded without events");
      } else {
        this.frame.actions = [];
        let calls = [];
        for (let i = 0; i < this.frame.events.length; i++) {
          calls.push(this.loadAction(i));
        }

        forkJoin(calls).subscribe((results) => {
          if (this.frame.hasActions) {
            this.suggestionsVisible = false;
          }

          this.render();
          observer.next(true);
          observer.complete();
          this.log.debug("Actions loaded");
        });
      }
    });
  }

  loadAction(index: number): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      if (index > this.frame.events.length - 1) {
        observer.next(true);
        observer.complete();
        return;
      }
      let event = this.frame.events[index];
      if (!event._id) {
        observer.next(true);
        observer.complete();
        return;
      }
      this.ctx.api.recorder.recorderEventActionExist(event._id).subscribe({
        next: (res) => {
          if (res == true && event._id) {
            this.ctx.api.recorder
              .recorderActionLoadByEvent(event._id)
              .subscribe({
                next: (result) => {
                  this.frame.actions.push(result);
                  observer.next(true);
                  observer.complete();
                },
                error: (result) => {
                  observer.next(true);
                  observer.complete();
                },
              });
          } else {
            observer.next(true);
            observer.complete();
          }
        },
      });
    });
  }
}
