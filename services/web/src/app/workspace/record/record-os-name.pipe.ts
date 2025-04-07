import { Pipe, PipeTransform } from '@angular/core';
import {Record} from '@api/index';
import { ContextService } from '@services/context.service';
@Pipe({
  name: 'recordOsName',
  standalone: false
})
export class RecordOsNamePipe implements PipeTransform {

  constructor(private ctx:ContextService){

  }

  transform(record: Record, ...args: unknown[]): string {
    return record.os.name+ ' ('+record.os.version+')';
  }

}
