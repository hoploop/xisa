import { Component, Input, OnInit } from '@angular/core';
import { RecordEventTypes } from '../record-event-types.enum';
import { FAIconType } from '@constants/icons';
import { Frame } from '../record-frame';
import { environment } from '@environments/environment';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { BaseComponent } from '@utils/base/base.component';
import { ContextService } from '@services/context.service';
import { NGXLogger } from 'ngx-logger';

@Component({
  selector: 'app-record-event-picker',
  standalone: false,
  templateUrl: './record-event-picker.component.html',
  styleUrl: './record-event-picker.component.scss'
})
export class RecordEventPickerComponent extends BaseComponent implements OnInit {
  @Input() frame!: Frame;
  RecordEventTypes = RecordEventTypes;
  imageUrl?:string;

  constructor(protected override ctx:ContextService,protected override  log: NGXLogger,private http: HttpClient){
    super(ctx,log)
  }

  ngOnInit(): void {

    this.loadUrlImage(environment.imageThumbnailUrl +
      this.frame.lesson.record +
      '/' +
      this.frame.count.toString());
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
