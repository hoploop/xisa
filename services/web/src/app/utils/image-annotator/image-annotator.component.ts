import {
  AfterViewInit,
  Component,
  ElementRef,
  EventEmitter,
  Input,
  OnDestroy,
  OnInit,
  Output,
  ViewChild,
} from '@angular/core';
import { ContextService } from '@services/context.service';
import { ImageAnnotatorSettings } from './image-annotator-settings';
import {
  ImageAnnotatorBox,
  ImageAnnotatorMouseOverType,
} from './image-annotator-box';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { BehaviorSubject, Observable, Subscription } from 'rxjs';
import { ImageAnnotatorHighlight } from './image-annotator-highlight';

export enum State {
  EMPTY = 0,
  SELECTED = 1,
  ADDING = 2,
  RESIZING = 3,
  MOVING = 4,
}

@Component({
  selector: 'app-image-annotator',
  standalone: false,
  templateUrl: './image-annotator.component.html',
  styleUrl: './image-annotator.component.scss',
})
export class ImageAnnotatorComponent
  implements AfterViewInit, OnInit, OnDestroy
{
  @ViewChild('canvasElement', { static: false })
  canvas!: ElementRef<HTMLCanvasElement>;
  @Input() dataUrl?: string;
  @Input() url?: string =
    'http://localhost:8000/record/frame/67dad716d009b25b6b6e66e5/21';
  @Input() detectorId: string = '67caa7b79fc10dc8e8afaf24';
  @Output() doubleClicked = new EventEmitter<ImageAnnotatorBox>();
  @Input() boxes = new BehaviorSubject<ImageAnnotatorBox[]>([]);
  @Input() highlights = new BehaviorSubject<ImageAnnotatorHighlight[]>([]);
  @Output() onSelectedBox: EventEmitter<ImageAnnotatorBox> = new EventEmitter();
  @Output() boxesChange = new EventEmitter<ImageAnnotatorBox[]>();
  @Output() onBoxCreated = new EventEmitter<ImageAnnotatorBox>();
  @Output() onBoxUpdated = new EventEmitter<ImageAnnotatorBox>();
  @Output() loaded = new EventEmitter<boolean>();
  @Input() settings = new BehaviorSubject<ImageAnnotatorSettings>({
    resizeHandleSize: 10,
    showHighlights: true,
    canCreateBox: true,
  });
  private context!: CanvasRenderingContext2D;
  private image = new Image();
  selectedBoxIndex: number = -1;
  selectedHighlightIndex: number = -1;
  subs = new Subscription();

  state: State = State.EMPTY;
  mouse = {
    x: 0,
    y: 0,
    cursor: 'default',
  };
  adding = {
    startX: 0,
    startY: 0,
  };
  moving = {
    startX: 0,
    startY: 0,
  };
  resizing = {
    startX: 0,
    startY: 0,
    type: ImageAnnotatorMouseOverType.NOT_OVER,
  };

  ngOnDestroy(): void {
    this.subs.unsubscribe();
  }

  ngOnInit(): void {
    this.subs.add(
      this.boxes.subscribe((boxes) => {
        if (this.context && this.canvas) {
          boxes.forEach(box=>{
            this.normalizeInitialBox(box);
          })

          this.draw();
        }
      })
    );

    this.subs.add(
      this.highlights.subscribe((highlights)=>{
        if (this.context && this.canvas) {
          highlights.forEach(highlight=>{
            //this.normalizeInitialHighlight(highlight);
          })

          this.draw();
        }
      })
    )
  }

  constructor(private ctx: ContextService, private http: HttpClient) {}

  ngAfterViewInit(): void {
    setTimeout(() => {
      this.context = this.canvas.nativeElement.getContext('2d')!;
      if (this.dataUrl) {
        this.loadBase64Image(this.dataUrl);
      } else if (this.url) {
        this.loadUrlImage(this.url);
      }
    });
  }

  // Method to get image as Blob from FastAPI
  getUrlImage(url: string): Observable<HttpResponse<Blob>> {
    const headers = new HttpHeaders().set(
      'Authorization',
      'Bearer ' + this.ctx.api.getToken() || ''
    );

    return this.http.get(url, {
      headers,
      responseType: 'blob', // This ensures the response is a Blob
      observe: 'response', // Observe the full response to get both headers and body
    });
  }

  handleLoadUrlImage(response: HttpResponse<Blob>) {
    this.image.onload = () => {
      setTimeout(() => {
        this.resizeCanvas();
        this.loaded.next(true);
      });
    };

    this.image.onerror = () => {
      console.error('Failed to load base64 image');
    };

    if (response.body) {
      this.image.src = URL.createObjectURL(response.body);
    }
  }

  loadUrlImage(url: string) {
    this.getUrlImage(url).subscribe(
      (response: HttpResponse<Blob>) => {
        this.handleLoadUrlImage(response);
      },
      (error) => {
        console.error('Error loading image:', error);
      }
    );
  }

  loadBase64Image(base64String: string): void {
    this.image.onload = () => {
      setTimeout(() => {
        this.resizeCanvas();
        this.loaded.next(true);
      });
    };

    this.image.onerror = () => {
      console.error('Failed to load base64 image');
    };

    this.image.src = base64String;
  }

  resizeCanvas(): void {
    this.canvas.nativeElement.width = this.image.width;
    this.canvas.nativeElement.height = this.image.height;
    this.boxes.getValue().forEach((box) => {
      this.normalizeInitialBox(box);
    });
    this.draw();
  }

  roundedImage(
    x: number,
    y: number,
    width: number,
    height: number,
    radius: number
  ) {
    this.context.beginPath();
    this.context.moveTo(x + radius, y);
    this.context.lineTo(x + width - radius, y);
    this.context.quadraticCurveTo(x + width, y, x + width, y + radius);
    this.context.lineTo(x + width, y + height - radius);
    this.context.quadraticCurveTo(
      x + width,
      y + height,
      x + width - radius,
      y + height
    );
    this.context.lineTo(x + radius, y + height);
    this.context.quadraticCurveTo(x, y + height, x, y + height - radius);
    this.context.lineTo(x, y + radius);
    this.context.quadraticCurveTo(x, y, x + radius, y);
    this.context.closePath();
  }

  drawImage(x: number, y: number, image: any) {
    this.context.drawImage(image, x, y, image.width, image.height);
  }

  draw(): void {
    this.context.clearRect(
      0,
      0,
      this.canvas.nativeElement.width,
      this.canvas.nativeElement.height
    );
    this.context.save();
    this.roundedImage(
      0,
      0,
      this.canvas.nativeElement.width,
      this.canvas.nativeElement.height,
      3
    );
    this.context.clip();
    this.context.drawImage(
      this.image,
      0,
      0,
      this.canvas.nativeElement.width,
      this.canvas.nativeElement.height
    );
    this.context.restore();

    this.boxes.getValue().forEach((box, index) => {
      box.draw(this.context, this.settings.getValue(), this.image);
    });

    this.highlights.getValue().forEach((highlight)=>{
      highlight.draw(this.context,this.settings.getValue(),this.image);
    })

    this.boxesChange.next(this.denormalizeOutputBoxes(this.boxes.getValue()));
  }

  addBox(event: MouseEvent): void {
    const rect = this.canvas.nativeElement.getBoundingClientRect();
    const mouseX = event.clientX - rect.left;
    const mouseY = event.clientY - rect.top;
    let boxes = this.boxes.getValue();
    let nbox = new ImageAnnotatorBox(mouseX, mouseY, 100, 100)
    boxes.push(nbox);
    this.boxes.next(boxes);
    this.boxesChange.next(this.denormalizeOutputBoxes(boxes));
    this.draw();
  }

  updateSelectedBox() {
    let cbox = this.selectedBox;
    if (cbox != undefined) {
      this.onSelectedBox.next(cbox);
    }
  }

  get selectedBox(): ImageAnnotatorBox | undefined {
    if (this.selectedBoxIndex == -1) return undefined;
    return this.boxes.getValue()[this.selectedBoxIndex];
  }

  getScales(): number[] {
    const canvas = this.canvas.nativeElement;
    const rect = canvas.getBoundingClientRect(); // Get canvas position & size

    // Scaling factor: Adjust for responsive canvas
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;
    return [scaleX, scaleY];
  }

  updateMousePosition(event: MouseEvent) {
    const canvas = this.canvas.nativeElement;
    const rect = canvas.getBoundingClientRect(); // Get canvas position & size

    // Scaling factor: Adjust for responsive canvas
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;

    // Adjusted X, Y relative to canvas scale
    const x = (event.clientX - rect.left) * scaleX;
    const y = (event.clientY - rect.top) * scaleY;
    this.mouse.x = x;
    this.mouse.y = y;
  }

  normalizeInitialBox(box: ImageAnnotatorBox) {
    const canvas = this.canvas.nativeElement;
    const rect = canvas.getBoundingClientRect(); // Get canvas position & size

    // Scaling factor: Adjust for responsive canvas
    const scaleX = canvas.width;// / rect.width;
    const scaleY = canvas.height;// / rect.height;
    if (box.percentage){
      box.x = box.x * scaleX;
      box.y = box.y * scaleY;
      box.w = box.w * scaleX;
      box.h = box.h * scaleY;
    }

  }


  normalizeInitialHighlight(highlight: ImageAnnotatorHighlight) {
    const canvas = this.canvas.nativeElement;
    const rect = canvas.getBoundingClientRect(); // Get canvas position & size

    // Scaling factor: Adjust for responsive canvas
    const scaleX = canvas.width;// / rect.width;
    const scaleY = canvas.height;// / rect.height;
    if (highlight.percentage){
      highlight.x = highlight.x * scaleX;
      highlight.y = highlight.y * scaleY;
      highlight.w = highlight.w * scaleX;
      highlight.h = highlight.h * scaleY;
    }

  }

  denormalizeOutputBoxes(boxes: ImageAnnotatorBox[]): ImageAnnotatorBox[] {
    let ret: ImageAnnotatorBox[] = [];
    boxes.forEach((box) => {
      ret.push(this.denormalizeOutputBox(box));
    });
    return ret;
  }

  denormalizeOutputBox(box: ImageAnnotatorBox): ImageAnnotatorBox {
    const canvas = this.canvas.nativeElement;
    const rect = canvas.getBoundingClientRect(); // Get canvas position & size

    // Scaling factor: Adjust for responsive canvas
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;

    let newBox = new ImageAnnotatorBox();
    newBox.x = Math.round(box.x / scaleX);
    newBox.y = Math.round(box.y / scaleY);
    newBox.w = Math.round(box.w / scaleX);
    newBox.h = Math.round(box.h / scaleY);
    return newBox;
  }

  onMouseDoubleClick(event: MouseEvent) {
    this.updateMousePosition(event);
    let overType: ImageAnnotatorMouseOverType =
      ImageAnnotatorMouseOverType.NOT_OVER;
    let boxOver: ImageAnnotatorBox | undefined = undefined;
    let boxOverIndex: number = -1;
    this.selectedBoxIndex = -1;
    for (let i = 0; i < this.boxes.getValue().length; i++) {
      let box = this.boxes.getValue()[i];
      let boxOverType = box.isMouseOver(
        this.settings.getValue(),
        this.mouse.x,
        this.mouse.y
      );
      if (boxOverType == ImageAnnotatorMouseOverType.INSIDE) {
        boxOver = box;
        overType = boxOverType;
        this.doubleClicked.next(box);
        break;
      }
    }
  }

  //@HostListener('mousedown', ['$event'])
  onMouseDown(event: MouseEvent): void {
    this.updateMousePosition(event);

    let overType: ImageAnnotatorMouseOverType =
      ImageAnnotatorMouseOverType.NOT_OVER;
    let boxOver: ImageAnnotatorBox | undefined = undefined;
    let boxOverIndex: number = -1;
    this.selectedBoxIndex = -1;
    this.selectedHighlightIndex = -1;
    this.updateSelectedBox();
    for (let i = 0; i < this.boxes.getValue().length; i++) {
      let box = this.boxes.getValue()[i];
      let boxOverType = box.isMouseOver(
        this.settings.getValue(),
        this.mouse.x,
        this.mouse.y
      );
      if (boxOverType != ImageAnnotatorMouseOverType.NOT_OVER) {
        boxOver = box;
        overType = boxOverType;
        boxOverIndex = i;
        if (boxOver.canSelect){
          boxOver.isSelected = true;
          this.selectedBoxIndex = i;
          this.updateSelectedBox();
        }
      } else {
        box.isSelected = false;
      }
    }

    if (overType == ImageAnnotatorMouseOverType.NOT_OVER) {
      if (this.settings.getValue().canCreateBox) {
        this.state = State.ADDING;
        this.adding.startX = this.mouse.x;
        this.adding.startY = this.mouse.y;
        let boxes = this.boxes.getValue();
        let nbox = new ImageAnnotatorBox(
          this.mouse.x,
          this.mouse.y,
          this.settings.getValue().resizeHandleSize,
          this.settings.getValue().resizeHandleSize
        );
        boxes.push(nbox);
        this.selectedBoxIndex = boxes.length - 1;
        boxes[boxes.length - 1].isSelected = true;
        this.boxes.next(boxes);
        this.updateSelectedBox();
        this.boxesChange.next(this.denormalizeOutputBoxes(boxes));
        this.onBoxCreated.next(nbox)
        this.draw();
      }
    } else if (overType == ImageAnnotatorMouseOverType.INSIDE) {
      if (boxOver) {
        if (boxOver.canMove) {
          this.state = State.MOVING;
          this.moving.startX = this.mouse.x - boxOver.x;
          this.moving.startY = this.mouse.y - boxOver.y;
        }else{
          if (boxOver.canSelect)
          this.state = State.SELECTED;
        }
        if (boxOver.canSelect){
        this.selectedBoxIndex = boxOverIndex;
        this.updateSelectedBox();
        boxOver.isSelected = true;
        }
      }
    } else {
      if (boxOver) {
        if (boxOver.canResize) {
          this.state = State.RESIZING;
          this.resizing.type = overType;
          this.resizing.startX = this.mouse.x;
          this.resizing.startY = this.mouse.y;
        }else{
          this.state = State.SELECTED;
        }
        this.selectedBoxIndex = boxOverIndex;
        this.updateSelectedBox();
      }
    }
  }

  //@HostListener('mousemove', ['$event'])
  onMouseMove(event: MouseEvent): void {
    this.updateMousePosition(event);

    // Adding Mode
    if (this.state == State.ADDING) {
      let w = Math.abs(this.mouse.x - this.adding.startX);
      let h = Math.abs(this.mouse.y - this.adding.startY);
      let x = Math.min(this.adding.startX, this.mouse.x);
      let y = Math.min(this.adding.startY, this.mouse.y);
      let box = this.selectedBox;
      if (box != undefined) {
        box.x = x;
        box.y = y;
        box.w = w;
        box.h = h;
        this.draw();
      }
    } else if (this.state == State.SELECTED) {
    } else if (this.state == State.EMPTY) {
    }

    // Moving Mode
    else if (this.state == State.MOVING) {
      this.mouse.cursor = 'move';
      let box = this.selectedBox;
      if (box != undefined) {
        let x = this.mouse.x - this.moving.startX;
        let y = this.mouse.y - this.moving.startY;
        box.x = x;
        box.y = y;
        this.draw();
      }
    } else if (this.state == State.RESIZING) {
      let box = this.selectedBox;
      if (box != undefined) {
        if (this.resizing.type == ImageAnnotatorMouseOverType.BOTTOM) {
          if (this.mouse.y > box.y) {
            box.h = this.mouse.y - box.y;
          }
        } else if (this.resizing.type == ImageAnnotatorMouseOverType.TOP) {
          if (this.mouse.y < box.y + box.h) {
            box.h = box.y + box.h - this.mouse.y;
            box.y = this.mouse.y;
          }
        } else if (this.resizing.type == ImageAnnotatorMouseOverType.LEFT) {
          if (this.mouse.x < box.x + box.w) {
            box.w = box.x + box.w - this.mouse.x;
            box.x = this.mouse.x;
          }
        }
        if (this.resizing.type == ImageAnnotatorMouseOverType.RIGHT) {
          if (this.mouse.x > box.x) {
            box.w = this.mouse.x - box.x;
          }
        }
        if (this.resizing.type == ImageAnnotatorMouseOverType.TOP_RIGHT) {
          if (this.mouse.y < box.y + box.h) {
            box.h = box.y + box.h - this.mouse.y;
            box.y = this.mouse.y;
          }
          if (this.mouse.x > box.x) {
            box.w = this.mouse.x - box.x;
          }
        }
        if (this.resizing.type == ImageAnnotatorMouseOverType.TOP_LEFT) {
          if (this.mouse.y < box.y + box.h) {
            box.h = box.y + box.h - this.mouse.y;
            box.y = this.mouse.y;
          }
          if (this.mouse.x < box.x + box.w) {
            box.w = box.x + box.w - this.mouse.x;
            box.x = this.mouse.x;
          }
        }
        if (this.resizing.type == ImageAnnotatorMouseOverType.BOTTOM_RIGHT) {
          if (this.mouse.y > box.y) {
            box.h = this.mouse.y - box.y;
          }
          if (this.mouse.x > box.x) {
            box.w = this.mouse.x - box.x;
          }
        }
        if (this.resizing.type == ImageAnnotatorMouseOverType.BOTTOM_LEFT) {
          if (this.mouse.y > box.y) {
            box.h = this.mouse.y - box.y;
          }
          if (this.mouse.x < box.x + box.w) {
            box.w = box.x + box.w - this.mouse.x;
            box.x = this.mouse.x;
          }
        }
        this.draw();
      }
    }
    this.updateCursor();
  }

  updateCursor() {
    let overType: ImageAnnotatorMouseOverType =
      ImageAnnotatorMouseOverType.NOT_OVER;
    let boxOver: ImageAnnotatorBox | undefined = undefined;
    let boxOverIndex: number = -1;
    for (let i = 0; i < this.boxes.getValue().length; i++) {
      let box = this.boxes.getValue()[i];
      let boxOverType = box.isMouseOver(
        this.settings.getValue(),
        this.mouse.x,
        this.mouse.y
      );
      if (boxOverType != ImageAnnotatorMouseOverType.NOT_OVER) {
        boxOver = box;
        overType = boxOverType;
        boxOverIndex = i;
        break;
      }
    }

    if (overType == ImageAnnotatorMouseOverType.BOTTOM_RIGHT) {
      this.mouse.cursor = 'nwse-resize';
    } else if (overType == ImageAnnotatorMouseOverType.BOTTOM_LEFT) {
      this.mouse.cursor = 'nesw-resize';
    } else if (overType == ImageAnnotatorMouseOverType.TOP_LEFT) {
      this.mouse.cursor = 'nwse-resize';
    } else if (overType == ImageAnnotatorMouseOverType.TOP_RIGHT) {
      this.mouse.cursor = 'nesw-resize';
    } else if (overType == ImageAnnotatorMouseOverType.TOP) {
      this.mouse.cursor = 'ns-resize';
    } else if (overType == ImageAnnotatorMouseOverType.BOTTOM) {
      this.mouse.cursor = 'ns-resize';
    } else if (overType == ImageAnnotatorMouseOverType.LEFT) {
      this.mouse.cursor = 'ew-resize';
    } else if (overType == ImageAnnotatorMouseOverType.RIGHT) {
      this.mouse.cursor = 'ew-resize';
    } else if (overType == ImageAnnotatorMouseOverType.INSIDE) {
      if (boxOver?.canMove){
      this.mouse.cursor = 'move';
      }else{this.mouse.cursor = 'default';}
    } else if (overType == ImageAnnotatorMouseOverType.NOT_OVER) {
      this.mouse.cursor = 'default';
    }

    this.canvas.nativeElement.style.cursor = this.mouse.cursor;
  }

  onKeyUp(event: KeyboardEvent): void {
    if (event.key == 'Backspace' && this.selectedBoxIndex != -1) {
      let boxes = this.boxes.getValue();
      boxes.splice(this.selectedBoxIndex, 1);
      this.boxes.next(boxes);
      this.boxesChange.next(this.denormalizeOutputBoxes(boxes));
      this.draw();
    }
  }

  onMouseUp(event: MouseEvent): void {
    this.updateMousePosition(event);

    if (this.state == State.ADDING) {
      let w = Math.abs(this.mouse.x - this.adding.startX);
      let h = Math.abs(this.mouse.y - this.adding.startY);
      let x = Math.min(this.adding.startX, this.mouse.x);
      let y = Math.min(this.adding.startY, this.mouse.y);
      if (w > 10 && h > 10) {
        let box = this.selectedBox;
        if (box != undefined) {
          box.x = x;
          box.y = y;
          box.w = w;
          box.h = h;
          this.draw();
        }
        this.state = State.SELECTED;
      } else {
        let boxes = this.boxes.getValue();
        boxes.splice(this.selectedBoxIndex, 1);
        this.boxes.next(boxes);
        this.boxesChange.next(this.denormalizeOutputBoxes(boxes));
        this.state = State.SELECTED;
        this.draw();
      }
    } else if (this.state == State.RESIZING) {
      let box = this.selectedBox;
      if (box != undefined) {
        this.onBoxUpdated.next(box);
      }


      this.state = State.SELECTED;
      this.draw();
    } else if (this.state == State.MOVING) {
      let box = this.selectedBox;
      if (box != undefined) {
        this.onBoxUpdated.next(box);
      }
      this.state = State.SELECTED;
      this.moving.startX = 0;
      this.moving.startY = 0;
      this.draw();
    } else if (this.state == State.SELECTED){
      this.draw();
    }
  }

  onMouseLeave(event: MouseEvent): void {
    const rect = this.canvas.nativeElement.getBoundingClientRect();
    const mouseX = event.clientX - rect.left;
    const mouseY = event.clientY - rect.top;
  }

  deleteSelectedBox(): void {
    if (this.selectedBoxIndex !== null) {
      let boxes = this.boxes.getValue();
      boxes.splice(this.selectedBoxIndex, 1);
      this.boxes.next(boxes);
      this.boxesChange.next(this.denormalizeOutputBoxes(boxes));
      this.selectedBoxIndex = -1;
      this.draw();
    }
  }


}
