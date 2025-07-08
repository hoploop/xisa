import { Injectable } from '@angular/core';
import { NavigationStart, Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class NavigationService {

  private previousUrl: string | null = null;

  constructor(private router: Router) {
    this.router.events.subscribe(event => {
      if (event instanceof NavigationStart) {
        this.previousUrl = event.url; // Store previous route
      }
    });
  }

  getPreviousUrl(): string | null {
    return this.previousUrl;
  }
}
