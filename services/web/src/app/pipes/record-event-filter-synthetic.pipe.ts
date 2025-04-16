import { Pipe, PipeTransform } from '@angular/core';
import { Observable } from 'rxjs';
import { Frame } from '../models/record-frame';

@Pipe({
  name: 'recordEventFilterSynthetic',
  standalone: false
})
export class RecordEventFilterSyntheticPipe implements PipeTransform {

  transform(frames: Frame[], synthetic:boolean = false): Observable<Frame[]> {
    return new Observable<Frame[]>(observer=>{
      let newFrames = frames.filter(frame => (!frame.hasEvents || frame.hasSyntheticEvents==synthetic));
      observer.next(newFrames);
    });
  }

}
