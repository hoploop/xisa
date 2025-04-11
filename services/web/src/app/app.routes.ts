import { Routes } from "@angular/router";
import { DetectorListRoute } from "@workspace/detector/detector-list/detector-list.route";
import { ProjectListRoute } from "@workspace/project/project-list/project-list.route";
import { ProjectPageRoute } from "@workspace/project/project-page/project-page.route";
import { RecordListRoute } from "@workspace/record/record-list/record-list.route";
import { RecordStudioRoute } from "@workspace/record/record-studio/record-studio.route";

export const routes: Routes = [
  { path: 'record/studio/:record_id', component: RecordStudioRoute },
  { path: 'project/list', component: ProjectListRoute },
  { path: 'project/page/:project_id', component: ProjectPageRoute },
  { path: 'record/list/:project_id', component: RecordListRoute },
  { path: 'detector/list/:project_id', component: DetectorListRoute },
];
