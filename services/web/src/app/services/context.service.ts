import { Injectable } from '@angular/core';
import { ApiService } from './api.service';
import { TranslateService } from '@ngx-translate/core';
import { StorageKeys } from '@constants/storage';
import { v4 as uuid } from 'uuid';
import { BeatService } from './beat.service';
import { WsService } from './ws.service';
import { NavigationService } from './navigation.service';
import { NgbActiveModal, NgbModal, NgbModalOptions } from '@ng-bootstrap/ng-bootstrap';
import { BehaviorSubject, Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ContextService {


  public resizeTop = new Subject<[number,number]>();

  constructor(
    public api: ApiService,
    public translate: TranslateService,
    public navigation: NavigationService,
    public beat: BeatService,
    public ws:WsService,
    private modal:NgbModal,
  ) {}

  private activeModal?:NgbActiveModal;


  public get session(): string {
    let found = localStorage.getItem(StorageKeys.session);
    if (found == undefined || found == null) {
      let nuuid = uuid();
      localStorage.setItem(StorageKeys.session, nuuid);
      return nuuid;
    } else {
      return found;
    }
  }


  public openModal<T>(content:any,values={},options:NgbModalOptions={centered:true}): Observable<T>{
    const modalRef = this.modal.open(content,options);
    this.activeModal = modalRef;
    Object.assign(modalRef.componentInstance,values);
    return new Observable<T>(observer=>{
      modalRef.result.then(result=>observer.next(result)).catch(error=>{observer.error(error)})
    })


  }

  public dismissModal(){
    this.modal.dismissAll();
  }

  public closeModal(value:any){
    if (this.activeModal){
      this.activeModal.close(value);
      this.activeModal = undefined;
    }


  }
}
