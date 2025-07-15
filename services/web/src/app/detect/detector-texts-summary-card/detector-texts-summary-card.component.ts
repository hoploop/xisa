import { Component, Input } from '@angular/core';
import { DetectText } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-texts-summary-card',
  standalone: false,
  templateUrl: './detector-texts-summary-card.component.html',
  styleUrl: './detector-texts-summary-card.component.scss',
})
export class DetectorTextsSummaryCardComponent extends BaseComponent {
  @Input() texts: DetectText[] = [];
}
