import { Component, Input } from '@angular/core';
import { BIconType, FAIconType } from '@constants/icons';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-loader',
  standalone: false,
  templateUrl: './loader.component.html',
  styleUrl: './loader.component.scss',
})
export class LoaderComponent {
  FAIconType = FAIconType;
  BIconType = BIconType;
  @Input() cardFooter: boolean = false;
  @Input() modalFooter: boolean = false;
  @Input() loading!: BehaviorSubject<string | undefined>;
  @Input() error!: BehaviorSubject<string | undefined>;
}
