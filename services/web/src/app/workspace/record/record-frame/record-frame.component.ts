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
  MouseClickLeftEvent,
  MouseClickLeftEventTypeEnum,
  MousePressLeftEvent,
  MousePressLeftEventTypeEnum,
  DetectObject,
  DetectText,
  TrainLesson,
  MouseReleaseLeftEventTypeEnum,
  MouseReleaseLeftEvent,
} from '@api/index';
import { environment } from '@environments/environment';
import { BaseComponent } from '@utils/base/base.component';
import { ImageAnnotatorBox } from '@train/image-annotator/image-annotator-box';
import { ImageAnnotatorSettings } from '@train/image-annotator/image-annotator-settings';
import { BehaviorSubject, Subscription } from 'rxjs';
import { DetectorLabelSelectComponent } from '@workspace/detector/detector-label-select/detector-label-select.component';
import { ImageAnnotatorHighlight } from '@train/image-annotator/image-annotator-highlight';
import { TrainImageObject } from '@api/model/train-image-object';
import { RecordEventListRecordId200ResponseInner } from '@api/model/record-event-list-record-id200-response-inner';
import { RecordBoxDetectedObjectComponent } from '../record-box-detected-object/record-box-detected-object.component';
import { RecordBoxDetectedTextComponent } from '../record-box-detected-text/record-box-detected-text.component';
import { RecordBoxEventComponent } from '../record-box-event/record-box-event.component';
import { RecordBoxTrainObjectComponent } from '../record-box-train-object/record-box-train-object.component';
import { RecordBoxEventResult } from '../record-box-event/record-box-event-result';
import { RecordBoxDetectedTextResult } from '../record-box-detected-text/record-box-detected-text-result';
import { RecordBoxDetectedObjectResult } from '../record-box-detected-object/record-box-detected-object-result';
import { RecordBoxSuggestionComponent } from '../record-box-suggestion/record-box-suggestion.component';
import { RecordBoxSuggestionResult } from '../record-box-suggestion/record-box-suggestion-result';
import { DetectorSettingsComponent } from '@workspace/detector/detector-settings/detector-settings.component';

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
  eventBoxes = new Map<string, RecordEventListRecordId200ResponseInner>();
  suggestionBoxes = new Map<string, DetectorSuggestion>();
  textsVisible = false;
  objectsVisible = false;
  trainVisible = false;
  eventVisible = false;
  suggestionsVisible = false;

  subs = new Subscription();
  settings = new BehaviorSubject<ImageAnnotatorSettings>({
    resizeHandleSize: 10,
    showHighlights: true,
    canCreateBox: false,
  });

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

  toggleTrain() {
    this.trainVisible = !this.trainVisible;

    // Update the image annotator so that it can create new box according to the train visibility
    let currentSettings = this.settings.getValue();
    currentSettings.canCreateBox = this.trainVisible;
    this.settings.next(currentSettings);

    // Render the image annotator box again
    this.render();
  }

  toggleEvent() {
    this.eventVisible = !this.eventVisible;
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
      let event: RecordEventListRecordId200ResponseInner | undefined =
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

  detectorSettings(){
    if (!this.lesson.detector) return;
    this.ctx.api.detector.detectorLoad(this.lesson.detector).subscribe({next:(result)=>{
      this.ctx
      .openModal<undefined>(DetectorSettingsComponent, {
        detector: result
      })
      .subscribe({
        next: (result) => {

        },
        error: (result) => {},
      });
    }})


  }

  eventDetail(
    box: ImageAnnotatorBox,
    event: RecordEventListRecordId200ResponseInner
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
      .openModal<RecordBoxSuggestionResult | undefined>(
        RecordBoxSuggestionComponent,
        {
          box: box,
          suggestion: suggestion,
          lesson: this.lesson,
        }
      )
      .subscribe({
        next: (result) => {},
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

  detectObjects() {
    if (!this.frame.lesson.detector) return;
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
        },
        error: (result) => {
          console.log(result);
        },
      });
  }

  accept(suggestion: DetectorSuggestion) {}

  loadSuggestions() {
    if (!this.frame.event?._id) return;
    if (!this.frame.lesson.detector) return;
    this.ctx.api.detector
      .detectorFrameSuggestions(
        this.frame.lesson.detector,
        this.frame.event._id,
        0.1
      )
      .subscribe({
        next: (result) => {
          this.frame.suggestions = result;
        },
        error: (result) => {
          console.log(result);
        },
      });
  }

  detectTexts() {
    this.loading.next(
      this.ctx.translate.instant('workspace.record.frame.loading')
    );
    this.ctx.api.detector
      .detectorFrameTexts(this.frame.lesson.record, this.frame.count, 0.1)
      .subscribe({
        next: (result) => {
          this.frame.texts = result;
          this.loading.next(undefined);
        },
        error: (result) => {
          console.log(result);
        },
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
      let n = new ImageAnnotatorBox(sug.x, sug.y, sug.w, sug.h,true,false,true);
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
    if (!this.eventVisible) return [];
    if (!this.frame) return [];
    if (!this.frame.event) return [];

    let ret: ImageAnnotatorBox[] = [];
    let event = this.frame.event;
    this.eventBoxes.clear();
    switch (event.type) {
      case KeyComboPressEventTypeEnum.KeyComboPress:
        break;
      case KeyPressEventTypeEnum.KeyPress:
        break;
      case KeyReleaseEventTypeEnum.KeyRelease:
        break;
      case MouseClickLeftEventTypeEnum.MouseClickLeft:
        let evt = event as MouseClickLeftEvent;
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
      case MousePressLeftEventTypeEnum.MousePressLeft:
        let evt2 = event as MousePressLeftEvent;
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
        case MouseReleaseLeftEventTypeEnum.MouseReleaseLeft:
          let evt3 = event as MouseReleaseLeftEvent;
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
    return ret;
  }

  load() {
    this.loading.next(
      this.ctx.translate.instant('workspace.record.frame.loading')
    );
    this.detectObjects();
    this.detectTexts();
    this.loadSuggestions();

    this.loading.next(undefined);
  }
}
