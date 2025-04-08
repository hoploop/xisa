import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TranslateModule } from '@ngx-translate/core';
import { TemplateCardContainerComponent } from './template-card-container/template-card-container.component';



@NgModule({
  declarations: [
    TemplateCardContainerComponent
  ],
  imports: [
    CommonModule,
    TranslateModule
  ],
  exports : [
    TemplateCardContainerComponent
  ]
})
export class TemplatesModule { }
