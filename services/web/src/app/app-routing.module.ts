import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MenuComponent } from './menu/menu.component';
import { LogoutComponent } from '@auth/logout/logout.component';
import { LoginComponent } from '@auth/login/login.component';
import { ProjectListComponent } from '@workspace/project/project-list/project-list.component';
import { ProjectFormComponent } from '@workspace/project/project-form/project-form.component';
import { RegisterComponent } from '@auth/register/register.component';
import { UnregisterComponent } from '@auth/unregister/unregister.component';
import { RecordListComponent } from '@workspace/record/record-list/record-list.component';
import { AuthGuard } from '@guards/auth.guard';
import { RecordControllerComponent } from '@workspace/record/record-controller/record-controller.component';
import { RecordFormComponent } from '@workspace/record/record-form/record-form.component';
import { DetectorListComponent } from '@workspace/detector/detector-list/detector-list.component';
import { CommonModule } from '@angular/common';
import { NotFoundComponent } from './not-found/not-found.component';
import { DetectorFormComponent } from '@workspace/detector/detector-form/detector-form.component';
import { DetectorLearnComponent } from '@workspace/detector/detector-learn/detector-learn.component';
import { RecordStudioComponent } from '@workspace/record/record-studio/record-studio.component';
import { RecordFrameComponent } from '@workspace/record/record-frame/record-frame.component';
import { ImageAnnotatorComponent } from '@train/image-annotator/image-annotator.component';

const routes: Routes = [
  { path: '', component: LogoutComponent,canActivate:[AuthGuard] },
  { path: '', component: MenuComponent, outlet: 'menu' },
  { path: 'login', component: LoginComponent },
  { path: 'logout', component: LogoutComponent,canActivate:[AuthGuard] },
  { path: 'register', component: RegisterComponent },
  { path: 'unregister', component: UnregisterComponent },
  { path: 'project/list', component: ProjectListComponent,canActivate:[AuthGuard] },
  { path: 'project/new', component: ProjectFormComponent,canActivate:[AuthGuard] },
  { path: 'project/edit/:id', component: ProjectFormComponent,canActivate:[AuthGuard] },
  { path: 'record/list/:project_id', component: RecordListComponent,canActivate:[AuthGuard] },
  { path: 'record/form/:record_id', component: RecordFormComponent,canActivate:[AuthGuard] },
  { path: 'record/studio/:record_id/:detector_id', component: RecordStudioComponent,canActivate:[AuthGuard] },
  { path: 'record/controller/:project_id', component: RecordControllerComponent,canActivate:[AuthGuard] },
  { path: 'detector/list/:project_id', component: DetectorListComponent,canActivate:[AuthGuard] },
  { path: 'detector/edit/:project_id/:id', component: DetectorFormComponent,canActivate:[AuthGuard] },
  { path: 'detector/new/:project_id', component: DetectorFormComponent,canActivate:[AuthGuard] },
  { path: 'detector/learn/:detector_id', component: DetectorLearnComponent,canActivate:[AuthGuard] },
  { path: 'mockup', component: ImageAnnotatorComponent,canActivate:[AuthGuard]  },
  { path: '**', component: NotFoundComponent }
];

@NgModule({
  imports: [CommonModule,RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
