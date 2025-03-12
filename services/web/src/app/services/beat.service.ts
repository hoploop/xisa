import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BeatService {

  public auth = {
    logged: new BehaviorSubject<boolean|undefined>(undefined)
  };

  constructor() { }
}
