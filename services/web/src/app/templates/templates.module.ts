import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TemplateMenuComponent } from './template-menu/template-menu.component';
import { TranslateModule } from '@ngx-translate/core';
import { TemplateCardContainerComponent } from './template-card-container/template-card-container.component';



@NgModule({
  declarations: [
    TemplateMenuComponent,
    TemplateCardContainerComponent
  ],
  imports: [
    CommonModule,
    TranslateModule
  ],
  exports : [
    TemplateMenuComponent,
    TemplateCardContainerComponent
  ]
})
export class TemplatesModule { }
