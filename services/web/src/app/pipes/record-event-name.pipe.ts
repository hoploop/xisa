import { Pipe, PipeTransform } from '@angular/core';
import { KeyComboPressEventTypeEnum, KeyPressEventTypeEnum, KeyReleaseEventTypeEnum, KeyTypeEventTypeEnum, MouseButton, MouseClickEventTypeEnum,MouseDoubleClickEventTypeEnum, MousePressEventTypeEnum, MouseReleaseEventTypeEnum, MouseScrollEventTypeEnum, RecorderEventList200ResponseInner } from '@api/index';
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
    let pars = {x:0,y:0,dx:0,dy:0,value:''};

    switch (value.type){
      case KeyComboPressEventTypeEnum.KeyComboPress:
        pars['value']=value.keys.toString();
        if (value.position){
          pars['x'] = Math.round(value.position[0]);
          pars['y'] = Math.round(value.position[1]);
        }
        return this.ctx.translate.instant("recorder.event.types.key_combo_press",pars); //keys
      case KeyPressEventTypeEnum.KeyPress:
        pars['value']=value.key;
        if (value.position){
          pars['x'] = Math.round(value.position[0]);
          pars['y'] = Math.round(value.position[1]);
        }
        return this.ctx.translate.instant("recorder.event.types.key_press",pars); //key
        case KeyTypeEventTypeEnum.KeyType:
          pars['value']=value.key;
        if (value.position){
          pars['x'] = Math.round(value.position[0]);
          pars['y'] = Math.round(value.position[1]);
        }
          return this.ctx.translate.instant("recorder.event.types.key_type",pars); //key
      case KeyReleaseEventTypeEnum.KeyRelease:
        pars['value']=value.key;
        if (value.position){
          pars['x'] = Math.round(value.position[0]);
          pars['y'] = Math.round(value.position[1]);
        }
        return this.ctx.translate.instant("recorder.event.types.key_release",pars); //key
      case MouseClickEventTypeEnum.MouseClick:
        if (value.position){
          pars['x'] = Math.round(value.position[0]);
          pars['y'] = Math.round(value.position[1]);
        }
        if (value.button == MouseButton.Left){
          return this.ctx.translate.instant("recorder.event.types.mouse_click_left",pars); //position
        }
        else if (value.button == MouseButton.Middle){
          return this.ctx.translate.instant("recorder.event.types.mouse_click_middle",pars); //position
        }
        else {
          return this.ctx.translate.instant("recorder.event.types.mouse_click_right",pars); //position
        }

      case MouseDoubleClickEventTypeEnum.MouseDoubleClick:
          if (value.position){
            pars['x'] = Math.round(value.position[0]);
            pars['y'] = Math.round(value.position[1]);
          }
          if (value.button == MouseButton.Left){
            return this.ctx.translate.instant("recorder.event.types.mouse_double_click_left",pars); //position
          }
          else if (value.button == MouseButton.Middle){
            return this.ctx.translate.instant("recorder.event.types.mouse_double_click_middle",pars); //position
          }
          else {
            return this.ctx.translate.instant("recorder.event.types.mouse_double_click_right",pars); //position
          }

      case MousePressEventTypeEnum.MousePress:
        if (value.position){
          pars['x'] = Math.round(value.position[0]);
          pars['y'] = Math.round(value.position[1]);
        }
        if (value.button == MouseButton.Left){
          return this.ctx.translate.instant("recorder.event.types.mouse_press_left",pars);
        }
        else if (value.button == MouseButton.Middle){
          return this.ctx.translate.instant("recorder.event.types.mouse_press_middle",pars);
        }
        else {
          return this.ctx.translate.instant("recorder.event.types.mouse_press_right",pars);
        }

      case MouseReleaseEventTypeEnum.MouseRelease:
        if (value.position){
          pars['x'] = Math.round(value.position[0]);
          pars['y'] = Math.round(value.position[1]);
        }
        if (value.button == MouseButton.Left){
          return this.ctx.translate.instant("recorder.event.types.mouse_release_left",pars);
        }
        else if (value.button == MouseButton.Middle){
          return this.ctx.translate.instant("recorder.event.types.mouse_release_middle",pars);
        }
        else {
          return this.ctx.translate.instant("recorder.event.types.mouse_release_right",pars);
        }

      case  MouseScrollEventTypeEnum.MouseScroll:
        if (value.position && value.dx && value.dy){
          pars['x'] = Math.round(value.position[0]);
          pars['y'] = Math.round(value.position[1]);
          pars['dx'] = Math.round(value.dx);
          pars['dy'] = Math.round(value.dy);
        }
        return this.ctx.translate.instant("recorder.event.types.mouse_scroll",pars);
      default:
        return '';
    }
  }

}
