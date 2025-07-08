import { Pipe, PipeTransform } from '@angular/core';
import { DetectorLabel } from '@api/index';

@Pipe({
  name: 'detectorClassFilter',
  standalone: false
})
export class DetectorClassFilterPipe implements PipeTransform {

  transform(array: DetectorLabel[],  value?: string| null): number {
    if (!array || value === undefined) {
      return -1;  // Return -1 if array, attribute or value is missing
    }

    return array.findIndex(item => item._id === value);
  }
}
