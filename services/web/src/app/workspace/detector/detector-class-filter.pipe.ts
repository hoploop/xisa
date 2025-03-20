import { Pipe, PipeTransform } from '@angular/core';
import { DetectorClass } from '@api/index';

@Pipe({
  name: 'detectorClassFilter',
  standalone: false
})
export class DetectorClassFilterPipe implements PipeTransform {

  transform(array: DetectorClass[],  value?: string| null): number {
    if (!array || value === undefined) {
      return -1;  // Return -1 if array, attribute or value is missing
    }

    return array.findIndex(item => item._id === value);
  }
}
