import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Box } from '@train/image-annotator/image-annotator.component';

@Component({
  selector: 'app-image-labeler',
  standalone: false,
  templateUrl: './image-labeler.component.html',
  styleUrl: './image-labeler.component.scss'
})
export class ImageLabelerComponent {
  @Output() close = new EventEmitter<boolean>();
  @Input() box!:Box;
}
