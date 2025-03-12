import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ImageLabelerComponent } from './image-labeler.component';

describe('ImageLabelerComponent', () => {
  let component: ImageLabelerComponent;
  let fixture: ComponentFixture<ImageLabelerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ImageLabelerComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ImageLabelerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
