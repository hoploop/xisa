import { Pipe, PipeTransform } from '@angular/core';
import { DetectorLabel } from '@api/index';
import { ContextService } from '@services/context.service';
import { Observable } from 'rxjs';

@Pipe({
  name: 'detectorLabelLoad',
  standalone: false
})
export class DetectorLabelLoadPipe implements PipeTransform {

 constructor(private ctx: ContextService) {}

   transform(
     value: string | undefined | null
     ,
     ...args: unknown[]
   ): Observable<DetectorLabel> {
     return new Observable<DetectorLabel>((observer) => {
       if (!value) {
         observer.next([]);
       } else {
         this.ctx.api.detector.detectorLabelLoad(value).subscribe({
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
