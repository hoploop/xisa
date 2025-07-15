import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomePageComponent } from '@home/home-page/home-page.component';
import { MenuPageComponent } from '@home/menu-page/menu-page.component';
import { HomeCardComponent } from './home-card/home-card.component';
import { MenuCardComponent } from './menu-card/menu-card.component';
import { UtilsModule } from '@utils/utils.module';
import { TranslateModule } from '@ngx-translate/core';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    HomePageComponent,
    MenuPageComponent,
    MenuCardComponent,
    HomeCardComponent,
  ],
  imports: [CommonModule,UtilsModule,TranslateModule,FormsModule],
  exports: [
    HomePageComponent,
    MenuPageComponent,
    MenuCardComponent,
    HomeCardComponent,
  ],
})
export class HomeModule {}
