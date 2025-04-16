import { Component, Input } from '@angular/core';
import { BIconType, FAIconType, NGIconType } from '@constants/icons';

@Component({
  selector: 'app-icon',
  standalone: false,
  templateUrl: './icon.component.html',
  styleUrl: './icon.component.scss'
})
export class IconComponent {
  @Input() faIcon?: FAIconType;
  @Input() ngIcon?: NGIconType;
  @Input() bIcon?: BIconType;
}
