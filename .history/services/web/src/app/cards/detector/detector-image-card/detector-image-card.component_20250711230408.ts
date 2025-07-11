import { Component, Input } from '@angular/core';
import { DetectorImage } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-image-card',
  standalone: false,
  templateUrl: './detector-image-card.component.html',
  styleUrl: './detector-image-card.component.scss'
})
export class DetectorImageCardComponent extends BaseComponent {
  @Input() image!:DetectorImage;

  loadImage(name:string){
    if (this.session.results){
      this.url = environment.resultsUrl+this.session.results+'/'+name;
       const headers = new HttpHeaders()
      //.set('Range', `bytes=${startByte}-${endByte}`)
      .set('Authorization', 'Bearer ' + this.ctx.api.getToken() || '');

    this.http.get(this.url, {
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
}
