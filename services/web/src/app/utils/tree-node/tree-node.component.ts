import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { BaseComponent } from '@utils/base/base.component';

export interface TreeNode {
  id: number;
  label: string;
  children: TreeNode[];
  expanded: boolean;
  checked: boolean;
  selected?: boolean;
  visible?: boolean; // <-- used to hide/show
  highlight?: boolean; // <-- optional: used to style matching text
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
}
