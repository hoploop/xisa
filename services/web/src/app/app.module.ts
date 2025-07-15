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
import { RouterModule } from '@angular/router';
import { routes } from './app.routes';
import { AceModule } from 'ngx-ace-wrapper';
import { ACE_CONFIG } from 'ngx-ace-wrapper';
import { AceConfigInterface } from 'ngx-ace-wrapper';
import { AuthModule } from '@auth/auth.module';
import { ProjectModule } from '@project/project.module';
import { TrainModule } from '@train/train.module';
import { RecordModule } from '@record/record.module';
import { PlayModule } from '@play/play.module';
import { OperatorModule } from '@operator/operator.module';
import { DetectModule } from '@detect/detect.module';
import { HomeModule } from '@home/home.module';

const DEFAULT_ACE_CONFIG: AceConfigInterface = {
};
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
    UtilsModule,
    AuthModule,
    ProjectModule,
    TrainModule,
    RecordModule,
    HomeModule,
    DetectModule,
    PlayModule,
    OperatorModule,
    AceModule,
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
  providers: [provideHttpClient(),{
    provide: ACE_CONFIG,
    useValue: DEFAULT_ACE_CONFIG
  }],
  bootstrap: [AppComponent],
})
export class AppModule {}
