export const environment = {
  production: false,
  title: 'Memex',
  version: "2.0.0",
  apiVersion: '1.5.0',
  apiUrl: 'http://localhost:8000',
  videoUrl: 'http://localhost:8000/recorder/video/',
  imageUrl: 'http://localhost:8000/recorder/frame/',
  imageThumbnailUrl: 'http://localhost:8000/recorder/frame/thumbnail/',
  apiBearerKey: 'OAuth2PasswordBearer',
  editorLicense: 'eyJhbGciOiJFUzI1NiJ9.eyJleHAiOjE3MzUzNDM5OTksImp0aSI6IjgzMGU2ZWM2LWZjZjItNDM1ZS1iZDE1LTZlMmMzMTEzOWU1NCIsInVzYWdlRW5kcG9pbnQiOiJodHRwczovL3Byb3h5LWV2ZW50LmNrZWRpdG9yLmNvbSIsImRpc3RyaWJ1dGlvbkNoYW5uZWwiOlsiY2xvdWQiLCJkcnVwYWwiLCJzaCJdLCJ3aGl0ZUxhYmVsIjp0cnVlLCJsaWNlbnNlVHlwZSI6InRyaWFsIiwiZmVhdHVyZXMiOlsiKiJdLCJ2YyI6Ijc1NmE1ZWIxIn0.1QDuspbXMxWGlv4hd2nS-d2DhcE624GiSWjuQ3rImz4l945NZhVC_gmEl4B_5SwzoO9dgtLBpEPmaCRgDavNUw',
  wsUrl: 'ws://localhost:8000/ws/connection',
  googleClientId:
    '130114740949-1f411fjld9q21hllacqh079s3dqfuc35.apps.googleusercontent.com',
  wsReconnect: 3000,
  locale: {
    i18n: {
      folders: [
       'http://localhost:8000/i18n/auth/',
        'http://localhost:8000/i18n/train/',
        'http://localhost:8000/i18n/menu/',
        'http://localhost:8000/i18n/detector/',
        'http://localhost:8000/i18n/recorder/',
        'http://localhost:8000/i18n/project/',
        'http://localhost:8000/i18n/player/',
        'http://localhost:8000/i18n/trainer/'
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
        width: { ideal: 4096 },
        height: { ideal: 2160 },
      },
      audio: false,
    },
  },
};
