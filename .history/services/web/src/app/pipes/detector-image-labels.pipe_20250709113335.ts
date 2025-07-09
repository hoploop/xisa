import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'detectorImageLabels',
  standalone: false
})
export class DetectorImageLabelsPipe implements PipeTransform {

  transform(value: unknown, ...args: unknown[]): unknown {
    return null;
  }

}
