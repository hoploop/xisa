import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Detector } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-settings',
  standalone: false,
  templateUrl: './detector-settings.component.html',
  styleUrl: './detector-settings.component.scss'
})
export class DetectorSettingsComponent extends BaseComponent {
  @Input() detector!:Detector;
  @Input() confidence: number = 0.1;
  @Output() confidenceChange = new EventEmitter<number>();
  dismiss(){
    this.ctx.dismissModal();
  }
  updateConfidence(value:number){
    this.confidence = value;
    this.confidenceChange.next(value);
  }

  accept(){
    this.ctx.closeModal(this.confidence);
  }
}
