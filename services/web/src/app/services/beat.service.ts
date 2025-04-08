import { Injectable } from '@angular/core';
import { Project } from '@api/index';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class BeatService {
  public auth = {
    logged: new BehaviorSubject<boolean | undefined>(undefined),
  };

  public menu = {
    project : new BehaviorSubject<Project|undefined>(undefined)
  }

}
