import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-switch',
  standalone: false,
  templateUrl: './switch.component.html',
  styleUrl: './switch.component.scss'
})
export class SwitchComponent {
  @Input() value:boolean = false;
  @Output() valueChange = new EventEmitter<boolean>();
  @Input() textOn?:string;
  @Input() textOff?:string;
  @Input() small:boolean = false;
  @Input() large:boolean = false;

  onChange(value:boolean) {

    this.value = value;
    this.valueChange.next(this.value);
  }
}
