import { Pipe, PipeTransform } from '@angular/core';
import { Record } from '@api/index';
import { ContextService } from '@services/context.service';
import { Observable } from 'rxjs';
@Pipe({
  name: 'recordActionCount',
  standalone: false
})
export class RecordActionCountPipe implements PipeTransform {

  constructor(private ctx:ContextService){

  }

  transform(record: Record, ...args: unknown[]): Observable<number> {
    return new Observable<number>(observer=>{
      if (!record._id){
        observer.next(0);
      }else{
        this.ctx.api.recorder.recorderActionCount(record._id).subscribe({
          next: (result)=>{
            observer.next(result);
          },
          error: (result)=>{
            observer.next(0);
          }
        })
      }

    })
  }

}
