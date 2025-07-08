import { Injectable } from '@angular/core';
import { Project, Record } from '@api/index';
import { MenuArea } from '@models/menu-area-enum';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class BeatService {
  public auth = {
    logged: new BehaviorSubject<boolean | undefined>(undefined),
  };

  project = new BehaviorSubject<Project|undefined>(undefined);
  record = new BehaviorSubject<Record|undefined>(undefined);
  area = new BehaviorSubject<MenuArea>(MenuArea.UNKNOWN);
}
