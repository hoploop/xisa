import { Component, EventEmitter, Input, Output } from '@angular/core';
import { FAIconType, FAIconValues } from '@constants/icons';
import { AnimationProp, IconDefinition, RotateProp } from '@fortawesome/angular-fontawesome';

@Component({
  selector: 'app-fa-icon',
  templateUrl: './fa-icon.component.html',
  styleUrl: './fa-icon.component.scss',
  standalone: false
})
export class FaIconComponent {
  @Input() icon: FAIconType = FAIconType.xmark;
  @Input() animation: AnimationProp | undefined = undefined;
  @Input() rotate:RotateProp | undefined = undefined;
  @Output() click = new EventEmitter<any>();

  get realIcon(): IconDefinition {
    return FAIconValues[this.icon];
  }
}
