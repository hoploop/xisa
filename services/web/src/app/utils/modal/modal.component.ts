import { Component, Input } from '@angular/core';
import { FAIconType } from '@constants/icons';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-modal',
  standalone: false,
  templateUrl: './modal.component.html',
  styleUrl: './modal.component.scss'
})
export class ModalComponent {
  FAIconType = FAIconType;
  @Input() loading = new BehaviorSubject<string|undefined>(undefined);
  @Input() error = new BehaviorSubject<string|undefined>(undefined);
  @Input() showBody: boolean = true;
  @Input() showHeader: boolean = true;
  constructor(private ctx:ContextService){

  }

  dismiss(){
    this.ctx.dismissModal();
  }
}
