import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AuthRegisterModalComponent } from './auth-register-modal.component';

describe('AuthRegisterModalComponent', () => {
  let component: AuthRegisterModalComponent;
  let fixture: ComponentFixture<AuthRegisterModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AuthRegisterModalComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AuthRegisterModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
