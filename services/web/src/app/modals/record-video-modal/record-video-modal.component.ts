import { HttpHeaders, HttpResponse } from '@angular/common/http';
import { Component, ElementRef, Input, OnInit, ViewChild } from '@angular/core';
import { environment } from '@environments/environment';
import { BaseComponent } from '@utils/base/base.component';
import { Observable } from 'rxjs';
import { Record } from '@api/index';

@Component({
  selector: 'app-record-video-modal',
  standalone: false,
  templateUrl: './record-video-modal.component.html',
  styleUrl: './record-video-modal.component.scss',
})
export class RecordVideoModalComponent extends BaseComponent implements OnInit {
  @ViewChild('videoPlayer') videoPlayer?: ElementRef<HTMLVideoElement>;

  @Input() record!: Record;
  videoSize: number = 0; // Total video size in bytes
  chunkSize: number = 1024 * 1024; // 5MB per chunk, you can adjust this based on your needs
  currentByte: number = 0; // Start byte for video streaming

  ngOnInit(): void {
    this.loadVideo();
  }

  dismiss() {
    this.ctx.closeModal(undefined);
  }

  getVideoWithRange(
    url: string,
    startByte: number,
    endByte: number
  ): Observable<HttpResponse<Blob>> {
    const headers = new HttpHeaders()
      .set('Range', `bytes=${startByte}-${endByte}`)
      .set('Authorization', 'Bearer ' + this.ctx.api.getToken() || '');

    return this.http.get(url, {
      headers,
      responseType: 'blob',
      observe: 'response', // Observe the full response to get both headers and body
    });
  }

  handleVideoResponse(response: HttpResponse<Blob>) {
    // Get content-range header
    const contentRange = response.headers.get('Content-Range');

    if (contentRange) {
      const match = contentRange.match(/bytes (\d+)-(\d+)\/(\d+)/);
      if (match && this.videoPlayer && response.body) {
        this.currentByte = parseInt(match[2], 10) + 1; // Update the current byte position
        this.videoSize = parseInt(match[3], 10); // Total video size

        // Create URL for the video blob and set it as the source for the video player
        const videoUrl = URL.createObjectURL(response.body);
        this.videoPlayer.nativeElement.src = videoUrl;
        this.videoPlayer.nativeElement.load(); // Optional: Load video once chunk is loaded

        this.appendNextChunkIfNeeded();
      }
    }
  }

  appendNextChunkIfNeeded() {
    if (this.currentByte < this.videoSize) {
      this.loadVideo();
    }
  }

  loadVideo() {
    if (!this.record._id) return;
    this.getVideoWithRange(
      environment.videoUrl + this.record._id,
      this.currentByte,
      this.currentByte + this.chunkSize - 1
    ).subscribe(
      (response: HttpResponse<Blob>) => {
        this.handleVideoResponse(response);
      },
      (error) => {
        console.error('Error loading video:', error);
      }
    );
  }
}
