import { Pipe, PipeTransform } from '@angular/core';
import { DetectorLabel } from '@api/index';
import { ContextService } from '@services/context.service';
import { Observable } from 'rxjs';

@Pipe({
  name: 'detectorLabelRemovable',
  standalone: false
})
export class DetectorLabelRemovablePipe implements PipeTransform {

  constructor(private ctx:ContextService){}

  transform(value: DetectorLabel, selection: DetectorLabel[]=[]): Observable<boolean> {
    return new Observable<boolean>(observer=>{
      if (!value._id){
        observer.error('Id not found');

      }else{
        let foundInSelection = selection.findIndex(item=> item._id == value._id);
        if (foundInSelection!=-1){
          observer.next(false);
        }else{
        this.ctx.api.detector.detectorLabelCanRemove(value._id).subscribe({
          next: (result)=>{
            observer.next(result)
          },
          error: (result)=>{
            observer.error(result);
          }
        })}
      }
    })
  }

}
