import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TemplateCardContainerComponent } from './template-card-container/template-card-container.component';



@NgModule({
  declarations: [
    TemplateCardContainerComponent
  ],
  imports: [
    CommonModule
  ],
  exports : [
    TemplateCardContainerComponent
  ]
})
export class TemplatesModule { }
