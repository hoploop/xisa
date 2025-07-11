export * from './auth.service';
import { AuthService } from './auth.service';
export * from './auth.serviceInterface';
export * from './default.service';
import { DefaultService } from './default.service';
export * from './default.serviceInterface';
export * from './detector.service';
import { DetectorService } from './detector.service';
export * from './detector.serviceInterface';
export * from './operator.service';
import { OperatorService } from './operator.service';
export * from './operator.serviceInterface';
export * from './player.service';
import { PlayerService } from './player.service';
export * from './player.serviceInterface';
export * from './project.service';
import { ProjectService } from './project.service';
export * from './project.serviceInterface';
export * from './recorder.service';
import { RecorderService } from './recorder.service';
export * from './recorder.serviceInterface';
export * from './trainer.service';
import { TrainerService } from './trainer.service';
export * from './trainer.serviceInterface';
export * from './ws.service';
import { WsService } from './ws.service';
export * from './ws.serviceInterface';
export const APIS = [AuthService, DefaultService, DetectorService, OperatorService, PlayerService, ProjectService, RecorderService, TrainerService, WsService];
