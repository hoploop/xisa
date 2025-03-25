import { Component, Input } from '@angular/core';
import { DetectText } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-texts-summary',
  standalone: false,
  templateUrl: './detector-texts-summary.component.html',
  styleUrl: './detector-texts-summary.component.scss'
})
export class DetectorTextsSummaryComponent extends BaseComponent {
  @Input() texts: DetectText[] = [];
}
