import { Routes } from "@angular/router";
import { HomePageComponent } from "@home/home-page/home-page.component";
import { ProjectListPageComponent } from "@project/project-list-page/project-list-page.component";
import { AuthGuard } from "@auth/auth.guard";
import { AuthLoginRequiredPageComponent } from "@auth/auth-login-required-page/auth-login-required-page.component";
import { ProjectPageComponent } from "@project/project-page/project-page.component";
import { DetectorImageListPageComponent } from "@detect/detector-image-list-page/detector-image-list-page.component";
import { DetectorListPageComponent } from "@detect/detector-list-page/detector-list-page.component";
import { RecordListPageComponent } from "@record/record-list-page/record-list-page.component";
import { RecordPageComponent } from "@record/record-page/record-page.component";
import { TrainerPageComponent } from "@train/trainer-page/trainer-page.component";
import { PlayerPageComponent } from "@play/player-page/player-page.component";
import { DetectorPageComponent } from "@detect/detector-page/detector-page.component";
import { TrainerLessonPageComponent } from "@train/trainer-lesson-page/trainer-lesson-page.component";
import { DetectorTrainSessionListPageComponent } from "@detect/detector-train-session-list-page/detector-train-session-list-page.component";
import { MockupComponent } from "@utils/mockup/mockup.component";

export const routes: Routes = [
  { path: '', component: HomePageComponent },

  { path: 'login', component: AuthLoginRequiredPageComponent },
  { path: 'project/list', component: ProjectListPageComponent, canActivate: [AuthGuard] },
  { path: 'project/page/:project_id', component: ProjectPageComponent, canActivate: [AuthGuard] },
  { path: 'record/list/:project_id', component: RecordListPageComponent, canActivate: [AuthGuard] },
  { path: 'record/page/:record_id', component: RecordPageComponent, canActivate: [AuthGuard] },
  { path: 'trainer/page/:project_id', component: TrainerPageComponent, canActivate: [AuthGuard] },
  { path: 'auto/page/:record_id', component: PlayerPageComponent, canActivate: [AuthGuard] },
  { path: 'player/page/:project_id', component: PlayerPageComponent, canActivate: [AuthGuard] },
  { path: 'detector/list/:project_id', component: DetectorListPageComponent, canActivate: [AuthGuard] },
  { path: 'detector/page/:detector_id', component: DetectorPageComponent, canActivate: [AuthGuard] },
  { path: 'detector/train/sessions/:detector_id', component: DetectorTrainSessionListPageComponent, canActivate: [AuthGuard] },
  { path: 'detector/image/list/:detector_id', component: DetectorImageListPageComponent, canActivate: [AuthGuard] },
  { path: 'trainer/lesson/:detector_id/:record_id', component: TrainerLessonPageComponent, canActivate: [AuthGuard] },
  { path: 'mockup',component:MockupComponent}
];
