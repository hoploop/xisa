import { ChangeDetectorRef, Directive, ElementRef, EventEmitter, NgZone, OnDestroy, Output } from '@angular/core';

@Directive({
  selector: '[appResizeObserver]',
  standalone: false
})
export class ResizeObserverDirective implements OnDestroy {

  @Output() resize: EventEmitter<ResizeObserverEntry[]> = new EventEmitter();

  private resizeObserver?: ResizeObserver;

  constructor(
    private el: ElementRef,
    private ngZone: NgZone,
    private cdr: ChangeDetectorRef
  ) {
    this.ngZone.runOutsideAngular(() => {
      this.resizeObserver = new ResizeObserver((entries) => {
        // Run inside Angular zone
        this.ngZone.run(() => {
          this.resize.emit(entries);
        });
      });

      // Start observing the parent element
      this.resizeObserver.observe(this.el.nativeElement.parentElement);
    });
  }

  ngOnDestroy() {
    // Disconnect the observer when the directive is destroyed
    if (this.resizeObserver) {
      this.resizeObserver.disconnect();
    }
  }
}
