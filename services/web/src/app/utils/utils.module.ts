import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FaIconComponent } from './fa-icon/fa-icon.component';
import { BIconComponent } from './b-icon/b-icon.component';
import { FaIconLibrary, FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { fas } from '@fortawesome/free-solid-svg-icons';
import { far } from '@fortawesome/free-regular-svg-icons';
import { LoaderComponent } from './loader/loader.component';
import { SearchComponent } from './search/search.component';
import { FormsModule } from '@angular/forms';
import { TranslateModule } from '@ngx-translate/core';
import { TagsEditorComponent } from './tags-editor/tags-editor.component';
import { BaseComponent } from './base/base.component';
import { ModalComponent } from './modal/modal.component';
import { ResizeObserverDirective } from './resize-observer.directive';
import { ResizeListenerComponent } from './resize-listener/resize-listener.component';
import { NGXLogger } from 'ngx-logger';



@NgModule({
  declarations: [
    FaIconComponent,
    BIconComponent,
    LoaderComponent,
    SearchComponent,
    TagsEditorComponent,
    BaseComponent,
    ModalComponent,
    ResizeListenerComponent,
    ResizeObserverDirective,

  ],
  imports: [
    CommonModule,
    FontAwesomeModule,
    FormsModule,
    TranslateModule
  ],
  exports: [
    FaIconComponent,
    BIconComponent,
    LoaderComponent,
    SearchComponent,
    TagsEditorComponent,
    ModalComponent,
    ResizeObserverDirective,
    ResizeListenerComponent
  ]
})
export class UtilsModule {
  constructor(library: FaIconLibrary, log: NGXLogger) {
    log.info('Loading icons');
    library.addIconPacks(fas, far);
}
}
