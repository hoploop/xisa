import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MenuComponent } from './menu/menu.component';
import { LogoutComponent } from '@auth/logout/logout.component';
import { LoginComponent } from '@auth/login/login.component';
import { ProjectListComponent } from '@workspace/project/project-list/project-list.component';
import { RegisterComponent } from '@auth/register/register.component';
import { UnregisterComponent } from '@auth/unregister/unregister.component';
import { RecordListComponent } from '@workspace/record/record-list/record-list.component';
import { AuthGuard } from '@guards/auth.guard';
import { RecordControllerComponent } from '@workspace/record/record-controller/record-controller.component';
import { RecordFormComponent } from '@workspace/record/record-form/record-form.component';
import { DetectorListComponent } from '@workspace/detector/detector-list/detector-list.component';
import { CommonModule } from '@angular/common';
import { NotFoundComponent } from './not-found/not-found.component';
import { RecordStudioComponent } from '@workspace/record/record-studio/record-studio.component';
import { ImageAnnotatorComponent } from '@train/image-annotator/image-annotator.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { ProjectMenuComponent } from '@workspace/project/project-menu/project-menu.component';

const routes: Routes = [
  { path: '', component: LogoutComponent,canActivate:[AuthGuard] },
  { path: '', component: MenuComponent, outlet: 'menu' },
  { path: 'welcome', component: WelcomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'unregister', component: UnregisterComponent },
  { path: 'project/list', component: ProjectListComponent,canActivate:[AuthGuard] },
  { path: 'project/list', component: ProjectMenuComponent, outlet: 'menu'},
  { path: 'record/list/:project_id', component: RecordListComponent,canActivate:[AuthGuard] },
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
