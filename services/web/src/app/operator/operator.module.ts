import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OperatorChatModalComponent } from './operator-chat-modal/operator-chat-modal.component';
import { UtilsModule } from '@utils/utils.module';
import { FormsModule } from '@angular/forms';
import { TranslateModule } from '@ngx-translate/core';



@NgModule({
  declarations: [
    OperatorChatModalComponent,
  ],
  imports: [
    CommonModule, UtilsModule,FormsModule,TranslateModule
  ],
  exports:[
    OperatorChatModalComponent,
  ]
})
export class OperatorModule { }
