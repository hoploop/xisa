import { Pipe, PipeTransform } from '@angular/core';
import { ContextService } from '@services/context.service';
import { NGXLogger } from 'ngx-logger';
import { Observable } from 'rxjs';

@Pipe({
  name: 'detectorTrainRunning',
  standalone: false
})
export class DetectorTrainRunningPipe implements PipeTransform {

  constructor(private ctx: ContextService,private log: NGXLogger) {}

    transform(
      value: string | undefined | null,
      ...args: unknown[]
    ): Observable<number> {
      return new Observable<number>((observer) => {

      })}

}
