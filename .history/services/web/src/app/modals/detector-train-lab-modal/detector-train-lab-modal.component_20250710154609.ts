import { HttpHeaders, HttpResponse } from '@angular/common/http';
import { Component, Input, OnInit } from '@angular/core';
import { TrainSession } from '@api/index';
import { environment } from '@environments/environment';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-train-lab-modal',
  standalone: false,
  templateUrl: './detector-train-lab-modal.component.html',
  styleUrl: './detector-train-lab-modal.component.scss',
})
export class DetectorTrainLabModalComponent extends BaseComponent implements OnInit {
  @Input() session!: TrainSession;
  url?:string = undefined;
  imageUrl?:string;
  dismiss() {
    this.ctx.dismissModal();
  }

  ngOnInit(): void {
    if (this.session.results){
      this.url = environment.resultsUrl+this.session.results+'/results.png';
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
