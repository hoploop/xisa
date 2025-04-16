import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AuthLogoutModalComponent } from './auth-logout-modal.component';

describe('AuthLogoutModalComponent', () => {
  let component: AuthLogoutModalComponent;
  let fixture: ComponentFixture<AuthLogoutModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AuthLogoutModalComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AuthLogoutModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
