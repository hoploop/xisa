import { Component, EventEmitter, Input, Output } from '@angular/core';
import { FAIconType } from '@constants/icons';

@Component({
  selector: 'app-tags-editor',
  standalone: false,
  templateUrl: './tags-editor.component.html',
  styleUrl: './tags-editor.component.scss'
})
export class TagsEditorComponent {
  @Input() tags:string[] = [];
  @Output() tagsChange = new EventEmitter<string[]>();
  value:string = '';
  FAIconType = FAIconType;

  onEnter(event:Event){
    if (this.tags.indexOf(this.value)!=-1){
      event.preventDefault();
      return;
    }
    this.tags.push(this.value);
    this.tagsChange.next(this.tags);
    this.value = '';
  }

  remove(value:string){
    let found = this.tags.indexOf(value);
    if (found!=-1){
      this.tags.splice(found,1);
      this.tagsChange.next(this.tags);
    }
  }

  onBackspace(event:Event){
    if (this.tags.length == 0 || this.value.length >0){
      return;
    }else{
      event.preventDefault();
      this.tags.splice(this.tags.length-1,1);
      this.tagsChange.next(this.tags);
    }

  }
}
