import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AuthLoginRequiredPageComponent } from './auth-login-required-page.component';

describe('AuthLoginRequiredPageComponent', () => {
  let component: AuthLoginRequiredPageComponent;
  let fixture: ComponentFixture<AuthLoginRequiredPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AuthLoginRequiredPageComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AuthLoginRequiredPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
