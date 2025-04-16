import { Pipe, PipeTransform } from '@angular/core';
import { Record } from '@api/index';
import moment, { Duration } from 'moment';

@Pipe({
  name: 'recordDuration',
  standalone: false,
})
export class RecordDurationPipe implements PipeTransform {
  transform(value: Record, ...args: unknown[]): string {
    let duration: Duration = moment.duration(
      moment(value.end).diff(moment(value.start))
    );
    let hours = duration.asHours();
    let minutes = duration.asMinutes();
    let seconds = duration.asSeconds();
    let milliseconds = duration.asMilliseconds();
    return (
      this.formatTwoDigits(hours) +
      ':' +
      this.formatTwoDigits(minutes) +
      ':' +
      this.formatTwoDigits(seconds) +
      '.' +
      milliseconds.toFixed(0)
    );
  }

  formatTwoDigits(num: number): string {
    return num.toFixed(0).toString().padStart(2, '0');
  }
}
