import { AnimationProp } from '@fortawesome/angular-fontawesome';
import { faGoogle } from '@fortawesome/free-brands-svg-icons';
import { faHandPointDown, faHandPointer, faHandPointLeft, faHandPointRight, faHandPointUp, faImages, faSquare, faSquareCheck } from '@fortawesome/free-regular-svg-icons';
import {
  faAnglesDown,
  faAnglesUp,
  faArrowDown,
  faArrowLeft,
  faArrowPointer,
  faArrowRightToBracket,
  faArrowsUpDownLeftRight,
  faArrowUp,
  faArrowUpFromBracket,
  faBan,
  faBarsProgress,
  faBook,
  faBookmark,
  faBroom,
  faBug,
  faCamera,
  faCaretDown,
  faCaretUp,
  faCheck,
  faChevronDown,
  faChevronLeft,
  faChevronRight,
  faChevronUp,
  faCircle,
  faCircleCheck,
  faCircleChevronDown,
  faCircleChevronLeft,
  faCircleChevronRight,
  faCircleChevronUp,
  faCircleDown,
  faCircleHalfStroke,
  faCircleInfo,
  faCircleNotch,
  faCircleQuestion,
  faCircleUp,
  faCircleXmark,
  faClapperboard,
  faCloudSunRain,
  faCogs,
  faCubesStacked,
  faDownload,
  faEye,
  faEyeSlash,
  faFile,
  faFileImage,
  faFileText,
  faFileWaveform,
  faFilm,
  faFilter,
  faFloppyDisk,
  faFolder,
  faGlasses,
  faHomeAlt,
  faImage,
  faKey,
  faKeyboard,
  faLocationDot,
  faMagnifyingGlass,
  faMap,
  faMessage,
  faMicrophoneAlt,
  faMicrophoneAltSlash,
  faMouse,
  faNoteSticky,
  faPaperPlane,
  faPause,
  faPauseCircle,
  faPen,
  faPenNib,
  faPhotoFilm,
  faPlay,
  faPlayCircle,
  faPlus,
  faQuestion,
  faRefresh,
  faRobot,
  faRss,
  faSave,
  faSearch,
  faShapes,
  faSpinner,
  faSquarePen,
  faStop,
  faStopCircle,
  faTags,
  faTemperatureFull,
  faTowerBroadcast,
  faTrash,
  faTriangleExclamation,
  faUniversity,
  faUpRightAndDownLeftFromCenter,
  faUser,
  faUserMinus,
  faUserPlus,
  faVideo,
  faVideoCamera,
  faVideoSlash,
  faWarning,
  faXmark,
  IconDefinition,
} from '@fortawesome/free-solid-svg-icons';

export enum BIconType {
  person = 'bi-person',
  recordCircle = 'bi-record-circle',
  personAdd = 'bi-person-add',
  key = 'bi-key',
  typeBold = 'bi-type-bold',
  arrowDownRight = 'bi-arrow-down-right',
  arrowsMove = 'bi-arrows-move',
  boxArrowInRight = 'bi-box-arrow-in-right',
  boxArrowInLeft = 'bi-box-arrow-in-left',
  boxes = 'bi-boxes',
  search = 'bi-search',
  houseFill = 'bi-house-fill',
  lockFill = 'bi-lock-fill',
  lock = 'bi-lock',
  plusCircle = 'bi-plus-circle',
  plusCircleFill = 'bi-plus-circle-fill',
  plusSquare = 'bi-plus-square',
  plus = 'bi-plus',
  unlockFill = 'bi-unlock-fill',
  unlock = 'bi-unlock',
  pin = 'bi-pin',
  pinFill = 'bi-pin-fill',
  pinAngle = 'bi-pin-angle',
  pinAngleFill = 'bi-pin-angle-fill',
  record = 'bi-record-btn',
  pause = 'bi-pause-btn',
  play = 'bi-play-btn',
  stop = 'bi-stop-btn',
}

export const FAIconValues: { [key: string]: IconDefinition } = {
  xmark: faXmark,
  triangleExclamation: faTriangleExclamation,
  check: faCheck,
  circleDown: faCircleDown,
  circleUp: faCircleUp,
  download: faDownload,
  arrowUpFromBracket: faArrowUpFromBracket,
  upRightAndDownLeftFromCenter: faUpRightAndDownLeftFromCenter,
  pen: faPen,
  refresh: faRefresh,
  arrowLeft: faArrowLeft,
  shapes: faShapes,
  images: faImages,
  userPlus: faUserPlus,
  pause: faPause,
  play: faPlay,
  pauseCircle: faPauseCircle,
  playCircle: faPlayCircle,
  stop: faStop,
  stopCircle: faStopCircle,
  cubesStacked: faCubesStacked,
  bug: faBug,
  filter: faFilter,
  camera: faCamera,
  tags: faTags,
  rss: faRss,
  magnifyingGlass: faMagnifyingGlass,
  warning: faWarning,
  circleNotch: faCircleNotch,
  circleInfo: faCircleInfo,
  eye: faEye,
  bookmark: faBookmark,
  circleCheck: faCircleCheck,
  map: faMap,
  circleChevronLeft: faCircleChevronLeft,
  circleChevronUp: faCircleChevronUp,
  circleChevronDown: faCircleChevronDown,
  ciclrChevronRight: faCircleChevronRight,
  circleXmark: faCircleXmark,
  cloudSunRain: faCloudSunRain,
  ban: faBan,
  cogs: faCogs,
  google: faGoogle,
  user: faUser,
  search: faSearch,
  glasses: faGlasses,
  arrowDown: faArrowDown,
  arrowUp: faArrowUp,
  trash: faTrash,
  squarePen: faSquarePen,
  chevronDown: faChevronDown,
  chevronUp: faChevronUp,
  chevronLeft: faChevronLeft,
  chevronRight: faChevronRight,
  paperPlane: faPaperPlane,
  circle: faCircle,
  anglesUp: faAnglesUp,
  anglesDown: faAnglesDown,
  plus: faPlus,
  robot: faRobot,
  book: faBook,
  temperatureFull: faTemperatureFull,
  save: faSave,
  floppyDisk: faFloppyDisk,
  noteSticky: faNoteSticky,
  caretDown: faCaretDown,
  arrowRightToBracket: faArrowRightToBracket,
  key: faKey,
  caretUp: faCaretUp,
  spinner: faSpinner,
  image: faImage,
  folder:faFolder,
  barsProgress: faBarsProgress,
  circleQuestion: faCircleQuestion,
  towerBroadcast: faTowerBroadcast,
  eyeSlash: faEyeSlash,
  arrowsUpDownLeftRight: faArrowsUpDownLeftRight,
  arrowPointer: faArrowPointer,
  microphoneAlt: faMicrophoneAlt,
  microphoneAltSlash: faMicrophoneAltSlash,
  squareCheck: faSquareCheck,
  square: faSquare,
  fileWaveForm: faFileWaveform,
  message: faMessage,
  broom: faBroom,
  home: faHomeAlt,
  penNib: faPenNib,
  locationDot: faLocationDot,
  question: faQuestion,
  userMinus:faUserMinus,
  film: faFilm,
  clapperBoard: faClapperboard,
  video: faVideo,
  videoSlash: faVideoSlash,
  videoCamera: faVideoCamera,
  photoFilm: faPhotoFilm,
  file: faFile,
  fileText: faFileText,
  mouse: faMouse,
  keyboard: faKeyboard,
  fileImage: faFileImage,
  circleHalfStroke: faCircleHalfStroke,
  university:faUniversity,
  handPointer: faHandPointer,
  handPointUp: faHandPointUp,
  handPointRight: faHandPointRight,
  handPointLeft: faHandPointLeft,
  handPointDown: faHandPointDown,
};

export enum FAIconType {
  handPointer = 'handPointer',
  handPointUp = 'handPointUp',
  handPointDown = 'handPointDown',
  handPointLeft = 'handPointLeft',
  handPointRight = 'handPointRight',
  film = 'film',
  square = 'square',
  arrowLeft = 'arrowLeft',
  squareCheck = 'squareCheck',
  clapperBoard = 'clapperBoard',
  mouse = 'mouse',
  shapes = 'shapes',
  keyboard = 'keyboard',
  video = 'video',
  university = 'university',
  photoFilm = 'photoFilm',
  videoSlash = 'videoSlash',
  videoCamera = 'videoCamera',
  map = 'map',
  fileText = 'fileText',
  tags = 'tags',
  folder = 'folder',
  fileImage = 'fileImage',
  userMinus = 'userMinus',
  fileWaveForm = 'fileWaveForm',
  images = 'images',
  arrowPointer = 'arrowPointer',
  arrowsUpDownLeftRight = 'arrowsUpDownLeftRight',
  plus = 'plus',
  circleHalfStroke = 'circleHalfStroke',
  broom = 'broom',
  filter = 'filter',
  circleDown = 'circleDown',
  circleUp = 'circleUp',
  arrowUpFromBracket = 'arrowUpFromBracket',
  home = 'home',
  locatioNDot = 'locationDot',
  upRightAndDownLeftFromCenter = 'upRightAndDownLeftFromCenter',
  file = 'file',
  penNib = 'penNib',
  message = 'message',
  towerBroadcast = 'towerBroadcast',
  microphoneAlt = 'microphoneAlt',
  microphoneAltSlash = 'microphoneAltSlash',
  barsProgress = 'barsProgress',
  bookmark = 'bookmark',
  circleQuestion = 'circleQuestion',
  userPlus = 'userPlus',
  question = 'question',
  key = 'key',
  eye = 'eye',
  eyeSlash = 'eyeSlash',
  play = 'play',
  refresh = 'refresh',
  playCircle = 'playCircle',
  stop = 'stop',
  stopCircle = 'stopCircle',
  pause = 'pause',
  pauseCircle = 'pauseCircle',
  spinner = 'spinner',
  image = 'image',
  camera = 'camera',
  magnifyingGlass = 'magnifyingGlass',
  arrowRightToBracket = 'arrowRightToBracket',
  caretUp = 'caretUp',
  caretDown = 'caretDown',
  arrowUp = 'arrowUp',
  arrowDown = 'arrowDown',
  xmark = 'xmark',
  search = 'search',
  warning = 'warning',
  download = 'download',
  glasses = 'glasses',
  noteSticky = 'noteSticky',
  bug = 'bug',
  rss = 'rss',
  cubesStacked = 'cubesStacked',
  temperatureFull = 'temperatureFull',
  cloudSunRain = 'cloudSunRain',
  pen = 'pen',
  cogs = 'cogs',
  user = 'user',
  google = 'google',
  anglesUp = 'anglesUp',
  check = 'check',
  anglesDown = 'anglesDown',
  trash = 'trash',
  ban = 'ban',
  robot = 'robot',
  squarePen = 'squarePen',
  triangleExclamation = 'triangleExclamation',
  circleInfo = 'circleInfo',
  circleCheck = 'circleCheck',
  circleChevronLeft = 'circleChevronLeft',
  circleChevronRight = 'circleChevronRight',
  circleChevronUp = 'circleChevronUp',
  circleChevronDown = 'circleChevronDown',
  chevronRight = 'chevronRight',
  circleXmark = 'circleXmark',
  circle = 'circle',
  circleNotch = 'circleNotch',
  chevronUp = 'chevronUp',
  chevronDown = 'chevronDown',
  chevronLeft = 'chevronLeft',
  book = 'book',
  paperPlane = 'paperPlane',
  floppyDisk = 'floppyDisk',
  save = 'save',
}
export interface WeatherIcon {
  label: string;
  icon: string;
}

export interface WeatherIcons {
  [index: string]: WeatherIcon;
}

export const weatherIcons: WeatherIcons = {
  '200': {
    label: 'thunderstorm with light rain',
    icon: 'storm-showers',
  },
  '201': {
    label: 'thunderstorm with rain',
    icon: 'storm-showers',
  },
  '202': {
    label: 'thunderstorm with heavy rain',
    icon: 'storm-showers',
  },
  '210': {
    label: 'light thunderstorm',
    icon: 'storm-showers',
  },
  '211': {
    label: 'thunderstorm',
    icon: 'thunderstorm',
  },
  '212': {
    label: 'heavy thunderstorm',
    icon: 'thunderstorm',
  },
  '221': {
    label: 'ragged thunderstorm',
    icon: 'thunderstorm',
  },
  '230': {
    label: 'thunderstorm with light drizzle',
    icon: 'storm-showers',
  },
  '231': {
    label: 'thunderstorm with drizzle',
    icon: 'storm-showers',
  },
  '232': {
    label: 'thunderstorm with heavy drizzle',
    icon: 'storm-showers',
  },
  '300': {
    label: 'light intensity drizzle',
    icon: 'sprinkle',
  },
  '301': {
    label: 'drizzle',
    icon: 'sprinkle',
  },
  '302': {
    label: 'heavy intensity drizzle',
    icon: 'sprinkle',
  },
  '310': {
    label: 'light intensity drizzle rain',
    icon: 'sprinkle',
  },
  '311': {
    label: 'drizzle rain',
    icon: 'sprinkle',
  },
  '312': {
    label: 'heavy intensity drizzle rain',
    icon: 'sprinkle',
  },
  '313': {
    label: 'shower rain and drizzle',
    icon: 'sprinkle',
  },
  '314': {
    label: 'heavy shower rain and drizzle',
    icon: 'sprinkle',
  },
  '321': {
    label: 'shower drizzle',
    icon: 'sprinkle',
  },
  '500': {
    label: 'light rain',
    icon: 'rain',
  },
  '501': {
    label: 'moderate rain',
    icon: 'rain',
  },
  '502': {
    label: 'heavy intensity rain',
    icon: 'rain',
  },
  '503': {
    label: 'very heavy rain',
    icon: 'rain',
  },
  '504': {
    label: 'extreme rain',
    icon: 'rain',
  },
  '511': {
    label: 'freezing rain',
    icon: 'rain-mix',
  },
  '520': {
    label: 'light intensity shower rain',
    icon: 'showers',
  },
  '521': {
    label: 'shower rain',
    icon: 'showers',
  },
  '522': {
    label: 'heavy intensity shower rain',
    icon: 'showers',
  },
  '531': {
    label: 'ragged shower rain',
    icon: 'showers',
  },
  '600': {
    label: 'light snow',
    icon: 'snow',
  },
  '601': {
    label: 'snow',
    icon: 'snow',
  },
  '602': {
    label: 'heavy snow',
    icon: 'snow',
  },
  '611': {
    label: 'sleet',
    icon: 'sleet',
  },
  '612': {
    label: 'shower sleet',
    icon: 'sleet',
  },
  '615': {
    label: 'light rain and snow',
    icon: 'rain-mix',
  },
  '616': {
    label: 'rain and snow',
    icon: 'rain-mix',
  },
  '620': {
    label: 'light shower snow',
    icon: 'rain-mix',
  },
  '621': {
    label: 'shower snow',
    icon: 'rain-mix',
  },
  '622': {
    label: 'heavy shower snow',
    icon: 'rain-mix',
  },
  '701': {
    label: 'mist',
    icon: 'sprinkle',
  },
  '711': {
    label: 'smoke',
    icon: 'smoke',
  },
  '721': {
    label: 'haze',
    icon: 'day-haze',
  },
  '731': {
    label: 'sand, dust whirls',
    icon: 'cloudy-gusts',
  },
  '741': {
    label: 'fog',
    icon: 'fog',
  },
  '751': {
    label: 'sand',
    icon: 'cloudy-gusts',
  },
  '761': {
    label: 'dust',
    icon: 'dust',
  },
  '762': {
    label: 'volcanic ash',
    icon: 'smog',
  },
  '771': {
    label: 'squalls',
    icon: 'day-windy',
  },
  '781': {
    label: 'tornado',
    icon: 'tornado',
  },
  '800': {
    label: 'clear sky',
    icon: 'sunny',
  },
  '801': {
    label: 'few clouds',
    icon: 'cloudy',
  },
  '802': {
    label: 'scattered clouds',
    icon: 'cloudy',
  },
  '803': {
    label: 'broken clouds',
    icon: 'cloudy',
  },
  '804': {
    label: 'overcast clouds',
    icon: 'cloudy',
  },
  '900': {
    label: 'tornado',
    icon: 'tornado',
  },
  '901': {
    label: 'tropical storm',
    icon: 'hurricane',
  },
  '902': {
    label: 'hurricane',
    icon: 'hurricane',
  },
  '903': {
    label: 'cold',
    icon: 'snowflake-cold',
  },
  '904': {
    label: 'hot',
    icon: 'hot',
  },
  '905': {
    label: 'windy',
    icon: 'windy',
  },
  '906': {
    label: 'hail',
    icon: 'hail',
  },
  '951': {
    label: 'calm',
    icon: 'sunny',
  },
  '952': {
    label: 'light breeze',
    icon: 'cloudy-gusts',
  },
  '953': {
    label: 'gentle breeze',
    icon: 'cloudy-gusts',
  },
  '954': {
    label: 'moderate breeze',
    icon: 'cloudy-gusts',
  },
  '955': {
    label: 'fresh breeze',
    icon: 'cloudy-gusts',
  },
  '956': {
    label: 'strong breeze',
    icon: 'cloudy-gusts',
  },
  '957': {
    label: 'high wind, near gale',
    icon: 'cloudy-gusts',
  },
  '958': {
    label: 'gale',
    icon: 'cloudy-gusts',
  },
  '959': {
    label: 'severe gale',
    icon: 'cloudy-gusts',
  },
  '960': {
    label: 'storm',
    icon: 'thunderstorm',
  },
  '961': {
    label: 'violent storm',
    icon: 'thunderstorm',
  },
  '962': {
    label: 'hurricane',
    icon: 'cloudy-gusts',
  },
};

export const beaufortGrades = [
  { speed: 0, desc: { en: 'Calm', es: 'Calma' } },
  { speed: 2, desc: { en: 'Light air', es: 'Ventolina' } },
  { speed: 6, desc: { en: 'Light breeze', es: 'Brisa muy débil' } },
  { speed: 12, desc: { en: 'Gentle breeze', es: 'Brisa ligera' } },
  { speed: 20, desc: { en: 'Moderate breeze', es: 'Brisa moderada' } },
  { speed: 29, desc: { en: 'Fresh breeze', es: 'Brisa fresca' } },
  { speed: 39, desc: { en: 'Strong breeze', es: 'Brisa fuerte' } },
  { speed: 50, desc: { en: 'High wind', es: 'Viento fuerte' } },
  { speed: 62, desc: { en: 'Gale', es: 'Temporal' } },
  { speed: 75, desc: { en: 'Strong gale', es: 'Temporal fuerte' } },
  { speed: 89, desc: { en: 'Storm', es: 'Temporal duro' } },
  { speed: 103, desc: { en: 'Violent Storm', es: 'Borrasca' } },
  { speed: 118, desc: { en: 'Hurricane', es: 'Huracán' } },
];

export const windDirectionsFrom = [
  { grade: 0, code: 'towards-0-deg' },
  { grade: 23, code: 'towards-23-deg' },
  { grade: 45, code: 'towards-45-deg' },
  { grade: 68, code: 'towards-68-deg' },
  { grade: 90, code: 'towards-90-deg' },
  { grade: 113, code: 'towards-113-deg' },
  { grade: 135, code: 'towards-135-deg' },
  { grade: 158, code: 'towards-158-deg' },
  { grade: 180, code: 'towards-180-deg' },
  { grade: 203, code: 'towards-203-deg' },
  { grade: 225, code: 'towards-225-deg' },
  { grade: 248, code: 'towards-248-deg' },
  { grade: 270, code: 'towards-270-deg' },
  { grade: 293, code: 'towards-293-deg' },
  { grade: 313, code: 'towards-313-deg' },
  { grade: 336, code: 'towards-336-deg' },
];
export const windDirectionsTowards = [
  { grade: 0, code: 'from-0-deg' },
  { grade: 23, code: 'from-23-deg' },
  { grade: 45, code: 'from-45-deg' },
  { grade: 68, code: 'from-68-deg' },
  { grade: 90, code: 'from-90-deg' },
  { grade: 113, code: 'from-113-deg' },
  { grade: 135, code: 'from-135-deg' },
  { grade: 158, code: 'from-158-deg' },
  { grade: 180, code: 'from-180-deg' },
  { grade: 203, code: 'from-203-deg' },
  { grade: 225, code: 'from-225-deg' },
  { grade: 248, code: 'from-248-deg' },
  { grade: 270, code: 'from-270-deg' },
  { grade: 293, code: 'from-293-deg' },
  { grade: 313, code: 'from-313-deg' },
  { grade: 336, code: 'from-336-deg' },
];

export const WIIcons = {
  wiFahrenheiht: 'wi wi-fahrenheit',
  wiCelsius: 'wi wi-celsius',
  wiSunrise: 'wi wi-sunrise',
  wiSunset: 'wi wi-sunset',
  wiHumidity: 'wi wi-humidity',
  wiRainDrop: 'wi wi-raindrop',
  wiStrongWind: 'wi wi-strong-wind',
  wiThermometer: 'wi wi-thermometer',
  wiUmbrella: 'wi wi-umbrella',
  wiBarometer: 'wi wi-barometer',
  wiDaySunny: 'wi wi-day-sunny',

  fromClock: function (hour: number): string {
    let numb = 12;
    if (hour == 0 || hour == 12 || hour == 24) {
      numb = 12;
    } else if (hour > 0 && hour <= 12) {
      numb = hour;
    } else if (hour > 12) {
      numb = hour - 12;
    }

    return 'wi wi-time-' + numb.toString();
  },

  fromCode: function (code: number): string {
    var prefix = 'wi wi-';

    var icon = 'sunny';
    try {
      icon = weatherIcons[code.toString()].icon;
    } catch (err) {
      icon = 'sunny';
    }

    // If we are not in the ranges mentioned above, add a day/night prefix.

    if (!(code > 699 && code < 800) && !(code > 899 && code < 1000)) {
      icon = 'day-' + icon;
    }

    // Finally tack on the prefix.
    icon = prefix + icon;
    return icon;
  },

  directionFromWind: function (angle: number): string {
    var prefix = 'wi wi-wind ';
    var code: string = 'from-313-deg';
    for (let i = 0; i < windDirectionsFrom.length; i++) {
      if (angle <= windDirectionsFrom[i].grade) {
        code = windDirectionsFrom[i].code;
        break;
      }
    }
    return prefix + code;
  },

  directionToWind: function (angle: number): string {
    var prefix = 'wi wi-wind ';
    var code: string = 'from-313-deg';
    for (let i = 0; i < windDirectionsTowards.length; i++) {
      if (angle <= windDirectionsTowards[i].grade) {
        code = windDirectionsTowards[i].code;
        break;
      }
    }
    return prefix + code;
  },

  beaufortFromWind: function (speed: number): string {
    var prefix = 'wi wi-wind-beaufort-';
    let real_speed = 1.852 * speed;
    let scale = 0;
    for (let i = 0; i < beaufortGrades.length; i++) {
      if (real_speed <= beaufortGrades[i].speed) {
        scale = i;
        break;
      }
    }
    return prefix + scale.toString();
  },
};
