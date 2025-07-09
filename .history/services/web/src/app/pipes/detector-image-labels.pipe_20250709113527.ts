import { Pipe, PipeTransform } from '@angular/core';
import { DetectorImageLabelListResponse, DetectorLabel } from '@api/index';
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
   ): Observable<DetectorLabel[]> {
     return new Observable<DetectorImageLabelListResponse>((observer) => {
       if (!value) {
         observer.next(0);
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
