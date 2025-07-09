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
      value: string,
      ...args: unknown[]
    ): Observable<boolean> {
      return new Observable<boolean>((observer) => {
        this.ctx.api.trainer.trainerSessionDetectorRunning(value).subscribe({
          next: (result)=>{
            observer.next(result);
          },
          error: (result)=>{
            observer.error(result);
          }
        })
      })}

}
