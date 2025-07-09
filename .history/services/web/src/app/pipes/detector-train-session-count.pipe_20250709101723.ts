import { Pipe, PipeTransform } from '@angular/core';
import { ContextService } from '@services/context.service';
import { NGXLogger } from 'ngx-logger';
import { Observable } from 'rxjs';

@Pipe({
  name: 'detectorTrainSessionCount',
  standalone: false
})
export class DetectorTrainSessionCountPipe implements PipeTransform {

constructor(private ctx: ContextService,private log: NGXLogger) {}

    transform(
      value: string,
      ...args: unknown[]
    ): Observable<number> {
      return new Observable<number>((observer) => {
        this.ctx.api.trainer.trainerSessionList(value).subscribe({
          next: (result)=>{
            observer.next(result.total);
          },
          error: (result)=>{
            observer.error(result);
          }
        })
      })}

}
