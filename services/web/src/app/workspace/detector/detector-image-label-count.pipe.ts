import { Pipe, PipeTransform } from '@angular/core';
import { DetectorImage } from '@api/index';
import { ContextService } from '@services/context.service';
import { Observable } from 'rxjs';

@Pipe({
  name: 'detectorImageLabelCount',
  standalone: false
})
export class DetectorImageLabelCountPipe implements PipeTransform {

 constructor(private ctx: ContextService) {}

   transform(
     value: DetectorImage
     ,
     ...args: unknown[]
   ): Observable<number> {
     return new Observable<number>((observer) => {
       if (!value._id) {
         observer.next(0);
       } else {
         this.ctx.api.detector.detectorImageLabelCount(value._id).subscribe({
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
