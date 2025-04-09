import { Component, Input } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-infinite-progress-bar',
  standalone: false,
  templateUrl: './infinite-progress-bar.component.html',
  styleUrl: './infinite-progress-bar.component.scss'
})
export class InfiniteProgressBarComponent {
  @Input() loading = new BehaviorSubject<boolean>(false);
}
