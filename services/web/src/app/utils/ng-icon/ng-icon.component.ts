import { Component, Input } from '@angular/core';
import { NGIconType } from '@constants/icons';

@Component({
  selector: 'app-ng-icon',
  standalone: false,
  templateUrl: './ng-icon.component.html',
  styleUrl: './ng-icon.component.scss'
})
export class NgIconComponent {
  @Input() icon!: NGIconType;




}
