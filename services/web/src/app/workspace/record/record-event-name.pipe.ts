import { Pipe, PipeTransform } from '@angular/core';
import { KeyComboPressEventTypeEnum, KeyPressEventTypeEnum, KeyReleaseEventTypeEnum, MouseClickLeftEventTypeEnum, MouseClickRightEventTypeEnum, MousePressLeftEventTypeEnum, MousePressMiddleEventTypeEnum, MousePressRightEventTypeEnum, MouseReleaseLeftEventTypeEnum, MouseReleaseMiddleEventTypeEnum, MouseReleaseRightEventTypeEnum, MouseScrollEventTypeEnum } from '@api/index';
import { RecordEventListRecordId200ResponseInner } from '@api/model/record-event-list-record-id200-response-inner';
import { ContextService } from '@services/context.service';

@Pipe({
  name: 'recordEventName',
  standalone: false
})
export class RecordEventNamePipe implements PipeTransform {

  constructor(private ctx:ContextService){

  }

  transform(value: RecordEventListRecordId200ResponseInner|undefined, ...args: unknown[]): unknown {
    if (!value) return '';
    let pars = {x:0,y:0,dx:0,dy:0};

    switch (value.type){
      case KeyComboPressEventTypeEnum.KeyComboPress:
        return this.ctx.translate.instant("workspace.record.event.types.key_combo_press",{value:value.keys.toString()}); //keys
      case KeyPressEventTypeEnum.KeyPress:
        return this.ctx.translate.instant("workspace.record.event.types.key_press",{value:value.key}); //key
      case KeyReleaseEventTypeEnum.KeyRelease:
        return this.ctx.translate.instant("workspace.record.event.types.key_release",{value:value.key}); //key
      case MouseClickLeftEventTypeEnum.MouseClickLeft:
        if (value.position){
          pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
        }
        return this.ctx.translate.instant("workspace.record.event.types.mouse_click_left",pars); //position
      case MousePressLeftEventTypeEnum.MousePressLeft:
        if (value.position){
          pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
        }
        return this.ctx.translate.instant("workspace.record.event.types.mouse_press_left",pars);
      case MouseReleaseLeftEventTypeEnum.MouseReleaseLeft:
        if (value.position){
          pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
        }
        return this.ctx.translate.instant("workspace.record.event.types.mouse_release_left",pars);
      case MouseClickRightEventTypeEnum.MouseClickRight:
        if (value.position){
          pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
        }
        return this.ctx.translate.instant("workspace.record.event.types.mouse_click_right",pars);
      case MousePressMiddleEventTypeEnum.MousePressMiddle:
        if (value.position){
          pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
        }
        return this.ctx.translate.instant("workspace.record.event.types.mouse_press_middle",pars);
      case MousePressRightEventTypeEnum.MousePressRight:
        if (value.position){
          pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
        }
        return this.ctx.translate.instant("workspace.record.event.types.mouse_press_right",pars);
      case MouseReleaseRightEventTypeEnum.MouseReleaseRight:
        if (value.position){
          pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
        }
        return this.ctx.translate.instant("workspace.record.event.types.mouse_release_right",pars);
      case MouseReleaseMiddleEventTypeEnum.MouseReleaseMiddle:
        if (value.position){
          pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
        }
        return this.ctx.translate.instant("workspace.record.event.types.mouse_release_middle",pars);
      case  MouseScrollEventTypeEnum.MouseScroll:
        if (value.position && value.dx && value.dy){
          pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:Math.round(value.dx),dy:Math.round(value.dy)}
        }
        return this.ctx.translate.instant("workspace.record.event.types.mouse_scroll",pars);
      default:
        return '';
    }
  }

}
