import {
  AfterViewInit,
  Component,
  ElementRef,
  Input,
  OnInit,
  ViewChild,
} from '@angular/core';
import { Frame } from '../record-frame';
import {
  DetectorImageMode,
  KeyComboPressEventTypeEnum,
  KeyPressEventTypeEnum,
  KeyReleaseEventTypeEnum,
  MouseClickLeftEvent,
  MouseClickLeftEventTypeEnum,
  MousePressLeftEvent,
  MousePressLeftEventTypeEnum,
} from '@api/index';
import { environment } from '@environments/environment';
import { BaseComponent } from '@utils/base/base.component';

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
  SELECT = 4,
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
  selector: 'app-record-frame',
  standalone: false,
  templateUrl: './record-frame.component.html',
  styleUrl: './record-frame.component.scss',
})
export class RecordFrameComponent
  extends BaseComponent
  implements AfterViewInit
{
  @Input() frame!: Frame;
  @Input() detectorId?: string;
  @ViewChild('canvasElement', { static: false })
  canvas!: ElementRef<HTMLCanvasElement>;
  @ViewChild('bgCanvas', { static: false })
  private context!: CanvasRenderingContext2D;
  training: boolean = true;
  evaluating: boolean = true;
  testing: boolean = false;
  image = new Image();
  box?: Box;
  resizeHandleSize: number = 10;
  private state: State = State.EMPTY;
  eventX: number = 0;
  eventY: number = 0;
  tags: string[] = [];
  @Input() recordId?: string;

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

  save() {
    // Converting the current image to blob
    if (this.detectorId && this.recordId) {
      let modes: DetectorImageMode[] = [];
      if (this.training){
        modes.push(DetectorImageMode.Train);
      }
      if (this.evaluating){
        modes.push(DetectorImageMode.Val);
      }
      if (this.testing){
        modes.push(DetectorImageMode.Test);
      }
      this.ctx.api.detector
        .detectorFrameUpload(
          this.recordId,
          this.detectorId,
          this.frame.count,
          modes
        )
        .subscribe({
          next: (result) => {
            this.setLoading(undefined);
            for (let i = 0; i < result.length; i++){
              let el = result[i];
            if (el._id && this.box) {
              let payloadAdd = {
                image_id: el._id,
                xstart: this.box.x,
                xend: this.box.x+this.box.width,
                ystart: this.box.y,
                yend: this.box.y+this.box.height,
                classes: this.tags,
              }
              this.ctx.api.detector
                .detectorImageLabelAdd(payloadAdd)
                .subscribe({
                  next: (result2) => {
                    this.setLoading(undefined);
                  },
                  error: (result2) => {
                    this.setError(result2.error.detail);
                    this.setLoading(undefined);
                  },
                });
              }
            }
          },
          error: (result) => {
            this.setError(result.error.detail);
            this.setLoading(undefined);
          },
        });
    }
  }

  onTagsChange(value: string[]) {
    this.tags = value;
    if (this.tags.length > 0) {
      this.frame.resolved = true;
    } else {
      this.frame.resolved = false;
    }
  }

  ngAfterViewInit(): void {
    this.context = this.canvas.nativeElement.getContext('2d')!;
    this.load();
  }

  load() {
    if (!this.frame) return;

    this.image.onload = () => {
      setTimeout(() => {
        this.resizeCanvas();
      });
    };

    this.image.onerror = () => {
      console.error('Failed to load base64 image');
    };

    this.image.src =
      environment.apiUrl +
      '/record/frame/' +
      this.frame.record +
      '/' +
      this.frame.count;

    if (!this.frame.event) return;
    let event = this.frame.event;
    if (event.type == KeyComboPressEventTypeEnum.KeyComboPress) {
    }
    switch (event.type) {
      case KeyComboPressEventTypeEnum.KeyComboPress:
        break;
      case KeyPressEventTypeEnum.KeyPress:
        break;
      case KeyReleaseEventTypeEnum.KeyRelease:
        break;
      case MouseClickLeftEventTypeEnum.MouseClickLeft:
        let evt = event as MouseClickLeftEvent;
        if (evt.position) {
          this.eventX = evt.position[0];
          this.eventY = evt.position[1];
          this.box = {
            x: evt.position[0] - 20,
            y: evt.position[1] - 20,
            width: 40,
            height: 40,
          };
        }

        break;
      case MousePressLeftEventTypeEnum.MousePressLeft:
        let evt2 = event as MousePressLeftEvent;
        if (evt2.position) {
          this.eventX = evt2.position[0];
          this.eventY = evt2.position[1];
          this.box = {
            x: evt2.position[0] - 20,
            y: evt2.position[1] - 20,
            width: 40,
            height: 40,
          };
        }
        break;
      default:
        break;
    }
  }

  resizeCanvas(): void {
    this.canvas.nativeElement.width = this.image.width;
    this.canvas.nativeElement.height = this.image.height;
    this.draw();
  }

  draw() {
    this.image.crossOrigin = 'anonymous';
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

    this.drawBox();
  }

  onMouseLeave(event: MouseEvent) {
    const [mouseX, mouseY] = this.getMousePosition(event);
  }

  onMouseMove(event: MouseEvent) {
    const [mouseX, mouseY] = this.getMousePosition(event);
    if (!this.box) return;
    if (this.state == State.ADD) {
      this.adding.endX = mouseX;
      this.adding.endY = mouseY;
      let width = Math.abs(this.adding.endX - this.adding.startX);
      let height = Math.abs(this.adding.endY - this.adding.startY);
      let x = Math.min(this.adding.startX, this.adding.endX);
      let y = Math.min(this.adding.startY, this.adding.endY);

      this.box = {
        x: x,
        y: y,
        width: width,
        height: height,
      };
      this.draw();
    } else if (this.state == State.RESIZE) {
      let box = this.box;

      let startX = box.x;
      let startY = box.y;
      let endX = box.x + box.width;
      let endY = box.y + box.height;

      if (this.resizing.handle == ResizeHandle.LEFT) {
        startX = Math.min(mouseX, this.resizing.startX);
        endX = Math.max(endX, this.resizing.startX);
      } else if (this.resizing.handle == ResizeHandle.RIGHT) {
        startX = Math.min(mouseX, this.resizing.startX);
        endX = Math.max(mouseX, this.resizing.startX);
      } else if (this.resizing.handle == ResizeHandle.TOP) {
        startY = Math.min(mouseY, this.resizing.startY);
        endY = Math.max(endY, this.resizing.startY);
      } else if (this.resizing.handle == ResizeHandle.BOTTOM) {
        startY = Math.min(startY, this.resizing.startY);
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

      this.box = {
        x: x,
        y: y,
        width: width,
        height: height,
      };
      this.draw();
    } else if (this.state == State.MOVE) {
      let box = this.box;
      let width = box.width;
      let height = box.height;
      let x = mouseX - this.moving.offsetX;
      let y = mouseY - this.moving.offsetY;
      this.box = {
        x: x,
        y: y,
        width: width,
        height: height,
      };
      this.draw();
    }
    this.setCursor(mouseX, mouseY);
  }

  onMouseDown(event: MouseEvent) {
    const [mouseX, mouseY] = this.getMousePosition(event);
    // Now I can move either in SELECT mode or ADD mode or RESIZE mode
    if (!this.box) return;
    let overResizing = this.isOverResizing(mouseX, mouseY);
    let overBox = this.isOverBox(mouseX, mouseY);
    if (overResizing) {
      this.state = State.RESIZE;
    } else if (overBox) {
      this.state = State.MOVE;
      let box = this.box;
      this.moving.offsetX = mouseX - box.x;
      this.moving.offsetY = mouseY - box.y;
      this.draw();
    } else if (this.state == State.EMPTY) {
      this.state = State.ADD;
      this.adding.startX = mouseX;
      this.adding.startY = mouseY;
    } else if (this.state == State.SELECT) {
      this.state = State.EMPTY;
      this.draw();
    }
  }

  onMouseUp(event: MouseEvent) {
    const [mouseX, mouseY] = this.getMousePosition(event);
    if (this.state == State.ADD) {
      this.adding.endX = mouseX;
      this.adding.endY = mouseY;
      let width = Math.abs(this.adding.endX - this.adding.startX);
      let height = Math.abs(this.adding.endY - this.adding.startY);
      let x = Math.min(this.adding.startX, this.adding.endX);
      let y = Math.min(this.adding.startY, this.adding.endY);
      if (width > 10 && height > 10) {
        this.box = {
          x: x,
          y: y,
          width: width,
          height: height,
        };
      }

      this.draw();
      this.state = State.SELECT;
    } else if (this.state == State.RESIZE) {
      this.state = State.SELECT;
    } else if (this.state == State.MOVE) {
      this.state = State.SELECT;
    }
  }

  onKeyUp(event: KeyboardEvent) {}

  getMousePosition(event: MouseEvent): [number, number] {
    const canvas = this.canvas.nativeElement;
    const rect = canvas.getBoundingClientRect(); // Get canvas position & size

    // Scaling factor: Adjust for responsive canvas
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;

    // Adjusted X, Y relative to canvas scale
    const x = (event.clientX - rect.left) * scaleX;
    const y = (event.clientY - rect.top) * scaleY;
    return [x, y];
  }

  counterScaleX(value:number):number{
    const canvas = this.canvas.nativeElement;
    const rect = canvas.getBoundingClientRect(); // Get canvas position & size
    const scaleX = rect.width / canvas.width ;
    const scaleY =  rect.height / canvas.height;
    return value * scaleX
  }

  counterScaleY(value:number):number{
    const canvas = this.canvas.nativeElement;
    const rect = canvas.getBoundingClientRect(); // Get canvas position & size
    const scaleX = rect.width / canvas.width ;
    const scaleY =  rect.height / canvas.height;
    return value * scaleY
  }

  drawBox() {
    if (!this.box) return;
    let color = 'blue';
    if (!this.frame.resolved) {
      color = 'red';
    }
    let box = this.box;
    this.context.strokeStyle = color;
    this.context.fillStyle = 'rgba(255,255,255,0.2)';
    this.context.fillRect(box.x, box.y, box.width, box.height);
    this.context.lineWidth = 1;
    this.context.strokeRect(box.x, box.y, box.width, box.height);

    // Draw resize handles
    this.context.fillStyle = color;
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
      box.x + box.width - this.resizeHandleSize / 2,
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
      box.y + box.height / 2 - this.resizeHandleSize / 2,
      this.resizeHandleSize,
      this.resizeHandleSize
    );
    this.context.fillRect(
      box.x + box.width - this.resizeHandleSize / 2,
      box.y + box.height / 2 - this.resizeHandleSize / 2,
      this.resizeHandleSize,
      this.resizeHandleSize
    );
    this.context.fillRect(
      box.x + box.width / 2 - this.resizeHandleSize / 2,
      box.y - this.resizeHandleSize / 2,
      this.resizeHandleSize,
      this.resizeHandleSize
    );
    this.context.fillRect(
      box.x + box.width / 2 - this.resizeHandleSize / 2,
      box.y + box.height - this.resizeHandleSize / 2,
      this.resizeHandleSize,
      this.resizeHandleSize
    );
  }

  isOverResizing(x: number, y: number): boolean {
    if (!this.box) return false;
    let box = this.box;

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
      return true;
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
      return true;
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
      return true;
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
      return true;
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
      return true;
    }
    // RIGHT
    else if (
      x >= box.x + box.width - this.resizeHandleSize &&
      x <= box.x + box.width + this.resizeHandleSize &&
      y >= box.y - this.resizeHandleSize &&
      y <= box.y + box.height + this.resizeHandleSize
    ) {
      this.resizing.handle = ResizeHandle.RIGHT;
      this.resizing.startX = box.x;
      this.resizing.startY = box.y;
      this.resizing.cursor = 'ew-resize';
      return true;
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
      return true;
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
      return true;
    }
    return false;
  }

  isOverBox(x: number, y: number): boolean {
    if (!this.box) return false;

    let box = this.box;
    if (
      x < box.x + box.width - this.resizeHandleSize &&
      x > box.x + this.resizeHandleSize &&
      y < box.y + box.height - this.resizeHandleSize &&
      y > box.y + this.resizeHandleSize
    ) {
      return true;
    }

    return false;
  }

  setCursor(x: number, y: number) {
    let type: string = 'default';
    if (this.state == State.RESIZE) {
      type = this.resizing.cursor;
    } else if (this.state == State.MOVE) {
      type = 'move';
    } else if (this.state == State.EMPTY || this.state == State.SELECT) {
      if (!this.box) return;
      let box = this.box;

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
    this.canvas.nativeElement.style.cursor = type;
  }
}
