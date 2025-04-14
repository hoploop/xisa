import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { debounceTime, Subject } from 'rxjs';
import { BaseComponent } from '../base/base.component';
import { TreeNode } from '@utils/tree-node/tree-node.component';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-treeview',
  standalone: false,
  templateUrl: './treeview.component.html',
  styleUrl: './treeview.component.scss',
})
export class TreeviewComponent implements OnInit {
  firstMatchId: string | null = null;
  searchControl = new FormControl('');
  @Input() selected?: TreeNode;
  @Output() selectedChange = new EventEmitter<TreeNode>();


  ngOnInit() {

      this.searchControl.valueChanges
      .pipe(debounceTime(300))
      .subscribe(term => {
        const cleanTerm = (term || '').toLowerCase();

        this.firstMatchId = null;
        this.nodes.forEach(node => this.applySearch(node, cleanTerm));

        // Wait for DOM to update (next tick)
        setTimeout(() => {
          if (this.firstMatchId) {
            const el = document.getElementById(this.firstMatchId);
            el?.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
        }, 0);
      });
  }

  @Input() nodes: TreeNode[] = [
    {
      id: 1,
      label: 'sample',
      children: [
        {
          id: 2,
          label: 'Sample bis',
          children: [],
          expanded: false,
          checked: false,
        },
        {
          id: 3,
          label: 'Sample bis 2',
          children: [],
          expanded: false,
          checked: false,
        },
        {
          id: 4,
          label: 'Sample bis 3',
          children: [],
          expanded: false,
          checked: false,
        },
        {
          id: 5,
          label: 'Sample bis 4',
          children: [
            {
              id: 6,
              label: 'Sample bis 3',
              children: [],
              expanded: false,
              checked: false,
            },
            {
              id: 7,
              label: 'Sample bis 4',
              children: [],
              expanded: false,
              checked: false,
            },
            {
              id: 8,
              label: 'Sample bis 5',
              children: [],
              expanded: false,
              checked: false,
            },
          ],
          expanded: false,
          checked: false,
        },
        {
          id: 9,
          label: 'Sample bis 5',
          children: [],
          expanded: false,
          checked: false,
        },
      ],
      expanded: false,
      checked: false,
    },
    {
      id: 10,
      label: 'Sample bis 5',
      children: [],
      expanded: false,
      checked: false,
    },
  ];

  searchTerm = '';

  onSearchChange() {
    this.nodes.forEach((node) => {
      this.applySearch(node, this.searchTerm.toLowerCase());
    });
  }

  applySearch(node: TreeNode, term: string): boolean {
    term = term || '';

    if (!term.trim()) {
      node.visible = true;
      node.highlight = false;
      this.firstMatchId = null;

      if (node.children) {
        node.children.forEach(child => this.applySearch(child, term));
      }

      return true;
    }

    const nameMatches = node.label.toLowerCase().includes(term);
    let childMatches = false;

    if (node.children) {
      childMatches = node.children
        .map(child => this.applySearch(child, term))
        .some(match => match);
    }

    node.visible = nameMatches || childMatches;
    node.highlight = nameMatches;
    node.expanded = childMatches;

    // ✅ Save the first match's ID to scroll to later
    if (nameMatches && !this.firstMatchId) {
      this.firstMatchId = `node-${node.id}`;
    }

    return node.visible!;
  }

  clearSearch() {
    this.searchControl.setValue('');
  }
}
