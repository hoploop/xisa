import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DockScrollerComponent } from './dock-scroller.component';

describe('DockScrollerComponent', () => {
  let component: DockScrollerComponent;
  let fixture: ComponentFixture<DockScrollerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [DockScrollerComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DockScrollerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
