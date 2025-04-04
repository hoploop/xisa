import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'; // Import this
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { Configuration, ConfigurationParameters } from '@api/configuration';
import { environment } from '@environments/environment';
import { ApiModule } from '@api/api.module';
import { HttpBackend, provideHttpClient } from '@angular/common/http';
import { TranslateLoader, TranslateModule } from '@ngx-translate/core';
import { MultiTranslateHttpLoader } from 'ngx-translate-multi-http-loader';
import { AuthModule } from '@auth/auth.module';
import { TrainModule } from "./train/train.module";
import { MenuComponent } from './menu/menu.component';
import { AppRoutingModule } from './app-routing.module';
import { RouterModule } from '@angular/router';
import { WorkspaceModule } from '@workspace/workspace.module';
import { MomentModule } from 'ngx-moment';
import { NotFoundComponent } from './not-found/not-found.component';
import { TemplatesModule } from '@templates/templates.module';
import { UtilsModule } from '@utils/utils.module';
import { LoggerModule, NgxLoggerLevel } from "ngx-logger";
import { WelcomeComponent } from './welcome/welcome.component';

export function apiConfigFactory(): Configuration {
  const params: ConfigurationParameters = {
    basePath: environment.apiUrl,
  };
  return new Configuration(params);
}


export function HttpLoaderFactory(_httpBackend: HttpBackend) {
  return new MultiTranslateHttpLoader(
    _httpBackend,
    environment.locale.i18n.folders
  ); // /i18n/core/ on angular >= v18 with the new public logic
}

@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    NotFoundComponent,
    WelcomeComponent,
  ],
  imports: [
    AppRoutingModule,
    RouterModule,
    BrowserModule,
    BrowserAnimationsModule,
    FontAwesomeModule,
    AuthModule,
    MomentModule,
    UtilsModule,
    WorkspaceModule,
    TemplatesModule,
    ApiModule.forRoot(apiConfigFactory),
    LoggerModule.forRoot({
      level: NgxLoggerLevel.DEBUG,
      serverLogLevel: NgxLoggerLevel.DEBUG,
      disableConsoleLogging: false
    }),
    TranslateModule.forRoot({
        defaultLanguage: environment.locale.i18n.default,
        loader: {
            provide: TranslateLoader,
            useFactory: HttpLoaderFactory,
            deps: [HttpBackend],
        },
    }),
    TrainModule
],
  providers: [provideHttpClient()],
  bootstrap: [AppComponent]
})
export class AppModule { }
