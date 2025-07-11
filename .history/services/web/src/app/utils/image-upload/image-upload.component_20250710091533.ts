import { Component, EventEmitter, Input, Output } from '@angular/core';
import { FAIconType } from '@constants/icons';
import { ContextService } from '@services/context.service';
import { BehaviorSubject, Observable } from 'rxjs';
import { v4 as uuid } from 'uuid';

@Component({
  selector: 'app-image-upload',
  standalone: false,
  templateUrl: './image-upload.component.html',
  styleUrl: './image-upload.component.scss',
})
export class ImageUploadComponent {
  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);

  imageIds: string[] = [];
  selectedFiles: Blob[] = [];
  @Output() uploaded = new EventEmitter<string>(); //.pdf,.txt or image/*
  @Input() accept = '*';
  @Input() multiple: boolean = false;
  FAIconType = FAIconType;

  constructor(private ctx: ContextService) {}

  onFileSelected(event: any) {
    this.selectedFiles = Array.from(event.target.files);
  }

  upload() {
    this.imageIds = [];
    this.selectedFiles.forEach((file) => {
      this.uploadImage(file);
    });
  }

  uploadImage(imageBlob: Blob) {
    /*
    let filename = uuid();
    const formData = new FormData();
    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant("train.image.uploading"));
    formData.append('file', imageBlob, filename); // Append Blob as file
    this.ctx.api.train.imageUpload(imageBlob).subscribe({
      next: (result) => {
        this.uploaded.next(result.id);
        this.imageIds.push(result.id);
        this.loading.next(undefined);
      },
      error: (result) => {
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      },
    });
  }*/
}
