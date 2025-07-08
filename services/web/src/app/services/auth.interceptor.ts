import { HttpEvent, HttpHandler, HttpInterceptor, HttpInterceptorFn, HttpRequest } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiService } from './api.service';
import { environment } from '@environments/environment';

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  return next(req);
};


@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  constructor(private api: ApiService) {}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    // Get the bearer token from localStorage (or another place where it's stored)
    const token = this.api.getToken();

    // If a token exists, clone the request and add the Authorization header
    if (token) {
      const clonedRequest = req.clone({
        setHeaders: {
          Authorization: `${environment.apiBearerKey} ${token}`,
        }
      });
      // Pass the modified request to the next handler
      return next.handle(clonedRequest);
    }

    // If no token is available, pass the original request
    return next.handle(req);
  }
}
