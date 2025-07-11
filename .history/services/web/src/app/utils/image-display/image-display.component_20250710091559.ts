import { AfterViewInit, Component, Input } from '@angular/core';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';
import { FAIconType } from '@constants/icons';

@Component({
  selector: 'app-image-display',
  standalone: false,
  templateUrl: './image-display.component.html',
  styleUrl: './image-display.component.scss',
})
export class ImageDisplayComponent implements AfterViewInit{
  @Input() fileId?:string;
  @Input() width: number = 300;
  imageUrl: string | null = null; // Store image URL
  loading = new BehaviorSubject<string|undefined>(undefined);
  error = new BehaviorSubject<string|undefined>(undefined);
  FAIconType = FAIconType;

  constructor(private ctx: ContextService) {}

  ngAfterViewInit(): void {
    setTimeout(()=>{
      this.retrieve();
    })

  }

  retrieve() {
    /*
    if (!this.fileId) return;
    console.log('Loading image blob');
    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant("train.image.downloading"));
    this.ctx.api.train.imageDownload(this.fileId).subscribe({
      next: (result) => {
        this.loading.next(undefined);
        //const blobUrl = URL.createObjectURL(result);
        //console.log('Loaded image blob');
        this.imageUrl = result; // Set URL for <img> tag
      },
      error: (result) => {
        console.log(result);
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
  });
  */
  }
}
