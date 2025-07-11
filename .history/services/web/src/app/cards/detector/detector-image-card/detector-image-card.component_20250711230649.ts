import { HttpHeaders, HttpResponse } from '@angular/common/http';
import { Component, Input } from '@angular/core';
import { DetectorImage } from '@api/index';
import { environment } from '@environments/environment';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-image-card',
  standalone: false,
  templateUrl: './detector-image-card.component.html',
  styleUrl: './detector-image-card.component.scss'
})
export class DetectorImageCardComponent extends BaseComponent {
  @Input() image!:DetectorImage;
  imageUrl?:string;

  loadImage(){

    let url = environment.detectorImageUrl+this.image.storage;
      const headers = new HttpHeaders()
    //.set('Range', `bytes=${startByte}-${endByte}`)
    .set('Authorization', 'Bearer ' + this.ctx.api.getToken() || '');

    this.http.get(url, {
      headers,
      responseType: 'blob',
      observe: 'response', // Observe the full response to get both headers and body
    }).subscribe(
      (response: HttpResponse<Blob>) => {
        if (response.body){
          this.imageUrl = URL.createObjectURL(response.body);
        }

      },
      (error) => {
        console.error('Error loading video:', error);
      });
    }
  }

