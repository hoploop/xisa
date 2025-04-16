import { Pipe, PipeTransform } from '@angular/core';
import { ContextService } from '@services/context.service';
import { Detector, Project, Record } from '@api/index';
import { Observable } from 'rxjs';
@Pipe({
  name: 'recordLoadDetectorName',
  standalone: false
})
export class RecordLoadDetectorNamePipe implements PipeTransform {

  constructor(private ctx:ContextService){

  }

  transform(record: Record, ...args: unknown[]): Observable<string> {
    return new Observable<string>(observer=>{
      if (!record._id){
        observer.next(
          this.ctx.translate.instant("recorder.errors.no_detector")
        );
      }else{
        this.ctx.api.trainer.trainerLesson(record._id).subscribe({
          next: (result)=>{
            if (!result.detector){
              observer.next(this.ctx.translate.instant("recorder.errors.no_detector"));
            }else{
              this.ctx.api.detector.detectorLoad(result.detector).subscribe({
                next: (resultb)=>{
                  observer.next(resultb.name);
                }
              })
            }

          },
          error: (result)=>{
            observer.error(result);
          }
        })
      }

    })
  }

}
