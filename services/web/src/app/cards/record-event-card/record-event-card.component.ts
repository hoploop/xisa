import { HttpHeaders, HttpResponse } from '@angular/common/http';
import { Component, Input, OnInit } from '@angular/core';
import { environment } from '@environments/environment';
import { BaseComponent } from '@utils/base/base.component';
import { RecordEventTypes } from '@models/record-event-types.enum';
import { Frame } from '@models/record-frame';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-record-event-card',
  standalone: false,
  templateUrl: './record-event-card.component.html',
  styleUrl: './record-event-card.component.scss',
})
export class RecordEventCardComponent extends BaseComponent implements OnInit {
  @Input() frame!: Frame;
  RecordEventTypes = RecordEventTypes;
  imageUrl?: string;

  ngOnInit(): void {
    this.loadUrlImage(
      environment.imageThumbnailUrl +
        this.frame.lesson.record +
        '/' +
        this.frame.count.toString()
    );
  }

  // Method to get image as Blob from FastAPI
  getUrlImage(url: string): Observable<HttpResponse<Blob>> {
    const headers = new HttpHeaders().set(
      'Authorization',
      'Bearer ' + this.ctx.api.getToken() || ''
    );

    return this.http.get(url, {
      headers,
      responseType: 'blob', // This ensures the response is a Blob
      observe: 'response', // Observe the full response to get both headers and body
    });
  }

  handleLoadUrlImage(response: HttpResponse<Blob>) {
    if (response.body) {
      this.imageUrl = URL.createObjectURL(response.body);
    }
  }

  loadUrlImage(url: string) {
    this.getUrlImage(url).subscribe(
      (response: HttpResponse<Blob>) => {
        this.handleLoadUrlImage(response);
      },
      (error) => {
        console.error('Error loading image:', error);
      }
    );
  }
}
