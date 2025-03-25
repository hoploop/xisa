import { Component, Input } from '@angular/core';
import { DetectObject } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-objects-summary',
  standalone: false,
  templateUrl: './detector-objects-summary.component.html',
  styleUrl: './detector-objects-summary.component.scss'
})
export class DetectorObjectsSummaryComponent extends BaseComponent {
  @Input() objects: DetectObject[] = [];
}
