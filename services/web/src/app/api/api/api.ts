export * from './auth.service';
import { AuthService } from './auth.service';
export * from './auth.serviceInterface';
export * from './detector.service';
import { DetectorService } from './detector.service';
export * from './detector.serviceInterface';
export * from './recorder.service';
import { RecorderService } from './recorder.service';
export * from './recorder.serviceInterface';
export * from './train.service';
import { TrainService } from './train.service';
export * from './train.serviceInterface';
export * from './trainer.service';
import { TrainerService } from './trainer.service';
export * from './trainer.serviceInterface';
export * from './workspace.service';
import { WorkspaceService } from './workspace.service';
export * from './workspace.serviceInterface';
export * from './ws.service';
import { WsService } from './ws.service';
export * from './ws.serviceInterface';
export const APIS = [AuthService, DetectorService, RecorderService, TrainService, TrainerService, WorkspaceService, WsService];
