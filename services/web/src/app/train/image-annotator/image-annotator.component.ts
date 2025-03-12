import {
  AfterViewInit,
  Component,
  ElementRef,
  HostListener,
  Input,
  OnDestroy,
  ViewChild,
} from '@angular/core';
import { FAIconType } from '@constants/icons';
import { ContextService } from '@services/context.service';
import { BehaviorSubject } from 'rxjs';

export interface Box {
  x: number;
  y: number;
  width: number;
  height: number;
  isResizing?: boolean;
  isDragging?: boolean;
  imageUrl?: string;
}

enum State {
  EMPTY = 0,
  ADD = 1,
  RESIZE = 2,
  MOVE = 3,
  SELECT = 4
}

enum ResizeHandle {
  TOP_LEFT = 0,
  TOP = 1,
  TOP_RIGHT = 2,
  RIGHT = 3,
  BOTTOM_RIGHT = 4,
  BOTTOM = 5,
  BOTTOM_LEFT = 6,
  LEFT = 7,
}

@Component({
  selector: 'app-image-annotator',
  standalone: false,
  templateUrl: './image-annotator.component.html',
  styleUrl: './image-annotator.component.scss',
})
export class ImageAnnotatorComponent implements AfterViewInit {
  @Input() fileId?: string;
  loading = new BehaviorSubject<string | undefined>(undefined);
  error = new BehaviorSubject<string | undefined>(undefined);

  @ViewChild('canvasElement', { static: false })
  canvas!: ElementRef<HTMLCanvasElement>;
  private context!: CanvasRenderingContext2D;
  private image = new Image();
  private imageUrl?: string;
  private resizeHandleSize = 6;
  selectedBoxIndex: number = -1;
  boxes: Box[] = [];
  private state: State = State.EMPTY;
  label?:Box;

  adding = {
    startX: 0,
    startY: 0,
    endX: 0,
    endY: 0,
  };

  moving = {
    offsetX: 0,
    offsetY: 0,
  };

  resizing = {
    handle: ResizeHandle.BOTTOM,
    startX: 0,
    startY: 0,
    cursor: 'default',
  };

  constructor(private ctx: ContextService) {}

  ngAfterViewInit(): void {
    setTimeout(()=>{
      this.context = this.canvas.nativeElement.getContext('2d')!;
      this.downloadImage();
    })

  }

  downloadImage() {
    if (!this.fileId) return;
    console.log('Loading image blob');
    this.error.next(undefined);
    this.loading.next(this.ctx.translate.instant('train.image.downloading'));
    this.ctx.api.train.trainImageDownloadFileId(this.fileId) .subscribe({
      next: (result) => {
        this.loading.next(undefined);
        console.log('Loaded image blob');
        this.loadBase64Image('data:image/png;base64,' + result);
      },
      error: (result) => {
        this.loading.next(undefined);
        this.error.next(result.error.detail);
      },
    });
  }

  loadBase64Image(base64String: string): void {
    this.image.onload = () => {
      setTimeout(()=>{
        this.resizeCanvas();
      })
    };

    this.image.onerror = () => {
      console.error('Failed to load base64 image');
    };

    this.image.src = base64String;

  }

  resizeCanvas(): void {
    this.canvas.nativeElement.width = this.image.width;
    this.canvas.nativeElement.height = this.image.height;
    this.draw();
  }

  draw(): void {

    this.context.clearRect(
      0,
      0,
      this.canvas.nativeElement.width,
      this.canvas.nativeElement.height
    );
    this.context.drawImage(
      this.image,
      0,
      0,
      this.canvas.nativeElement.width,
      this.canvas.nativeElement.height
    );

    this.boxes.forEach((box, index) => {
      this.cropImageBox(index);
      this.context.strokeStyle =
        index === this.selectedBoxIndex ? 'blue' : 'red';
      this.context.fillStyle = 'rgba(255,255,255,0.2)';
      this.context.fillRect(box.x, box.y, box.width, box.height);
      this.context.lineWidth = 1;
      this.context.strokeRect(box.x, box.y, box.width, box.height);

      // Draw resize handles
      this.context.fillStyle = 'blue';
      this.context.fillRect(
        box.x + box.width - this.resizeHandleSize / 2,
        box.y + box.height - this.resizeHandleSize / 2,
        this.resizeHandleSize,
        this.resizeHandleSize
      );
      this.context.fillRect(
        box.x - this.resizeHandleSize / 2,
        box.y - this.resizeHandleSize / 2,
        this.resizeHandleSize,
        this.resizeHandleSize
      );
      this.context.fillRect(
        box.x +box.width - this.resizeHandleSize / 2,
        box.y - this.resizeHandleSize / 2,
        this.resizeHandleSize,
        this.resizeHandleSize
      );
      this.context.fillRect(
        box.x - this.resizeHandleSize / 2,
        box.y + box.height - this.resizeHandleSize / 2,
        this.resizeHandleSize,
        this.resizeHandleSize
      );
      this.context.fillRect(
        box.x - this.resizeHandleSize / 2,
        box.y + box.height/2 - this.resizeHandleSize / 2,
        this.resizeHandleSize,
        this.resizeHandleSize
      );
      this.context.fillRect(
        box.x  + box.width - this.resizeHandleSize / 2,
        box.y + box.height/2 - this.resizeHandleSize / 2,
        this.resizeHandleSize,
        this.resizeHandleSize
      );
      this.context.fillRect(
        box.x + box.width /2 - this.resizeHandleSize / 2,
        box.y - this.resizeHandleSize / 2,
        this.resizeHandleSize,
        this.resizeHandleSize
      );
      this.context.fillRect(
        box.x + box.width /2 - this.resizeHandleSize / 2,
        box.y +box.height - this.resizeHandleSize / 2,
        this.resizeHandleSize,
        this.resizeHandleSize
      );
    });
  }

  addBox(event: MouseEvent): void {
    const rect = this.canvas.nativeElement.getBoundingClientRect();
    const mouseX = event.clientX - rect.left;
    const mouseY = event.clientY - rect.top;

    this.boxes.push({
      x: mouseX,
      y: mouseY,
      width: 100,
      height: 100,
    });

    this.draw();
  }

  findBoxIndex(mouseX: number, mouseY: number): number | null {
    return this.boxes.findIndex(
      (box) =>
        mouseX >= box.x &&
        mouseX <= box.x + box.width &&
        mouseY >= box.y &&
        mouseY <= box.y + box.height
    );
  }

  isMouseOverResizeHandle(box: Box, mouseX: number, mouseY: number): boolean {
    return (
      mouseX >= box.x + box.width - this.resizeHandleSize &&
      mouseX <= box.x + box.width &&
      mouseY >= box.y + box.height - this.resizeHandleSize &&
      mouseY <= box.y + box.height
    );
  }

  isOverResizing(x: number, y: number): number {
    if (this.boxes.length == 0) return -1;
    for (let index = 0; index < this.boxes.length; index++) {
      let box = this.boxes[index];

      // Bottom Right
      if (
        x >= box.x + box.width - this.resizeHandleSize &&
        x <= box.x + box.width + this.resizeHandleSize &&
        y >= box.y + box.height - this.resizeHandleSize &&
        y <= box.y + box.height + this.resizeHandleSize
      ) {
        this.resizing.handle = ResizeHandle.BOTTOM_RIGHT;
        this.resizing.startX = box.x;
        this.resizing.startY = box.y;
        this.resizing.cursor = 'nwse-resize';
        return index;
      }

      // Top Right
      else if (
        x >= box.x + box.width - this.resizeHandleSize &&
        x <= box.x + box.width + this.resizeHandleSize &&
        y >= box.y - this.resizeHandleSize &&
        y <= box.y + this.resizeHandleSize
      ) {
        this.resizing.handle = ResizeHandle.TOP_RIGHT;
        this.resizing.startX = box.x;
        this.resizing.startY = box.y;
        this.resizing.cursor = 'nesw-resize';
        return index;
      }
      // Top LEFT
      else if (
        x >= box.x - this.resizeHandleSize &&
        x <= box.x + this.resizeHandleSize &&
        y >= box.y - this.resizeHandleSize &&
        y <= box.y + this.resizeHandleSize
      ) {
        this.resizing.handle = ResizeHandle.TOP_LEFT;
        this.resizing.startX = box.x;
        this.resizing.startY = box.y;
        this.resizing.cursor = 'nwse-resize';
        return index;
      }
      // Bottom left
      else if (
        x >= box.x - this.resizeHandleSize &&
        x <= box.x + this.resizeHandleSize &&
        y >= box.y + box.height - this.resizeHandleSize &&
        y <= box.y + box.height + this.resizeHandleSize
      ) {
        this.resizing.handle = ResizeHandle.BOTTOM_LEFT;
        this.resizing.startX = box.x;
        this.resizing.startY = box.y;
        this.resizing.cursor = 'nesw-resize';
        return index;
      }
      // LEFT
      else if (
        x >= box.x - this.resizeHandleSize &&
        x <= box.x + this.resizeHandleSize &&
        y >= box.y - this.resizeHandleSize &&
        y <= box.y + box.height + this.resizeHandleSize
      ) {
        this.resizing.handle = ResizeHandle.LEFT;
        this.resizing.startX = box.x;
        this.resizing.startY = box.y;
        this.resizing.cursor = 'ew-resize';
        return index;
      }
      // RIGHT
      else if (
        x >= box.x + box.width - this.resizeHandleSize &&
        x <= box.x + box.width + this.resizeHandleSize &&
        y >= box.y - this.resizeHandleSize &&
        y <= box.y + box.height + this.resizeHandleSize
      ) {
        this.resizing.handle = ResizeHandle.LEFT;
        this.resizing.startX = box.x;
        this.resizing.startY = box.y;
        this.resizing.cursor = 'ew-resize';
        return index;
      }
      // TOP
      else if (
        x >= box.x - this.resizeHandleSize &&
        x <= box.x + box.width + this.resizeHandleSize &&
        y >= box.y - this.resizeHandleSize &&
        y <= box.y + this.resizeHandleSize
      ) {
        this.resizing.handle = ResizeHandle.TOP;
        this.resizing.startX = box.x;
        this.resizing.startY = box.y;
        this.resizing.cursor = 'ns-resize';
        return index;
      }
      // BOTTOM
      else if (
        x >= box.x - this.resizeHandleSize &&
        x <= box.x + box.width + this.resizeHandleSize &&
        y >= box.y + box.height - this.resizeHandleSize &&
        y <= box.y + +box.height + this.resizeHandleSize
      ) {
        this.resizing.handle = ResizeHandle.BOTTOM;
        this.resizing.startX = box.x;
        this.resizing.startY = box.y;
        this.resizing.cursor = 'ns-resize';
        return index;
      }
    }
    return -1;
  }

  isOverBox(x: number, y: number): number {
    if (this.boxes.length == 0) return -1;
    for (let index = 0; index < this.boxes.length; index++) {
      let box = this.boxes[index];
      if (
        x < box.x + box.width - this.resizeHandleSize &&
        x > box.x + this.resizeHandleSize &&
        y < box.y + box.height - this.resizeHandleSize &&
        y > box.y + this.resizeHandleSize
      ) {
        return index;
      }
    }
    return -1;
  }

  getMousePosition(event:MouseEvent):[number,number] {
    const canvas = this.canvas.nativeElement;
    const rect = canvas.getBoundingClientRect(); // Get canvas position & size

    // Scaling factor: Adjust for responsive canvas
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;

    // Adjusted X, Y relative to canvas scale
    const x = (event.clientX - rect.left) * scaleX;
    const y = (event.clientY - rect.top) * scaleY;
    return [x,y]
  }



  //@HostListener('mousedown', ['$event'])
  onMouseDown(event: MouseEvent): void {
    const [mouseX, mouseY] = this.getMousePosition(event);
    console.log(`MOUSE DOWN [${mouseX},${mouseY}]`);

    // Now I can move either in SELECT mode or ADD mode or RESIZE mode
    let overResizing = this.isOverResizing(mouseX, mouseY);
    let overBox = this.isOverBox(mouseX, mouseY);
    if (overResizing != -1) {
      this.state = State.RESIZE;
      this.selectedBoxIndex = overResizing;
    } else if (overBox != -1) {
      this.state = State.MOVE;
      this.selectedBoxIndex = overBox;
      let box = this.boxes[this.selectedBoxIndex];
      this.moving.offsetX = mouseX - box.x;
      this.moving.offsetY = mouseY - box.y;
      this.draw();
    } else if (this.state == State.EMPTY) {
        this.state = State.ADD;
        this.adding.startX = mouseX;
        this.adding.startY = mouseY;
        this.boxes.push({
          x: mouseX,
          y: mouseY,
          width: this.resizeHandleSize,
          height: this.resizeHandleSize,
        });
        this.selectedBoxIndex = this.boxes.length - 1;
      }
      else if (this.state == State.SELECT){
        this.selectedBoxIndex = -1;
        this.state = State.EMPTY;
        this.draw();
      }

  }

  //@HostListener('mousemove', ['$event'])
  onMouseMove(event: MouseEvent): void {
    const [mouseX, mouseY] = this.getMousePosition(event);
    //console.log(`MOUSE MOVE [${mouseX},${mouseY}]`);

    if (this.state == State.ADD) {
      this.adding.endX = mouseX;
      this.adding.endY = mouseY;
      let width = Math.abs(this.adding.endX - this.adding.startX);
      let height = Math.abs(this.adding.endY - this.adding.startY);
      let x = Math.min(this.adding.startX, this.adding.endX);
      let y = Math.min(this.adding.startY, this.adding.endY);

      this.boxes[this.selectedBoxIndex] = {
        x: x,
        y: y,
        width: width,
        height: height,
      };
      this.draw();
    } else if (this.state == State.RESIZE) {
      let box = this.boxes[this.selectedBoxIndex];

      let startX = box.x;
      let startY = box.y;
      let endX = box.x + box.width;
      let endY = box.y + box.height;

      if (this.resizing.handle == ResizeHandle.LEFT) {
        startX = Math.min(mouseX, this.resizing.startX);
        endX = Math.max(mouseX, this.resizing.startX);
      } else if (this.resizing.handle == ResizeHandle.RIGHT) {
        startX = Math.min(mouseX, this.resizing.startX);
        endX = Math.max(mouseX, this.resizing.startX);
      } else if (this.resizing.handle == ResizeHandle.TOP) {
        startY = Math.min(mouseY, this.resizing.startY);
        endY = Math.max(mouseY, this.resizing.startY);
      } else if (this.resizing.handle == ResizeHandle.BOTTOM) {
        startY = Math.min(mouseY, this.resizing.startY);
        endY = Math.max(mouseY, this.resizing.startY);
      } else {
        startX = Math.min(mouseX, this.resizing.startX);
        endX = Math.max(mouseX, this.resizing.startX);
        startY = Math.min(mouseY, this.resizing.startY);
        endY = Math.max(mouseY, this.resizing.startY);
      }

      let width = Math.abs(endX - startX);
      let height = Math.abs(endY - startY);
      let x = startX;
      let y = startY;

      this.boxes[this.selectedBoxIndex] = {
        x: x,
        y: y,
        width: width,
        height: height,
      };
      this.draw();
    } else if (this.state == State.MOVE) {
      let box = this.boxes[this.selectedBoxIndex];
      let width = box.width;
      let height = box.height;
      let x = mouseX - this.moving.offsetX;
      let y = mouseY - this.moving.offsetY;
      this.boxes[this.selectedBoxIndex] = {
        x: x,
        y: y,
        width: width,
        height: height,
      };
      this.draw();
    }
    this.setCursor(mouseX, mouseY);
  }

  setCursor(x: number, y: number) {
    let type: string = 'default';
    if (this.state == State.RESIZE) {
      type = this.resizing.cursor;
    } else if (this.state == State.MOVE) {
      type = 'move';
    } else if (this.state == State.EMPTY || this.state == State.SELECT) {
      for (let index = 0; index < this.boxes.length; index++) {
        let box = this.boxes[index];

        if (
          x < box.x + box.width - this.resizeHandleSize &&
          x > box.x + this.resizeHandleSize &&
          y < box.y + box.height - this.resizeHandleSize &&
          y > box.y + this.resizeHandleSize
        ) {
          type = 'move';
        }

        // Bottom Right
        else if (
          x >= box.x + box.width - this.resizeHandleSize &&
          x <= box.x + box.width + this.resizeHandleSize &&
          y >= box.y + box.height - this.resizeHandleSize &&
          y <= box.y + box.height + this.resizeHandleSize
        ) {
          type = 'nwse-resize';
        }

        // Top Right
        else if (
          x >= box.x + box.width - this.resizeHandleSize &&
          x <= box.x + box.width + this.resizeHandleSize &&
          y >= box.y - this.resizeHandleSize &&
          y <= box.y + this.resizeHandleSize
        ) {
          type = 'nesw-resize';
        }
        // Top LEFT
        else if (
          x >= box.x - this.resizeHandleSize &&
          x <= box.x + this.resizeHandleSize &&
          y >= box.y - this.resizeHandleSize &&
          y <= box.y + this.resizeHandleSize
        ) {
          type = 'nwse-resize';
        }
        // Bottom left
        else if (
          x >= box.x - this.resizeHandleSize &&
          x <= box.x + this.resizeHandleSize &&
          y >= box.y + box.height - this.resizeHandleSize &&
          y <= box.y + box.height + this.resizeHandleSize
        ) {
          type = 'nesw-resize';
        }
        // LEFT
        else if (
          x >= box.x - this.resizeHandleSize &&
          x <= box.x + this.resizeHandleSize &&
          y >= box.y - this.resizeHandleSize &&
          y <= box.y + box.height + this.resizeHandleSize
        ) {
          type = 'ew-resize';
        }
        // RIGHT
        else if (
          x >= box.x + box.width - this.resizeHandleSize &&
          x <= box.x + box.width + this.resizeHandleSize &&
          y >= box.y - this.resizeHandleSize &&
          y <= box.y + box.height + this.resizeHandleSize
        ) {
          type = 'ew-resize';
        }
        // TOP
        else if (
          x >= box.x - this.resizeHandleSize &&
          x <= box.x + box.width + this.resizeHandleSize &&
          y >= box.y - this.resizeHandleSize &&
          y <= box.y + this.resizeHandleSize
        ) {
          type = 'ns-resize';
        }
        // BOTTOM
        else if (
          x >= box.x - this.resizeHandleSize &&
          x <= box.x + box.width + this.resizeHandleSize &&
          y >= box.y + box.height - this.resizeHandleSize &&
          y <= box.y + +box.height + this.resizeHandleSize
        ) {
          type = 'ns-resize';
        }
      }
    }
    this.canvas.nativeElement.style.cursor = type;
  }


  onKeyUp(event: KeyboardEvent): void {
    if (event.key == 'Backspace' && this.selectedBoxIndex != -1){
      this.boxes.splice(this.selectedBoxIndex,1);
      this.draw();
    }
  }

  onMouseUp(event: MouseEvent): void {
    const [mouseX, mouseY] = this.getMousePosition(event);
    console.log(`MOUSE UP [${mouseX},${mouseY}]`);

    if (this.state == State.ADD) {
      this.adding.endX = mouseX;
      this.adding.endY = mouseY;
      let width = Math.abs(this.adding.endX - this.adding.startX);
      let height = Math.abs(this.adding.endY - this.adding.startY);
      let x = Math.min(this.adding.startX, this.adding.endX);
      let y = Math.min(this.adding.startY, this.adding.endY);
      if (width > 10 && height > 10){
      this.boxes[this.selectedBoxIndex] = {
        x: x,
        y: y,
        width: width,
        height: height,
      };}else{
        this.boxes.splice(this.selectedBoxIndex,1);
      }

      this.draw();
      this.state = State.SELECT;
    } else if (this.state == State.RESIZE) {
      this.state = State.SELECT;
    } else if (this.state == State.MOVE) {
      this.state = State.SELECT;
    }
  }

  onMouseLeave(event: MouseEvent): void {
    const rect = this.canvas.nativeElement.getBoundingClientRect();
    const mouseX = event.clientX - rect.left;
    const mouseY = event.clientY - rect.top;
    console.log(`MOUSE LEAVE [${mouseX},${mouseY}]`);
  }

  deleteSelectedBox(): void {
    if (this.selectedBoxIndex !== null) {
      this.boxes.splice(this.selectedBoxIndex, 1);
      this.selectedBoxIndex = -1;
      this.draw();
    }
  }

  labelSelectedBox(){
    if (this.selectedBoxIndex != -1){
      this.label = this.boxes[this.selectedBoxIndex];
    }
  }

  cropImageBox(boxNumber: number){
    let box = this.boxes[boxNumber];
    const croppedCanvas = document.createElement('canvas');
    const croppedCtx = croppedCanvas.getContext('2d')!;
    const canvas = this.canvas.nativeElement;
    const rect = canvas.getBoundingClientRect(); // Get canvas position & size

    // Scaling factor: Adjust for responsive canvas
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;
    const cropX = box.x / scaleX;
    const cropY = box.y / scaleY;
    const cropWidth = box.width / scaleX;
    const cropHeight = box.height / scaleY;
    croppedCanvas.width = cropWidth;
    croppedCanvas.height = cropHeight;
    croppedCtx.drawImage(this.image, cropX, cropY, cropWidth, cropHeight, 0, 0, cropWidth, cropHeight);
    let croppedImage = croppedCanvas.toDataURL('image/png');

    console.log(croppedImage);
    box.imageUrl = croppedImage;
  }
}
