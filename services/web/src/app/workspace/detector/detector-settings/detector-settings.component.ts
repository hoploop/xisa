import { Component, Input } from '@angular/core';
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
  dismiss(){
    this.ctx.dismissModal();
  }
}
