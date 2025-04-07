import { Component, NgModule } from '@angular/core';
import { Router, RouterModule, Routes } from '@angular/router';
import { MenuComponent } from './menu/menu.component';
import { ProjectListComponent } from '@workspace/project/project-list/project-list.component';
import { RecordListComponent } from '@workspace/record/record-list/record-list.component';
import { AuthGuard } from '@guards/auth.guard';
import { RecordFormComponent } from '@workspace/record/record-form/record-form.component';
import { DetectorListComponent } from '@workspace/detector/detector-list/detector-list.component';
import { CommonModule } from '@angular/common';
import { NotFoundComponent } from './not-found/not-found.component';
import { RecordStudioComponent } from '@workspace/record/record-studio/record-studio.component';
import { ImageAnnotatorComponent } from '@train/image-annotator/image-annotator.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { ProjectMenuComponent } from '@workspace/project/project-menu/project-menu.component';
import { RecordMenuComponent } from '@workspace/record/record-menu/record-menu.component';
import { AuthCheckGuard } from '@guards/auth-check.guard';
import { ProjectPageComponent } from '@workspace/project/project-page/project-page.component';

const routes: Routes = [
  { path: '', redirectTo:'welcome',pathMatch: 'full' },
  { path: '', component: MenuComponent, outlet: 'menu' },
  { path: 'welcome', component: WelcomeComponent ,canActivate:[AuthCheckGuard]  },
  { path: 'welcome', component: MenuComponent, outlet: 'menu' ,canActivate:[AuthCheckGuard] },
  { path: 'project/page/:project_id', component: ProjectPageComponent,canActivate:[AuthGuard] },
  { path: 'project/list', component: ProjectListComponent,canActivate:[AuthGuard] },
  { path: 'project/list', component: MenuComponent, outlet: 'menu' },
  { path: 'project/page/:project_id', component: ProjectMenuComponent, outlet: 'menu'},
  { path: 'record/list/:project_id', component: RecordListComponent,canActivate:[AuthGuard] },
  { path: 'record/list/:project_id', component: RecordMenuComponent,outlet: 'menu',canActivate:[AuthGuard] },
  { path: 'record/form/:record_id', component: RecordFormComponent,canActivate:[AuthGuard] },
  { path: 'record/studio/:record_id/:detector_id', component: RecordStudioComponent,canActivate:[AuthGuard] },
  { path: 'detector/list/:project_id', component: DetectorListComponent,canActivate:[AuthGuard] },
  { path: 'mockup', component: ImageAnnotatorComponent,canActivate:[AuthGuard]  },
  { path: '**', component: NotFoundComponent }
];

@NgModule({
  imports: [CommonModule,RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }


