import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AuthService, DetectorService, RecorderService, ProjectService, TrainerService, PlayerService, OperatorService } from '@api/index';
import { environment } from '@environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(
    private http: HttpClient,
    public auth: AuthService,
    public project: ProjectService,
    public detector: DetectorService,
    public recorder: RecorderService,
    public operator: OperatorService,
    public trainer: TrainerService,
    public player: PlayerService

  ) {}

  setSession(session: string) {
    let newHeaders = new HttpHeaders({ 'X-Session': session });
    this.auth.defaultHeaders = newHeaders;
    this.project.defaultHeaders = newHeaders;
    this.recorder.defaultHeaders = newHeaders;
    this.operator.defaultHeaders = newHeaders;
    this.detector.defaultHeaders = newHeaders;
    this.player.defaultHeaders = newHeaders;
    this.trainer.defaultHeaders = newHeaders;

  }

  checkToken(): string | null {
    let token = localStorage.getItem('token');
    if (token != null) {
      this.auth.configuration.credentials[environment.apiBearerKey] = token;
      this.operator.configuration.credentials[environment.apiBearerKey] = token;
      this.recorder.configuration.credentials[environment.apiBearerKey] = token;
      this.project.configuration.credentials[environment.apiBearerKey] = token;
      this.detector.configuration.credentials[environment.apiBearerKey] = token;
      this.player.configuration.credentials[environment.apiBearerKey] = token;
      this.trainer.configuration.credentials[environment.apiBearerKey] = token;

    } else {
      delete this.auth.configuration.credentials[environment.apiBearerKey];
      delete this.project.configuration.credentials[environment.apiBearerKey];
      delete this.operator.configuration.credentials[environment.apiBearerKey];
      delete this.recorder.configuration.credentials[environment.apiBearerKey];
      delete this.detector.configuration.credentials[environment.apiBearerKey];
      delete this.player.configuration.credentials[environment.apiBearerKey];
      delete this.trainer.configuration.credentials[environment.apiBearerKey];
    }
    return token;
  }

  getToken(): string | null {
    let token = localStorage.getItem('token');
    return token;
  }

  setToken(token: string) {
    localStorage.setItem('token', token);
    this.auth.configuration.credentials[environment.apiBearerKey] = token;
    this.project.configuration.credentials[environment.apiBearerKey] = token;
    this.operator.configuration.credentials[environment.apiBearerKey] = token;
    this.recorder.configuration.credentials[environment.apiBearerKey] = token;
    this.trainer.configuration.credentials[environment.apiBearerKey] = token;
    this.player.configuration.credentials[environment.apiBearerKey] = token;
    this.detector.configuration.credentials[environment.apiBearerKey] = token;
  }

  remToken() {
    localStorage.removeItem('token');
    delete this.auth.configuration.credentials[environment.apiBearerKey];
    delete this.project.configuration.credentials[environment.apiBearerKey];
    delete this.recorder.configuration.credentials[environment.apiBearerKey];
    delete this.operator.configuration.credentials[environment.apiBearerKey];
    delete this.trainer.configuration.credentials[environment.apiBearerKey];
    delete this.player.configuration.credentials[environment.apiBearerKey];
    delete this.detector.configuration.credentials[environment.apiBearerKey];
  }

}
