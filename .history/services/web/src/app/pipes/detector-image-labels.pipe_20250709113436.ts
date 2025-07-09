import { Pipe, PipeTransform } from '@angular/core';
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
   ): Observable<number> {
     return new Observable<number>((observer) => {
       if (!value) {
         observer.next(0);
       } else {
         this.ctx.api.detector.detectorImageList(value).subscribe({
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
