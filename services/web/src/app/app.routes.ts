import { Routes } from "@angular/router";
import { TreeviewComponent } from "@utils/treeview/treeview.component";
import { DetectorImageListRoute } from "@workspace/detector/detector-image-list/detector-image-list.route";
import { DetectorListRoute } from "@workspace/detector/detector-list/detector-list.route";
import { ProjectListRoute } from "@workspace/project/project-list/project-list.route";
import { ProjectPageRoute } from "@workspace/project/project-page/project-page.route";
import { RecordListRoute } from "@workspace/record/record-list/record-list.route";
import { RecordStudioRoute } from "@workspace/record/record-studio/record-studio.route";
import { WelcomeRoute } from "./welcome/welcome.route";

export const routes: Routes = [
  { path: '', component: WelcomeRoute },
  { path: 'record/studio/:record_id', component: RecordStudioRoute },
  { path: 'project/list', component: ProjectListRoute },
  { path: 'project/page/:project_id', component: ProjectPageRoute },
  { path: 'record/list/:project_id', component: RecordListRoute },
  { path: 'detector/list/:project_id', component: DetectorListRoute },
  { path: 'detector/image/list/:detector_id', component: DetectorImageListRoute },
  { path: 'mockup',component:TreeviewComponent}
];
