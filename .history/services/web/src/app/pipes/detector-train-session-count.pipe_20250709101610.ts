import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'detectorTrainSessionCount',
  standalone: false
})
export class DetectorTrainSessionCountPipe implements PipeTransform {

  transform(value: unknown, ...args: unknown[]): unknown {
    return null;
  }

}
