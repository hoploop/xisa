import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetectorImageListPageComponent } from './detector-image-list-page.component';

describe('DetectorImageListPageComponent', () => {
  let component: DetectorImageListPageComponent;
  let fixture: ComponentFixture<DetectorImageListPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [DetectorImageListPageComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DetectorImageListPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
