import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { Configuration, ConfigurationParameters } from '@api/configuration';
import { environment } from '@environments/environment';
import { ApiModule } from '@api/api.module';
import { HttpBackend, provideHttpClient } from '@angular/common/http';
import { TranslateLoader, TranslateModule } from '@ngx-translate/core';
import { MultiTranslateHttpLoader } from 'ngx-translate-multi-http-loader';
import { MomentModule } from 'ngx-moment';
import { UtilsModule } from '@utils/utils.module';
import { LoggerModule, NgxLoggerLevel } from 'ngx-logger';
import { NgIconsModule } from '@ng-icons/core';
import { NGIcons } from '@constants/icons';
import { MonacoEditorModule } from 'ngx-monaco-editor-v2';
import { RouterModule } from '@angular/router';
import { routes } from './app.routes';
import { PagesModule } from '@pages/pages.module';
import { ModalsModule } from '@modals/modals.module';
import { CardsModule } from '@cards/cards.module';

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
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    FontAwesomeModule,
    MomentModule,
    ModalsModule,
    CardsModule,
    UtilsModule,
    PagesModule,
    MonacoEditorModule.forRoot(),
    ApiModule.forRoot(apiConfigFactory),
    NgIconsModule.withIcons(NGIcons),
    RouterModule.forRoot(routes),
    LoggerModule.forRoot({
      level: NgxLoggerLevel.DEBUG,
      serverLogLevel: NgxLoggerLevel.DEBUG,
      disableConsoleLogging: false,
    }),
    TranslateModule.forRoot({
      defaultLanguage: environment.locale.i18n.default,
      loader: {
        provide: TranslateLoader,
        useFactory: HttpLoaderFactory,
        deps: [HttpBackend],
      },
    }),
  ],
  providers: [provideHttpClient()],
  bootstrap: [AppComponent],
})
export class AppModule {}
