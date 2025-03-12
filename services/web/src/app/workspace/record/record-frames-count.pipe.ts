import { Pipe, PipeTransform } from '@angular/core';
import { ContextService } from '@services/context.service';
import { Observable } from 'rxjs';

@Pipe({
  name: 'recordFramesCount',
  standalone: false
})
export class RecordFramesCountPipe implements PipeTransform {

 constructor(private ctx:ContextService){}

   transform(value: string|undefined|null, ...args: unknown[]): Observable<number> {
     return new Observable<number>(observer=>{
       if (value==undefined || value == null){
         observer.next(0);
       }else{
       this.ctx.api.record.recordFrameCountRecordId(value).subscribe({
         next: (result)=>{
           observer.next(result);
         },
         error: (result)=>{
           observer.error(result);
         }
       })}
     })
   }

}
