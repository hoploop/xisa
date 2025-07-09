import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'detectorTrainRunning',
  standalone: false
})
export class DetectorTrainRunningPipe implements PipeTransform {

  transform(value: unknown, ...args: unknown[]): unknown {
    return null;
  }

}
