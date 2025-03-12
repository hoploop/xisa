import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';
import { LogoutComponent } from './logout/logout.component';
import { CheckComponent } from './check/check.component';
import { RegisterComponent } from './register/register.component';
import { UnregisterComponent } from './unregister/unregister.component';
import { TranslateModule } from '@ngx-translate/core';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { UtilsModule } from '@utils/utils.module';
import { FormsModule } from '@angular/forms';



@NgModule({
  declarations: [
    LoginComponent,
    LogoutComponent,
    CheckComponent,
    RegisterComponent,
    UnregisterComponent
  ],
  imports: [
    CommonModule,
    TranslateModule,
    FontAwesomeModule,
    UtilsModule,
    FormsModule
  ],
  exports: [
    CheckComponent,
    LoginComponent,
    RegisterComponent
  ]
})
export class AuthModule { }
