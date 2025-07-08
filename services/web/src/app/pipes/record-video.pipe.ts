import { Pipe, PipeTransform } from '@angular/core';
import { ContextService } from '@services/context.service';
import { Observable } from 'rxjs';

@Pipe({
  name: 'recordVideo',
  standalone: false
})
export class RecordVideoPipe implements PipeTransform {

  constructor(private ctx:ContextService){}

  transform(value: string, ...args: unknown[]): Observable<any> {
    return new Observable(observer=>{
      this.ctx.api.recorder.recorderVideo(value).subscribe({
        next: (result)=>{
          observer.next(result);
        },
        error: (result)=>{
          observer.error(result);
        }
      })
    })
  }

}
