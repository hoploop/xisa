import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImageAnnotatorComponent } from './image-annotator/image-annotator.component';
import { ImageUploadComponent } from './image-upload/image-upload.component';
import { UtilsModule } from '@utils/utils.module';
import { ImageDisplayComponent } from './image-display/image-display.component';
import { ImageLabelerComponent } from './image-labeler/image-labeler.component';



@NgModule({
  declarations: [
    ImageAnnotatorComponent,
    ImageUploadComponent,
    ImageDisplayComponent,
    ImageLabelerComponent
  ],
  imports: [
    CommonModule,
    UtilsModule
  ],
  exports: [
    ImageAnnotatorComponent,
    ImageUploadComponent,
    ImageDisplayComponent
  ]
})
export class TrainModule { }
