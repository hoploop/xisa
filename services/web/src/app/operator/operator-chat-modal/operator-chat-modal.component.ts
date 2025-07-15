import { Component } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';

export interface Message {
  role: 'user'|'system'|'error',
  text: string
}


@Component({
  selector: 'app-operator-chat-modal',
  standalone: false,
  templateUrl: './operator-chat-modal.component.html',
  styleUrl: './operator-chat-modal.component.scss'
})
export class OperatorChatModalComponent extends BaseComponent{
  message: string = '';
  messages: Message[] = [];

  dismiss(){
    this.ctx.dismissModal();
  }

  send(){
    this.messages.push({role:'user',text:this.message});
    this.ctx.api.operator.operatorAsk(this.message).subscribe({
      next: (result)=>{
        this.message = '';
        this.messages.push({role:'system',text:result});
      },
      error: (result)=>{
        this.messages.push({role:'error',text:result.error.detail});
      }
    })
  }
}
