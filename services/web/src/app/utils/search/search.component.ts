import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { debounceTime, distinctUntilChanged } from 'rxjs';
import { FAIconType } from '@constants/icons';

@Component({
  selector: 'app-search',
  standalone: false,
  templateUrl: './search.component.html',
  styleUrl: './search.component.scss'
})
export class SearchComponent implements OnInit{
  @Input() debounce:number = 500;
  @Input() placeholder:string = '';
  valueChanges = new EventEmitter<string>();
  @Output() valueChange = new EventEmitter<string>();
  FAIconType = FAIconType;
  @Input() value:string = '';

  ngOnInit() {
    this.valueChanges
      .pipe(
        debounceTime(this.debounce), // Wait 500ms after user stops typing
        distinctUntilChanged() // Only emit when value changes
      )
      .subscribe(value => {
        this.valueChange.next(value);
      });
  }

  onChange(value:string){
    this.value = value;
    this.valueChanges.next(this.value);
  }

}
