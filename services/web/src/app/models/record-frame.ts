import {
  Action,
  DetectObject,
  Detector,
  DetectorSuggestion,
  DetectText,
  RecorderEventList200ResponseInner,
  TrainImageObject,
  Record,
} from '@api/index';

export class Frame {
  constructor(
    public count: number,
    public events: RecorderEventList200ResponseInner[],
    public actions: Action[],
    public milliseconds: number,
    public suggestions: DetectorSuggestion[],
    public train: TrainImageObject[],
    public record: Record,
    public detector: Detector,
    public texts: DetectText[],
    public objects: DetectObject[]
  ) {}

  get hasEvents(): boolean {
    return this.events.length > 0;
  }

  get hasActions(): boolean {
    return this.actions.length > 0;
  }

  get hasSuggestion(): boolean {
    return this.suggestions.length > 0;
  }

  get hasSyntheticEvents(): boolean {
    if (this.events.length == 0) return false;
    for (let i = 0; i < this.events.length; i++){
      if (this.events[i].synthetic) return true;
    }
    return false;
  }

  get syntheticEvents(): RecorderEventList200ResponseInner[]{
    let ret = [];
    for (let i = 0; i < this.events.length; i++){
      if (this.events[i].synthetic) ret.push(this.events[i]);
    }
    return ret;
  }

  get avgConfidence(): number {
    if (this.actions.length == 0) return 0.0;
    let ret: number = 0.0;
    for (let i = 0; i < this.actions.length; i++) {
      ret += this.actions[i].confidence;
    }
    return ret / this.actions.length;
  }

  get calculateButtonClass(): string {
    if (!this.hasEvents) {
      return 'bg-light';
    } else if (this.hasEvents && this.hasActions && this.avgConfidence >= 0.5) {
      return 'bg-success text-white';
    } else if (this.hasEvents && this.hasActions && this.avgConfidence < 0.5) {
      return 'bg-warning';
    } else if (this.hasEvents && !this.hasActions) {
      return 'bg-danger text-white';
    } else {
      return 'bg-info';
    }
  }
}
