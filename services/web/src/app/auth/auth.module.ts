import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthCheckModalComponent } from './auth-check-modal/auth-check-modal.component';
import { AuthLoginModalComponent } from './auth-login-modal/auth-login-modal.component';
import { AuthLogoutModalComponent } from './auth-logout-modal/auth-logout-modal.component';
import { AuthRegisterModalComponent } from './auth-register-modal/auth-register-modal.component';
import { AuthUnregisterModalComponent } from './auth-unregister-modal/auth-unregister-modal.component';
import { AuthLoginRequiredPageComponent } from './auth-login-required-page/auth-login-required-page.component';
import { UtilsModule } from '@utils/utils.module';
import { TranslateModule } from '@ngx-translate/core';
import { FormsModule } from '@angular/forms';
import { MomentModule } from 'ngx-moment';

@NgModule({
  declarations: [
    AuthCheckModalComponent,
    AuthLoginModalComponent,
    AuthLogoutModalComponent,
    AuthRegisterModalComponent,
    AuthUnregisterModalComponent,
    AuthLoginRequiredPageComponent,
  ],
  imports: [
    CommonModule,
    UtilsModule,
    TranslateModule,
    FormsModule,
    MomentModule,
  ],
  exports: [
    AuthCheckModalComponent,
    AuthLoginModalComponent,
    AuthLogoutModalComponent,
    AuthRegisterModalComponent,
    AuthLoginRequiredPageComponent,
  ],
})
export class AuthModule {}
