import { AfterViewInit, Component, ElementRef, EventEmitter, OnDestroy, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-resize-listener',
  standalone: false,

  templateUrl: './resize-listener.component.html',
  styleUrl: './resize-listener.component.scss'
})
export class ResizeListenerComponent implements OnInit,OnDestroy, AfterViewInit {
  observer?: ResizeObserver;
  @Output() resized = new EventEmitter<[number,number]>();

  constructor(private host: ElementRef) {}


  ngOnInit(): void {
    this.observer = new ResizeObserver(entries => {
      const width = entries[0].contentRect.width;
      const height = entries[0].contentRect.height;
      this.resized.next([width,height]);

    });

    this.observer.observe(this.host.nativeElement);


  }

  ngAfterViewInit(): void {
    setTimeout(()=>{
      const height = this.host.nativeElement.clientHeight;
      const width = this.host.nativeElement.clientWidth;
      this.resized.next([width,height]);
    })

  }


  ngOnDestroy(): void {
    this.observer?.unobserve(this.host.nativeElement);
  }

}
