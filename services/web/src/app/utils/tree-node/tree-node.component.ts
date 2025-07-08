import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { BIconType, FAIconType, NGIconType } from '@constants/icons';
import { BaseComponent } from '@utils/base/base.component';
import { Observable } from 'rxjs';

export type TreeNodeIcon = FAIconType | BIconType;

export interface TreeNode {
  id: number;
  label: string;
  children: TreeNode[];
  expanded: boolean;
  checked: boolean;
  selected?: boolean;
  visible?: boolean; // <-- used to hide/show
  highlight?: boolean; // <-- optional: used to style matching text
  faIcon?: FAIconType;
  bIcon?: BIconType;
  ngIcon?: NGIconType;
  callback?: Observable<any>
}

@Component({
  selector: 'app-tree-node',
  standalone: false,
  templateUrl: './tree-node.component.html',
  styleUrl: './tree-node.component.scss',
})
export class TreeNodeComponent extends BaseComponent implements OnInit {
  @Input() nesting: number = 0;
  @Input() selected?: TreeNode;
  @Output() selectedChange = new EventEmitter<TreeNode>();

  @Input() node!: TreeNode;

  ngOnInit(): void {}

  toggle() {
    this.node.expanded = !this.node.expanded;
  }

  get isSelected(): boolean {
    return this.selected != undefined && this.selected.id == this.node.id;
  }

  onSelect(){
    this.selected=this.node;
    this.selectedChange.next(this.node);
    if (this.node.callback){

      this.node.callback.subscribe(result=>{

      })
    }
  }
}
