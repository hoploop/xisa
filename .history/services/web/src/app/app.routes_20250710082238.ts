import { Routes } from "@angular/router";
import { TreeviewComponent } from "@utils/treeview/treeview.component";
import { HomePageComponent } from "@pages/home-page/home-page.component";
import { ProjectListPageComponent } from "@pages/project-list-page/project-list-page.component";
import { AuthGuard } from "@guards/auth.guard";
import { AuthLoginRequiredPageComponent } from "@pages/auth-login-required-page/auth-login-required-page.component";
import { ProjectPageComponent } from "@pages/project-page/project-page.component";
import { DetectorImageListPageComponent } from "@pages/detector-image-list-page/detector-image-list-page.component";
import { DetectorListPageComponent } from "@pages/detector-list-page/detector-list-page.component";
import { RecordListPageComponent } from "@pages/record-list-page/record-list-page.component";
import { RecordPageComponent } from "@pages/record-page/record-page.component";
import { TrainerPageComponent } from "@pages/trainer-page/trainer-page.component";
import { PlayerPageComponent } from "@pages/player-page/player-page.component";
import { DetectorPageComponent } from "@pages/detector-page/detector-page.component";
import { TrainerLessonPageComponent } from "@pages/trainer-lesson-page/trainer-lesson-page.component";
import { DetectorTrainSessionListPageComponent } from "@pages/detector-train-session-list-page/detector-train-session-list-page.component";

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
  { path: 'mockup',component:TreeviewComponent}
];
