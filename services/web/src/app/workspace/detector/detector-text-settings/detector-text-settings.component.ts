import { Component, EventEmitter, Input, Output } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-text-settings',
  standalone: false,
  templateUrl: './detector-text-settings.component.html',
  styleUrl: './detector-text-settings.component.scss'
})
export class DetectorTextSettingsComponent extends BaseComponent{
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
