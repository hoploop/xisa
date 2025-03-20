export const environment = {
  production: true,
  title: 'Memex',
  version: "2.0.0",
  apiVersion: '1.5.0',
  apiUrl: 'http://localhost:8000',
  apiBearerKey: 'OAuth2PasswordBearer',
  videoUrl: 'http://localhost:8000/record/video/',
  wsUrl: 'ws://localhost:8000/ws/connection',
  editorLicense:'eyJhbGciOiJFUzI1NiJ9.eyJleHAiOjE3NjU2NzAzOTksImp0aSI6ImRkNjQ2NjNlLTA2NzAtNDIxOS04ZWMwLTU1NjZjMTRlMjA3OCIsInVzYWdlRW5kcG9pbnQiOiJodHRwczovL3Byb3h5LWV2ZW50LmNrZWRpdG9yLmNvbSIsImRpc3RyaWJ1dGlvbkNoYW5uZWwiOlsiY2xvdWQiLCJkcnVwYWwiXSwiZmVhdHVyZXMiOlsiRFJVUCIsIkJPWCJdLCJ2YyI6IjI2MTM2YjkxIn0.5T1JM73gGmiqJpXchMYDXDcjJ786TvrZf_e1hDOCvcwg-_ws4gksZwt0GLTVgr2weX3RaHC7e1XETur0Fd1ULQ' ,
  googleClientId:
    '130114740949-1f411fjld9q21hllacqh079s3dqfuc35.apps.googleusercontent.com',
  wsReconnect: 3000,
  locale: {
    i18n: {
      folders: [
        'http://localhost:8000/i18n/auth/',
        'http://localhost:8000/i18n/train/',
        'http://localhost:8000/i18n/menu/',
        'http://localhost:8000/i18n/workspace/',
        'http://localhost:8000/i18n/player/'
      ],
      default: 'en',
    },
  },
  theme: {
    default: 'light',
  },
  background: {
    default: 'autumn',
  },
  camera: {
    constraints: {
      video: {
        facingMode: { exact: 'user' },
        width: { ideal: 4096 },
        height: { ideal: 2160 },
      },
      audio: false,
    },
  },
};
