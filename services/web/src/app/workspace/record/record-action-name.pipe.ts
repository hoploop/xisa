import { Pipe, PipeTransform } from '@angular/core';
import { Action, KeyComboPressEventTypeEnum, KeyPressEventTypeEnum, KeyReleaseEventTypeEnum, MouseClickLeftEventTypeEnum, MouseClickRightEventTypeEnum, MousePressLeftEventTypeEnum, MousePressMiddleEventTypeEnum, MousePressRightEventTypeEnum, MouseReleaseLeftEventTypeEnum, MouseReleaseMiddleEventTypeEnum, MouseReleaseRightEventTypeEnum, MouseScrollEventTypeEnum, ResponseRecordereventload } from '@api/index';
import { ContextService } from '@services/context.service';
import { Observable } from 'rxjs';

@Pipe({
  name: 'recordActionName',
  standalone: false
})
export class RecordActionNamePipe implements PipeTransform {

  constructor(private ctx:ContextService){

  }

  transform(value: Action, ...args: unknown[]): Observable<string> {
    return new Observable<string>(observer=>{
      this.ctx.api.recorder.recorderEventLoad(value.event).subscribe({
        next: (event)=>{
          let firstPart = this.renderFirstPart(event);
          let secondPart = this.renderSecondPart(value);
          observer.next(firstPart+' '+secondPart);
        },
        error: (result)=>{
          observer.error(result);
        }
      })


    });
  }

  renderSecondPart(action:Action){

    if (action.by_label && action.by_order &&  action.by_order.length == 0){
      return this.ctx.translate.instant('workspace.record.action.by_class',{'class':action.by_label});
    }else if (action.by_label && action.by_order && action.by_order.length == 1){
      return this.ctx.translate.instant('workspace.record.action.by_classes_order_1',{'class':action.by_label,'order':action.by_order[0]});
    }else if (action.by_label && action.by_order && action.by_order.length == 2){
      return this.ctx.translate.instant('workspace.record.action.by_classes_order_2',{'class':action.by_label,'row':action.by_order[0],'col':action.by_order[1]});
    } else if (action.by_text && action.by_order && action.by_order.length == 0){
      return this.ctx.translate.instant('workspace.record.action.by_text',{'text':action.by_text});
    } else if (action.by_text && action.by_order && action.by_order.length == 1){
      return this.ctx.translate.instant('workspace.record.action.by_texts_order_1',{'text':action.by_text,'order':action.by_order[0]});
    } else if (action.by_text && action.by_order && action.by_order.length == 2){
      return this.ctx.translate.instant('workspace.record.action.by_texts_order_2',{'text':action.by_text,'row':action.by_order[0],'col':action.by_order[1]});
    } else if (action.by_regex && action.by_order && action.by_order.length == 0){
      return this.ctx.translate.instant('workspace.record.action.by_regex',{'regex':action.by_regex});
    } else if (action.by_regex && action.by_order && action.by_order.length == 1){
      return this.ctx.translate.instant('workspace.record.action.by_regex_order_1',{'regex':action.by_regex,'order':action.by_order[0]});
    } else if (action.by_regex && action.by_order && action.by_order.length == 2){
      return this.ctx.translate.instant('workspace.record.action.by_regex_order_2',{'regex':action.by_regex,'row':action.by_order[0],'col':action.by_order[1]});
    }
  }

  renderFirstPart(value:ResponseRecordereventload){
    let pars = {x:0,y:0,dx:0,dy:0};

        switch (value.type){
          case KeyComboPressEventTypeEnum.KeyComboPress:
            return this.ctx.translate.instant("workspace.record.action.types.key_combo_press",{value:value.keys.toString()}); //keys
          case KeyPressEventTypeEnum.KeyPress:
            return this.ctx.translate.instant("workspace.record.action.types.key_press",{value:value.key}); //key
          case KeyReleaseEventTypeEnum.KeyRelease:
            return this.ctx.translate.instant("workspace.record.action.types.key_release",{value:value.key}); //key
          case MouseClickLeftEventTypeEnum.MouseClickLeft:
            if (value.position){
              pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
            }
            return this.ctx.translate.instant("workspace.record.action.types.mouse_click_left",pars); //position
          case MousePressLeftEventTypeEnum.MousePressLeft:
            if (value.position){
              pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
            }
            return this.ctx.translate.instant("workspace.record.action.types.mouse_press_left",pars);
          case MouseReleaseLeftEventTypeEnum.MouseReleaseLeft:
            if (value.position){
              pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
            }
            return this.ctx.translate.instant("workspace.record.action.types.mouse_release_left",pars);
          case MouseClickRightEventTypeEnum.MouseClickRight:
            if (value.position){
              pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
            }
            return this.ctx.translate.instant("workspace.record.action.types.mouse_click_right",pars);
          case MousePressMiddleEventTypeEnum.MousePressMiddle:
            if (value.position){
              pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
            }
            return this.ctx.translate.instant("workspace.record.action.types.mouse_press_middle",pars);
          case MousePressRightEventTypeEnum.MousePressRight:
            if (value.position){
              pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
            }
            return this.ctx.translate.instant("workspace.record.action.types.mouse_press_right",pars);
          case MouseReleaseRightEventTypeEnum.MouseReleaseRight:
            if (value.position){
              pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
            }
            return this.ctx.translate.instant("workspace.record.action.types.mouse_release_right",pars);
          case MouseReleaseMiddleEventTypeEnum.MouseReleaseMiddle:
            if (value.position){
              pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
            }
            return this.ctx.translate.instant("workspace.record.action.types.mouse_release_middle",pars);
          case  MouseScrollEventTypeEnum.MouseScroll:
            if (value.position && value.dx && value.dy){
              pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:Math.round(value.dx),dy:Math.round(value.dy)}
            }
            return this.ctx.translate.instant("workspace.record.action.types.mouse_scroll",pars);
          default:
            return '';
        }
  }


}
