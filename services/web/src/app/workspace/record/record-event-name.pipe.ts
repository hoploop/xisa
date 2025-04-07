import { Pipe, PipeTransform } from '@angular/core';
import { KeyComboPressEventTypeEnum, KeyPressEventTypeEnum, KeyReleaseEventTypeEnum, MouseButton, MouseClickEventTypeEnum,MouseDoubleClickEventTypeEnum, MousePressEventTypeEnum, MouseReleaseEventTypeEnum, MouseScrollEventTypeEnum, RecorderEventList200ResponseInner } from '@api/index';
import { ContextService } from '@services/context.service';

@Pipe({
  name: 'recordEventName',
  standalone: false
})
export class RecordEventNamePipe implements PipeTransform {

  constructor(private ctx:ContextService){

  }

  transform(value: RecorderEventList200ResponseInner|undefined, ...args: unknown[]): unknown {
    if (!value) return '';
    let pars = {x:0,y:0,dx:0,dy:0};

    switch (value.type){
      case KeyComboPressEventTypeEnum.KeyComboPress:
        return this.ctx.translate.instant("workspace.record.event.types.key_combo_press",{value:value.keys.toString()}); //keys
      case KeyPressEventTypeEnum.KeyPress:
        return this.ctx.translate.instant("workspace.record.event.types.key_press",{value:value.key}); //key
      case KeyReleaseEventTypeEnum.KeyRelease:
        return this.ctx.translate.instant("workspace.record.event.types.key_release",{value:value.key}); //key
      case MouseClickEventTypeEnum.MouseClick:
        if (value.position){
          pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
        }
        if (value.button == MouseButton.Left){
          return this.ctx.translate.instant("workspace.record.event.types.mouse_click_left",pars); //position
        }
        else if (value.button == MouseButton.Middle){
          return this.ctx.translate.instant("workspace.record.event.types.mouse_click_middle",pars); //position
        }
        else {
          return this.ctx.translate.instant("workspace.record.event.types.mouse_click_right",pars); //position
        }

      case MouseDoubleClickEventTypeEnum.MouseDoubleClick:
          if (value.position){
            pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
          }
          if (value.button == MouseButton.Left){
            return this.ctx.translate.instant("workspace.record.event.types.mouse_double_click_left",pars); //position
          }
          else if (value.button == MouseButton.Middle){
            return this.ctx.translate.instant("workspace.record.event.types.mouse_double_click_middle",pars); //position
          }
          else {
            return this.ctx.translate.instant("workspace.record.event.types.mouse_double_click_right",pars); //position
          }

      case MousePressEventTypeEnum.MousePress:
        if (value.position){
          pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
        }
        if (value.button == MouseButton.Left){
          return this.ctx.translate.instant("workspace.record.event.types.mouse_press_left",pars);
        }
        else if (value.button == MouseButton.Middle){
          return this.ctx.translate.instant("workspace.record.event.types.mouse_press_middle",pars);
        }
        else {
          return this.ctx.translate.instant("workspace.record.event.types.mouse_press_right",pars);
        }

      case MouseReleaseEventTypeEnum.MouseRelease:
        if (value.position){
          pars = {x:Math.round(value.position[0]),y:Math.round(value.position[1]),dx:0,dy:0}
        }
        if (value.button == MouseButton.Left){
          return this.ctx.translate.instant("workspace.record.event.types.mouse_release_left",pars);
        }
        else if (value.button == MouseButton.Middle){
          return this.ctx.translate.instant("workspace.record.event.types.mouse_release_middle",pars);
        }
        else {
          return this.ctx.translate.instant("workspace.record.event.types.mouse_release_right",pars);
        }

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
