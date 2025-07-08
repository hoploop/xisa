import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AuthUnregisterModalComponent } from './auth-unregister-modal.component';

describe('AuthUnregisterModalComponent', () => {
  let component: AuthUnregisterModalComponent;
  let fixture: ComponentFixture<AuthUnregisterModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AuthUnregisterModalComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AuthUnregisterModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
