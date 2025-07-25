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
  selected: number = 0;
  dismiss() {
    this.ctx.dismissModal();
  }


  ngOnInit(): void {

    this.loadResults();
  }

  loadResults(){
    this.loadImage('results.png');
    this.selected = 0;
  }

  loadCorrelogram(){
    this.loadImage('labels_correlogram.jpg');
    this.selected = 1;
  }

  loadF1Curve(){
    this.loadImage('F1_curve.png');
    this.selected = 2;
  }


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
