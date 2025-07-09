import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'detectorLabelLoad',
  standalone: false
})
export class DetectorLabelLoadPipe implements PipeTransform {

  transform(value: unknown, ...args: unknown[]): unknown {
    return null;
  }

}
