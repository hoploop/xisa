import { Injectable } from '@angular/core';
import { environment } from '@environments/environment';
import {
  retry,
  BehaviorSubject,
  Subject,
  skip,
  filter,
  tap,
  map,
  timer,
  distinctUntilChanged,
  Observable,
  take,
} from 'rxjs';
import { webSocket } from 'rxjs/webSocket';

export const WS_ENDPOINT = environment.wsUrl;
export const RECONNECT_INTERVAL = environment.wsReconnect;

@Injectable({
  providedIn: 'root',
})
export class WsService {
  private readonly URL = environment.wsUrl;
  private status$: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(
    false
  );
  private ws: any;
  public messages$: Subject<any> = new Subject<any>();

  public connect(token: string, session: string): void {
    this.create(token, session);
    this.connectionStatus
      .pipe(
        skip(1),
        filter((status) => !status),
        tap(() => this.create(token, session))
      )
      .subscribe();
  }

  private create(token: string, session: string) {
    if (this.ws) {
      this.ws.unsubscribe();
    }
    let queryParams = `?&token=${token}`;

    const openObserver = new Subject<Event>();
    openObserver.pipe(map((_) => true)).subscribe(this.status$);
    const closeObserver = new Subject<CloseEvent>();
    closeObserver.pipe(map((_) => false)).subscribe(this.status$);
    this.ws = webSocket<any>({
      url: WS_ENDPOINT + '/' + session + queryParams,
      openObserver,
      closeObserver,
    });
    this.ws
      .pipe(
        retry({
          delay: (errs) => {
            this.status$.next(false);
            console.log(
              `Websocket connection down, will attempt reconnection in ${RECONNECT_INTERVAL}ms`
            );
            return timer(RECONNECT_INTERVAL);
          },
        })
      )
      .subscribe(this.messages$);
  }

  public get connectionStatus(): Observable<boolean> {
    return this.status$.pipe(distinctUntilChanged());
  }

  send(value: string) {
    if (this.ws) {
      this.ws.next(value);
    }
  }

  close() {
    if (this.ws) {
      this.ws.unsubscribe();
    }
    this.ws = null;
  }

  message(message: any) {
    this.connectionStatus
      .pipe(
        filter((status) => status),
        tap(() => this.ws.next(message)),
        take(1)
      )
      .subscribe();
  }
}
