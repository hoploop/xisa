import { Component, Input, OnInit } from '@angular/core';
import { RecordEventTypes } from '../record-event-types.enum';
import { FAIconType } from '@constants/icons';
import { Frame } from '../record-frame';

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

  ngOnInit(): void {
  }


}
