import { Pipe, PipeTransform } from '@angular/core';
import { ContextService } from '@services/context.service';
import { NGXLogger } from 'ngx-logger';
import { Observable } from 'rxjs';

@Pipe({
  name: 'detectorTrainCount',
  standalone: false
})
export class DetectorTrainCountPipe  implements PipeTransform {
  constructor(private ctx: ContextService,private log: NGXLogger) {}

  transform(
    value: string | undefined | null,
    ...args: unknown[]
  ): Observable<number> {
    return new Observable<number>((observer) => {

      if (value == undefined || value == null) {
        observer.next(0);
      } else {
        this.ctx.api.trainer.trainerLessonImageObjectCountByDetector(value).subscribe({
          next: (result) => {
            observer.next(result);
          },
          error: (result) => {
            observer.error(result);
          },
        });
      }
    });
  }
}
