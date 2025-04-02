import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetectorSettingsComponent } from './detector-settings.component';

describe('DetectorSettingsComponent', () => {
  let component: DetectorSettingsComponent;
  let fixture: ComponentFixture<DetectorSettingsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [DetectorSettingsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DetectorSettingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
