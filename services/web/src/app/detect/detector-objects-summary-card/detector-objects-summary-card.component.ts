import { Component, Input } from '@angular/core';
import { DetectObject } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-objects-summary-card',
  standalone: false,
  templateUrl: './detector-objects-summary-card.component.html',
  styleUrl: './detector-objects-summary-card.component.scss'
})
export class DetectorObjectsSummaryCardComponent  extends BaseComponent {
  @Input() objects: DetectObject[] = [];
}
