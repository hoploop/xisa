import { HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AuthService, TrainService, ProjectService, DetectorService, RecordService } from '@api/index';
import { environment } from '@environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(
    public auth: AuthService,
    public train: TrainService,
    public project: ProjectService,
    public detector: DetectorService,
    public record: RecordService
  ) {}

  setSession(session: string) {
    let newHeaders = new HttpHeaders({ 'X-Session': session });
    this.auth.defaultHeaders = newHeaders;
    this.project.defaultHeaders = newHeaders;
    this.record.defaultHeaders = newHeaders;
    this.detector.defaultHeaders = newHeaders;

  }

  checkToken(): string | null {
    let token = localStorage.getItem('token');
    if (token != null) {
      this.auth.configuration.credentials[environment.apiBearerKey] = token;
      this.train.configuration.credentials[environment.apiBearerKey] = token;
      this.record.configuration.credentials[environment.apiBearerKey] = token;
      this.project.configuration.credentials[environment.apiBearerKey] = token;
      this.detector.configuration.credentials[environment.apiBearerKey] = token;

    } else {
      delete this.auth.configuration.credentials[environment.apiBearerKey];
      delete this.train.configuration.credentials[environment.apiBearerKey];
      delete this.project.configuration.credentials[environment.apiBearerKey];
      delete this.record.configuration.credentials[environment.apiBearerKey];
      delete this.detector.configuration.credentials[environment.apiBearerKey];
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
    this.project.configuration.credentials[environment.apiBearerKey] = token;
    this.record.configuration.credentials[environment.apiBearerKey] = token;
    this.detector.configuration.credentials[environment.apiBearerKey] = token;
  }

  remToken() {
    localStorage.removeItem('token');
    delete this.auth.configuration.credentials[environment.apiBearerKey];
    delete this.train.configuration.credentials[environment.apiBearerKey];
    delete this.project.configuration.credentials[environment.apiBearerKey];
    delete this.record.configuration.credentials[environment.apiBearerKey];
    delete this.detector.configuration.credentials[environment.apiBearerKey];
  }

}
