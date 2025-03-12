import { Component, Input } from '@angular/core';
import { BIconType } from '@constants/icons';

@Component({
  selector: 'app-b-icon',
  templateUrl: './b-icon.component.html',
  styleUrl: './b-icon.component.scss',
  standalone: false
})
export class BIconComponent {
  @Input() icon:string = BIconType.person;
}
