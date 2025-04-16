import {
  AfterViewInit,
  Component,
  Input,
  OnDestroy,
  OnInit,
  Output,
} from '@angular/core';
import {
  Action,
  DetectObject,
  DetectorLabel,
  DetectorSuggestion,
  DetectText,
  RecorderEventList200ResponseInner,
  TrainImageObject,
  TrainLesson,
} from '@api/index';
import { BaseComponent } from '@utils/base/base.component';
import { ImageAnnotatorBox } from '@utils/image-annotator/image-annotator-box';
import { ImageAnnotatorHighlight } from '@utils/image-annotator/image-annotator-highlight';
import { ImageAnnotatorSettings } from '@utils/image-annotator/image-annotator-settings';
import { TreeNode } from '@utils/tree-node/tree-node.component';
import { RecordEventTypes } from '@models/record-event-types.enum';
import { Frame } from '@models/record-frame';
import { BehaviorSubject, forkJoin, Observable } from 'rxjs';
import { DetectorSuggestionListModalComponent } from '@modals/detector-suggestion-list-modal/detector-suggestion-list-modal.component';
import { TrainObjectModalComponent } from '@modals/train-object-modal/train-object-modal.component';
import { DetectorSettingsModalComponent } from '@modals/detector-settings-modal/detector-settings-modal.component';
import { RecordEventModalComponent } from '@modals/record-event-modal/record-event-modal.component';
import { DetectorTextModalComponent } from '@modals/detector-text-modal/detector-text-modal.component';
import { DetectorObjectModalComponent } from '@modals/detector-object-modal/detector-object-modal.component';
import { AutoSuggestionModalComponent } from '@modals/auto-suggestion-modal/auto-suggestion-modal.component';
import { DetectorLabelSelectModalComponent } from '@modals/detector-label-select-modal/detector-label-select-modal.component';
import { RecordActionModalComponent } from '@modals/record-action-modal/record-action-modal.component';
import { DetectorTextSettingsModalComponent } from '@modals/detector-text-settings-modal/detector-text-settings-modal.component';
import { environment } from '@environments/environment';
import { BIconType, FAIconType } from '@constants/icons';

@Component({
  selector: 'app-record-frame-card',
  standalone: false,
  templateUrl: './record-frame-card.component.html',
  styleUrl: './record-frame-card.component.scss',
})
export class RecordFrameCardComponent
  extends BaseComponent
  implements AfterViewInit, OnInit, OnDestroy
{
  @Input() frame!: Frame;
  @Input() lesson!: TrainLesson;
  boxes = new BehaviorSubject<ImageAnnotatorBox[]>([]);
  highlights = new BehaviorSubject<ImageAnnotatorHighlight[]>([]);
  nodes: TreeNode[] = [];

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

  settings = new BehaviorSubject<ImageAnnotatorSettings>({
    resizeHandleSize: 10,
    showHighlights: true,
    canCreateBox: false,
  });

  RecordEventTypes = RecordEventTypes;

  buildNodes() {
    this.nodes = [];

    let eventNodes: TreeNode[] = [];
    for (let i = 0; i < this.frame.events.length; i++) {
      eventNodes.push({
        id: 9,
        label: 'Event',
        faIcon: FAIconType.mouse,
        expanded: false,
        children: [],
        checked: false,
        callback: new Observable<any>((observer) => {
          this.toggleSuggestions();
        }),
      });
    }

    let eventsNode: TreeNode = {
      id: 1,
      label: this.ctx.translate.instant('recorder.studio.events_n', {
        n: this.frame.events.length,
      }),
      expanded: false,
      children: eventNodes,
      checked: false,
      callback: new Observable<any>((observer) => {
        this.toggleEvents();
      }),
    };
    let objectsNodeSettings: TreeNode = {
      id: 4,
      label: 'Settings',
      faIcon: FAIconType.cogs,
      expanded: false,
      children: [],
      checked: false,
      callback: new Observable<any>((observer) => {
        this.detectorSettings();
      }),
    };
    let objectsNode: TreeNode = {
      id: 2,
      label: this.ctx.translate.instant('recorder.studio.detected_objects', {
        n: this.frame.objects.length,
      }),
      faIcon: FAIconType.shapes,
      expanded: false,
      children: [objectsNodeSettings],
      checked: false,
      callback: new Observable<any>((observer) => {
        this.toggleObjects();
      }),
    };

    let textNodeSettings: TreeNode = {
      id: 5,
      label: 'Settings',
      faIcon: FAIconType.cogs,
      expanded: false,
      children: [],
      checked: false,
      callback: new Observable<any>((observer) => {
        this.textDetectionSettings();
      }),
    };
    let textsNode: TreeNode = {
      id: 6,
      label: this.ctx.translate.instant('recorder.studio.detected_texts', {
        n: this.frame.texts.length,
      }),
      bIcon: BIconType.textareaT,
      expanded: false,
      children: [textNodeSettings],
      checked: false,
      callback: new Observable<any>((observer) => {
        this.toggleTexts();
      }),
    };

    let trainsNode: TreeNode = {
      id: 8,
      label: this.ctx.translate.instant('recorder.studio.train', {
        n: this.frame.train.length,
      }),
      bIcon: BIconType.boundingBox,
      expanded: false,
      children: [],
      checked: false,
      callback: new Observable<any>((observer) => {
        this.toggleTrain();
      }),
    };

    let suggestionNodes: TreeNode[] = [];
    for (let i = 0; i < this.frame.suggestions.length; i++) {
      suggestionNodes.push({
        id: 9,
        label: this.ctx.translate.instant('detector.suggestion.title_n', {
          n: this.frame.suggestions.length,
        }),
        faIcon: FAIconType.handPointer,
        expanded: false,
        children: [],
        checked: false,
        callback: new Observable<any>((observer) => {
          this.toggleSuggestions();
        }),
      });
    }

    let suggestionsNode: TreeNode = {
      id: 9,
      label: this.ctx.translate.instant('detector.suggestion.title_n', {
        n: this.frame.suggestions.length,
      }),
      faIcon: FAIconType.handPointer,
      expanded: false,
      children: suggestionNodes,
      checked: false,
      callback: new Observable<any>((observer) => {
        this.toggleSuggestions();
      }),
    };

    let actionsNode: TreeNode = {
      id: 10,
      label: this.ctx.translate.instant('recorder.action.title_n', {
        n: this.frame.actions.length,
      }),
      faIcon: FAIconType.handPointer,
      expanded: false,
      children: [],
      checked: false,
      callback: new Observable<any>((observer) => {
        this.toggleActions();
      }),
    };

    this.nodes.push(eventsNode);
    this.nodes.push(objectsNode);
    this.nodes.push(textsNode);
    this.nodes.push(trainsNode);
    this.nodes.push(suggestionsNode);
    this.nodes.push(actionsNode);
  }

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

  listSuggestions() {
    this.log.info('Loading suggestions');
    this.suggestionsVisible = true;
    this.render();
    this.ctx
      .openModal<undefined>(
        DetectorSuggestionListModalComponent,
        {
          suggestions: this.frame.suggestions,
          suggestionBoxes: this.suggestionBoxes,
          boxes: this.boxes.getValue(),
        },
        { size: 'lg' }
      )
      .subscribe({
        next: (result) => {},
        error: (result) => {},
      });
  }

  detectTrainObjectDetail(box: ImageAnnotatorBox, train: TrainImageObject) {
    this.ctx
      .openModal<undefined>(TrainObjectModalComponent, {
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
          .openModal<number>(DetectorSettingsModalComponent, {
            detector: result,
            confidence: this.lesson.objectConfidence,
          })
          .subscribe({
            next: (result) => {
              this.lesson.objectConfidence = result;
              if (this.lesson._id) {
                this.ctx.api.trainer
                  .trainerLessonSetObjectConfidence(this.lesson._id, result)
                  .subscribe({
                    next: (result) => {},
                    error: (result) => {
                      this.log.warn(result.error.detail);
                    },
                  });
              }
            },
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
      .openModal<undefined>(RecordEventModalComponent, {
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
      .openModal<undefined>(DetectorTextModalComponent, {
        box: box,
        text: text,
      })
      .subscribe({
        next: (result) => {},
        error: (result) => {},
      });
  }

  detectObjectDetail(box: ImageAnnotatorBox, obj: DetectObject) {
    this.ctx
      .openModal<undefined>(DetectorObjectModalComponent, {
        box: box,
        obj: obj,
      })
      .subscribe({
        next: (result) => {},
        error: (result) => {},
      });
  }

  suggestionDetail(box: ImageAnnotatorBox, suggestion: DetectorSuggestion) {
    this.ctx
      .openModal<Action>(
        AutoSuggestionModalComponent,
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
      .openModal<DetectorLabel[] | undefined>(
        DetectorLabelSelectModalComponent,
        {
          detectorId: this.frame.lesson.detector,
          selected: box.labels,
        }
      )
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
        RecordActionModalComponent,
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
        this.log.debug('Object detection completed with no detector specified');
        return;
      }
      this.ctx.api.detector
        .detectorObjectsFromFrame(
          this.frame.lesson.record,
          this.frame.lesson.detector,
          this.frame.count,
          this.lesson.objectConfidence || 0.1
        )
        .subscribe({
          next: (result) => {
            this.frame.objects = result;
            observer.next(true);
            observer.complete();
            this.log.debug('Object detection completed');
          },
          error: (result) => {
            observer.next(true);
            observer.complete();
            this.log.debug('Object detection completed');
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

  textDetectionSettings() {
    this.ctx
      .openModal<number>(DetectorTextSettingsModalComponent, {
        confidence: this.lesson.textConfidence,
      })
      .subscribe({
        next: (result) => {
          if (this.lesson._id) {
            this.ctx.api.trainer
              .trainerLessonSetTextConfidence(this.lesson._id, result)
              .subscribe({
                next: (result) => {},
                error: (result) => {
                  this.log.warn(result.error.detail);
                },
              });
          }
        },
      });
  }

  loadSuggestions(): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      if (!this.frame.hasEvents) {
        observer.next(true);
        observer.complete();
        this.log.debug('Suggestions loaded');
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
        this.log.debug('Suggestions loaded');
      });
    });
  }

  detectTexts(): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      this.loading.next(this.ctx.translate.instant('recorder.frame.loading'));
      this.ctx.api.detector
        .detectorFrameTexts(
          this.frame.lesson.record,
          this.frame.count,
          this.lesson.textConfidence || 0.1
        )
        .subscribe({
          next: (result) => {
            this.frame.texts = result;
            this.loading.next(undefined);
            observer.next(true);
            observer.complete();
            this.log.debug('Text detection completed');
          },
          error: (result) => {
            observer.next(true);
            observer.complete();
            this.log.debug('Text detection completed');
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
      let evt = this.frame.events[i];
      this.eventBoxes.clear();

      if (evt.position) {
        let x = evt.position[0] - 20;
        let y = evt.position[1] - 20;
        let w = 40;
        let h = 40;
        let evt_box = new ImageAnnotatorBox(x, y, w, h);
        evt_box.canResize = false;
        evt_box.canMove = false;
        evt_box.showCross = true;
        this.eventBoxes.set(evt_box.id, evt);
        ret.push(evt_box);
      }
    }
    return ret;
  }

  load() {
    this.loading.next(this.ctx.translate.instant('recorder.frame.loading'));
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
      this.buildNodes();
    });
  }

  loadActions(): Observable<boolean> {
    return new Observable<boolean>((observer) => {
      if (!this.frame.hasEvents) {
        observer.next(true);
        observer.complete();
        this.log.debug('Actions loaded without events');
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
          this.log.debug('Actions loaded');
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
