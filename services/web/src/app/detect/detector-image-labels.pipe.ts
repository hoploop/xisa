import { Pipe, PipeTransform } from '@angular/core';
import { DetectorImageLabel } from '@api/index';
import { ContextService } from '@services/context.service';
import { Observable } from 'rxjs';

@Pipe({
  name: 'detectorImageLabels',
  standalone: false
})
export class DetectorImageLabelsPipe implements PipeTransform {


 constructor(private ctx: ContextService) {}

   transform(
     value: string | undefined | null
     ,
     ...args: unknown[]
   ): Observable<DetectorImageLabel[]> {
     return new Observable<DetectorImageLabel[]>((observer) => {
       if (!value) {
         observer.next([]);
       } else {
         this.ctx.api.detector.detectorImageLabelList(value).subscribe({
           next: (result) => {
             observer.next(result.labels);
           },
           error: (result) => {
             observer.error(result);
           },
         });
       }
     });
   }

}
