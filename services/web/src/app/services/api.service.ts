import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AuthService, TrainService, DetectorService, RecorderService, WorkspaceService, TrainerService } from '@api/index';
import { environment } from '@environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(
    private http: HttpClient,
    public auth: AuthService,
    public train: TrainService,
    public workspace: WorkspaceService,
    public detector: DetectorService,
    public recorder: RecorderService,
    public trainer: TrainerService,

  ) {}

  setSession(session: string) {
    let newHeaders = new HttpHeaders({ 'X-Session': session });
    this.auth.defaultHeaders = newHeaders;
    this.workspace.defaultHeaders = newHeaders;
    this.recorder.defaultHeaders = newHeaders;
    this.detector.defaultHeaders = newHeaders;
    this.trainer.defaultHeaders = newHeaders;

  }

  checkToken(): string | null {
    let token = localStorage.getItem('token');
    if (token != null) {
      this.auth.configuration.credentials[environment.apiBearerKey] = token;
      this.train.configuration.credentials[environment.apiBearerKey] = token;
      this.recorder.configuration.credentials[environment.apiBearerKey] = token;
      this.workspace.configuration.credentials[environment.apiBearerKey] = token;
      this.detector.configuration.credentials[environment.apiBearerKey] = token;
      this.trainer.configuration.credentials[environment.apiBearerKey] = token;

    } else {
      delete this.auth.configuration.credentials[environment.apiBearerKey];
      delete this.train.configuration.credentials[environment.apiBearerKey];
      delete this.workspace.configuration.credentials[environment.apiBearerKey];
      delete this.recorder.configuration.credentials[environment.apiBearerKey];
      delete this.detector.configuration.credentials[environment.apiBearerKey];
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
    this.train.configuration.credentials[environment.apiBearerKey] = token;
    this.workspace.configuration.credentials[environment.apiBearerKey] = token;
    this.recorder.configuration.credentials[environment.apiBearerKey] = token;
    this.trainer.configuration.credentials[environment.apiBearerKey] = token;
    this.detector.configuration.credentials[environment.apiBearerKey] = token;
  }

  remToken() {
    localStorage.removeItem('token');
    delete this.auth.configuration.credentials[environment.apiBearerKey];
    delete this.train.configuration.credentials[environment.apiBearerKey];
    delete this.workspace.configuration.credentials[environment.apiBearerKey];
    delete this.recorder.configuration.credentials[environment.apiBearerKey];
    delete this.trainer.configuration.credentials[environment.apiBearerKey];
    delete this.detector.configuration.credentials[environment.apiBearerKey];
  }

}
