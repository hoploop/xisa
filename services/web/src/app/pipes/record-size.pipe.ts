import { Pipe, PipeTransform } from '@angular/core';
import { ContextService } from '@services/context.service';
import { Observable } from 'rxjs';

@Pipe({
  name: 'recordSize',
  standalone: false
})
export class RecordSizePipe implements PipeTransform {

  constructor(private ctx:ContextService){}

     transform(value: string|undefined|null, ...args: unknown[]): Observable<string> {
       return new Observable<string>(observer=>{
         if (value==undefined || value == null){
           observer.next('');
         }else{
         this.ctx.api.recorder.recorderSize(value).subscribe({
           next: (result)=>{
             observer.next(this.formatSize(result));
           },
           error: (result)=>{
             observer.error(result);
           }
         })}
       })
     }

     formatSize(value:number):string{
      if (value==0) return '';
      if (value < 1000) return value.toString()+' bytes';
      if (value < 1000000) return (value/1000).toFixed(2)+ 'Kb';
      return (value/1000000).toFixed(2)+' Mb';
     }

}
