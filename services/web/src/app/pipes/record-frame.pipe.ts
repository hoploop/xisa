import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'recordFrame',
  standalone: false
})
export class RecordFramePipe implements PipeTransform {

  transform(value: unknown, ...args: unknown[]): unknown {
    return null;
  }

}
