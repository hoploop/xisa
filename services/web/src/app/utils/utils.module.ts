import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FaIconComponent } from './fa-icon/fa-icon.component';
import { BIconComponent } from './b-icon/b-icon.component';
import {
  FaIconLibrary,
  FontAwesomeModule,
} from '@fortawesome/angular-fontawesome';
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
import { NgIconComponent } from './ng-icon/ng-icon.component';
import { NgIconsModule } from '@ng-icons/core';
import { ImageAnnotatorComponent } from './image-annotator/image-annotator.component';
import { ImageUploadComponent } from './image-upload/image-upload.component';
import { ImageDisplayComponent } from './image-display/image-display.component';
import { ImageLabelerComponent } from './image-labeler/image-labeler.component';
import { TemplateCardContainerComponent } from './template-card-container/template-card-container.component';
import { DockScrollerComponent } from './dock-scroller/dock-scroller.component';
import { InfiniteProgressBarComponent } from './infinite-progress-bar/infinite-progress-bar.component';
import { RouteComponent } from './route/route.component';
import { SwitchComponent } from './switch/switch.component';
import { PaginationComponent } from './pagination/pagination.component';

@NgModule({
  declarations: [
    FaIconComponent,
    BIconComponent,
    LoaderComponent,
    SearchComponent,
    TagsEditorComponent,
    TemplateCardContainerComponent,
    BaseComponent,
    ModalComponent,
    ResizeListenerComponent,
    ResizeObserverDirective,
    NgIconComponent,
    ImageAnnotatorComponent,
    ImageUploadComponent,
    ImageDisplayComponent,
    ImageLabelerComponent,
    DockScrollerComponent,
    InfiniteProgressBarComponent,
    RouteComponent,
    SwitchComponent,
    PaginationComponent,
  ],
  imports: [
    CommonModule,
    FontAwesomeModule,
    FormsModule,
    TranslateModule,
    NgIconsModule
  ],
  exports: [
    FaIconComponent,
    BIconComponent,
    LoaderComponent,
    SearchComponent,
    TagsEditorComponent,
    ModalComponent,
    ResizeObserverDirective,
    ResizeListenerComponent,
    NgIconComponent,
    ImageAnnotatorComponent,
    ImageUploadComponent,
    ImageDisplayComponent,
    TemplateCardContainerComponent,
    ImageLabelerComponent,
    DockScrollerComponent,
    InfiniteProgressBarComponent,
    SwitchComponent,
    PaginationComponent
  ],
})
export class UtilsModule {
  constructor(library: FaIconLibrary, log: NGXLogger) {
    log.info('Loading icons');
    library.addIconPacks(fas, far);
  }
}
