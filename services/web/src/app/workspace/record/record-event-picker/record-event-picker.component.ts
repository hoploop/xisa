import { Component, Input, OnInit } from '@angular/core';
import { RecordEventTypes } from '../record-event-types.enum';
import { FAIconType } from '@constants/icons';
import { Frame } from '../record-frame';
import { MouseClickLeftEventTypeEnum, MousePressLeftEventTypeEnum, MouseReleaseLeftEventTypeEnum } from '@api/index';

@Component({
  selector: 'app-record-event-picker',
  standalone: false,
  templateUrl: './record-event-picker.component.html',
  styleUrl: './record-event-picker.component.scss'
})
export class RecordEventPickerComponent implements OnInit {
  @Input() frame!: Frame;
  FAIconType = FAIconType;
  RecordEventTypes = RecordEventTypes;
  name: string = '';

  ngOnInit(): void {
      this.name = this.renderEventName();
  }

  renderEventName(): string {

    if (!this.frame.event) return '';
    console.log(this.frame.event.type);
    switch (this.frame.event.type){
      case MouseClickLeftEventTypeEnum.MouseClickLeft:
          return 'Mouse click left'
      case MousePressLeftEventTypeEnum.MousePressLeft:
        return 'Mouse press Left';
      case MouseReleaseLeftEventTypeEnum.MouseReleaseLeft:
        return 'Mouse release left';
      default:
        return '';
    }
  }
}
