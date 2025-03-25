import { Pipe, PipeTransform } from '@angular/core';
import { ContextService } from '@services/context.service';
import { Observable } from 'rxjs';
import { RecordEventsCountPipe } from '../record/record-events-count.pipe';

@Pipe({
  name: 'projectRecordCount',
  standalone: false
})
export class ProjectRecordCountPipe implements PipeTransform {

 constructor(private ctx:ContextService){}

  transform(value: string|undefined|null, ...args: unknown[]): Observable<number> {
    return new Observable<number>(observer=>{
      if (value==undefined || value == null){
        observer.next(0);
      }else{
      this.ctx.api.recorder.recorderCount(value).subscribe({
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
