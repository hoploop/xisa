import { ComponentRef, Injectable, ViewContainerRef } from '@angular/core';
import { ApiService } from './api.service';
import { TranslateService } from '@ngx-translate/core';
import { StorageKeys } from '@constants/storage';
import { v4 as uuid } from 'uuid';
import { BeatService } from './beat.service';
import { WsService } from './ws.service';
import { NavigationService } from './navigation.service';
import { NgbActiveModal, NgbModal, NgbModalOptions } from '@ng-bootstrap/ng-bootstrap';
import { Observable, Subject } from 'rxjs';
import { MenuComponent } from '../menu/menu.component';


@Injectable({
  providedIn: 'root',
})
export class ContextService {


  public resizeTop = new Subject<[number,number]>();
  private mainContainer?:ViewContainerRef;

  constructor(
    public api: ApiService,
    public translate: TranslateService,
    public navigation: NavigationService,
    public beat: BeatService,
    public ws:WsService,
    private modal:NgbModal,
  ) {}

  private activeModal?:NgbActiveModal;

  public initialize(main:ViewContainerRef){
    this.mainContainer = main;
  }

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



  public open(componentType: any, values={}): Observable<ComponentRef<any>>{
    return new Observable<ComponentRef<any>>(observer=>{
      let refComponent:ComponentRef<any>|undefined = undefined;

      if (this.mainContainer){
        this.mainContainer.clear();
        refComponent = this.mainContainer.createComponent(componentType);
      }
      if (refComponent){
        Object.assign(refComponent.instance,values);
        observer.next(refComponent);
      }else{
        observer.error('Cannot create component');
      }
    })
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
