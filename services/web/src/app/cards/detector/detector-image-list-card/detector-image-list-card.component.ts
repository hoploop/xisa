import { Component, Input, OnInit } from '@angular/core';
import { Detector, DetectorImage, DetectorImageMode } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-detector-image-list-card',
  standalone: false,
  templateUrl: './detector-image-list-card.component.html',
  styleUrl: './detector-image-list-card.component.scss'
})
export class DetectorImageListCardComponent extends BaseComponent implements OnInit {

  DetectorImageMode = DetectorImageMode;
  @Input() detector!: Detector;
  images: DetectorImage[] = []
  total: number = 0;
  skip:number = 0;
  limit:number = 10;
  search: string = '';
  page:number = 1;

  ngOnInit(): void {
      this.load();
  }

  onChangeSearch(value:string){
    this.search = value;
    this.skip = 0;
    this.load();
  }

  onnPageChange(value:number){
    this.skip = (value-1) * this.limit;
    this.page = value;
    this.load();
  }

  back(){
    this.router.navigate(['detector/list',this.detector.project]);
  }

  remove(image:DetectorImage){
    if (!image._id) return;
    this.loading.next(this.ctx.translate.instant("detector.image.removing"));
    this.ctx.api.detector.detectorImageRemove(image._id).subscribe({
      next: (result)=>{
        this.loading.next(undefined);
        this.load();
      },
      error: (result)=>{
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      }
    })
  }

  update(){

  }

  load(){
    if (!this.detector._id) return;
    this.loading.next(this.ctx.translate.instant("detector.image.loadings"));
    this.error.next(undefined);
    this.ctx.api.detector.detectorImageList(this.detector._id,this.skip,this.limit).subscribe({
      next: (result)=>{
        this.total = result.total;
        this.images = result.images;
        this.loading.next(undefined);
      },
      error: (result)=>{
        this.error.next(result.error.detail);
        this.loading.next(undefined);
      }
    })
  }
}
