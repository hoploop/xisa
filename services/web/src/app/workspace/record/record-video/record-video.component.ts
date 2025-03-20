import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Component, ElementRef, Input, OnInit, ViewChild } from '@angular/core';
import { environment } from '@environments/environment';
import { ContextService } from '@services/context.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-record-video',
  standalone: false,
  templateUrl: './record-video.component.html',
  styleUrl: './record-video.component.scss'
})
export class RecordVideoComponent implements OnInit{
  @ViewChild('videoPlayer') videoPlayer?: ElementRef<HTMLVideoElement>;

  @Input() recordId!:string;
  videoSize: number = 0; // Total video size in bytes
  chunkSize: number = 1024 * 1024; // 5MB per chunk, you can adjust this based on your needs
  currentByte: number = 0; // Start byte for video streaming

  constructor(private ctx:ContextService,private http: HttpClient){

  }

  ngOnInit(): void {
    this.loadVideo();
  }


  getVideoWithRange(url: string, startByte: number, endByte: number): Observable<HttpResponse<Blob>> {
    const headers = new HttpHeaders().set('Range', `bytes=${startByte}-${endByte}`).set('Authorization','Bearer '+this.ctx.api.getToken() ||'');

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

    this.getVideoWithRange(environment.videoUrl+this.recordId, this.currentByte, this.currentByte + this.chunkSize - 1).subscribe(
      (response: HttpResponse<Blob>) => {
        this.handleVideoResponse(response);
      },
      (error) => {
        console.error('Error loading video:', error);
      }
    );

  }
}
