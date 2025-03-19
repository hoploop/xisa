import {
  AfterViewInit,
  Component,
  ElementRef,
  EventEmitter,
  HostListener,
  Input,
  Output,
  ViewChild,
} from '@angular/core';
import { ContextService } from '@services/context.service';
import { sample } from './sample';
import { ImageAnnotatorSettings } from './image-annotator-settings';
import {
  ImageAnnotatorBox,
  ImageAnnotatorMouseOverType,
} from './image-annotator-box';


export enum State {
  EMPTY = 0,
  SELECTED = 1,
  ADDING = 2,
  RESIZING = 3,
  MOVING=4,
}

@Component({
  selector: 'app-image-annotator',
  standalone: false,
  templateUrl: './image-annotator.component.html',
  styleUrl: './image-annotator.component.scss',
})
export class ImageAnnotatorComponent implements AfterViewInit {
  @Input() dataUrl: string = sample;
  @Output() doubleClicked = new EventEmitter<ImageAnnotatorBox>();
  @ViewChild('canvasElement', { static: false })

  canvas!: ElementRef<HTMLCanvasElement>;
  @Input() settings: ImageAnnotatorSettings = {
    resizeHandleSize: 10,
    selectedBorderColor: 'blue',
    defaultBorderColor: 'red',
    selectedColor: 'rgba(255,255,255,0.4)',
    defaultColor: 'rgba(255,255,255,0.2)',
  };
  private context!: CanvasRenderingContext2D;
  private image = new Image();
  selectedBoxIndex: number = -1;
  @Input() boxes: ImageAnnotatorBox[] = [];
  @Output() boxesChange = new EventEmitter<ImageAnnotatorBox[]>();
  label?: ImageAnnotatorBox;
  state: State = State.EMPTY;
  mouse = {
    x: 0,
    y:0,
    cursor:'default'
  };
  adding = {
    startX: 0,
    startY: 0
  };
  moving = {
    startX: 0,
    startY: 0
  };
  resizing = {
    startX: 0,
    startY: 0,
    type: ImageAnnotatorMouseOverType.NOT_OVER
  };


  constructor(private ctx: ContextService) {}

  ngAfterViewInit(): void {
    setTimeout(() => {
      this.context = this.canvas.nativeElement.getContext('2d')!;
      this.loadBase64Image(this.dataUrl);
    });
  }

  loadBase64Image(base64String: string): void {
    this.image.onload = () => {
      setTimeout(() => {
        this.resizeCanvas();
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
    this.boxes.forEach(box=>{
      this.normalizeInitialBox(box);
    })
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

  drawImage(x:number,y:number,image: any) {
    this.context.drawImage(
      image,
      x,
      y,
      image.width,
      image.height
    );
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

    this.boxes.forEach((box, index) => {
      box.draw();
    });
    this.boxesChange.next(this.boxes);
  }

  addBox(event: MouseEvent): void {
    const rect = this.canvas.nativeElement.getBoundingClientRect();
    const mouseX = event.clientX - rect.left;
    const mouseY = event.clientY - rect.top;
    this.boxes.push(
      new ImageAnnotatorBox(
        this.context,
        this.canvas.nativeElement,
        this.image,
        this.settings,
        mouseX,
        mouseY,
        100,
        100
      )
    );
    this.boxesChange.next(this.boxes);
    this.draw();
  }

  get selectedBox(): ImageAnnotatorBox | undefined {
    if (this.selectedBoxIndex == -1) return undefined;
    return this.boxes[this.selectedBoxIndex];
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

  normalizeInitialBox(box: ImageAnnotatorBox){
    const canvas = this.canvas.nativeElement;
    const rect = canvas.getBoundingClientRect(); // Get canvas position & size

    // Scaling factor: Adjust for responsive canvas
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;
    box.x = box.x * scaleX;
    box.y = box.y * scaleY;
    box.w = box.w * scaleX;
    box.h = box.h * scaleY;
  }

  onMouseDoubleClick(event:MouseEvent){
    this.updateMousePosition(event);
    let overType: ImageAnnotatorMouseOverType =ImageAnnotatorMouseOverType.NOT_OVER;
    let boxOver: ImageAnnotatorBox | undefined = undefined;
    let boxOverIndex: number = -1;
    this.selectedBoxIndex = -1;
    for (let i = 0; i < this.boxes.length; i++) {
      let box = this.boxes[i];
      let boxOverType = box.isMouseOver(this.mouse.x, this.mouse.y);
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


    let overType: ImageAnnotatorMouseOverType =ImageAnnotatorMouseOverType.NOT_OVER;
    let boxOver: ImageAnnotatorBox | undefined = undefined;
    let boxOverIndex: number = -1;
    this.selectedBoxIndex = -1;
    for (let i = 0; i < this.boxes.length; i++) {
      let box = this.boxes[i];
      let boxOverType = box.isMouseOver(this.mouse.x, this.mouse.y);
      if (boxOverType != ImageAnnotatorMouseOverType.NOT_OVER) {
        boxOver = box;
        overType = boxOverType;
        boxOverIndex = i;
        boxOver.isSelected = true;
        this.selectedBoxIndex = i;
      }else{
        box.isSelected = false;
      }
    }
    if (overType == ImageAnnotatorMouseOverType.NOT_OVER) {
      this.state = State.ADDING;
      this.adding.startX = this.mouse.x;
      this.adding.startY = this.mouse.y;
      this.boxes.push(
        new ImageAnnotatorBox(
          this.context,
          this.canvas.nativeElement,
          this.image,
          this.settings,
          this.mouse.x,
          this.mouse.y,
          this.settings.resizeHandleSize,
          this.settings.resizeHandleSize
        )

      );
      this.selectedBoxIndex = this.boxes.length - 1;
      this.boxes[this.boxes.length-1].isSelected = true;
      this.boxesChange.next(this.boxes);
      this.draw();
    } else if (overType == ImageAnnotatorMouseOverType.INSIDE) {
      this.state = State.MOVING;
      if (boxOver){
        this.moving.startX = this.mouse.x - boxOver.x;
        this.moving.startY = this.mouse.y - boxOver.y;
        this.selectedBoxIndex = boxOverIndex;
        boxOver.isSelected = true;
      }


    } else {
      this.state = State.RESIZING;
      this.resizing.type = overType;
      this.resizing.startX = this.mouse.x;
      this.resizing.startY = this.mouse.y;
      this.selectedBoxIndex = boxOverIndex;
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
    }
    else if (this.state == State.SELECTED){

    }
    else if (this.state == State.EMPTY){

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
      if (box!=undefined){
        if (this.resizing.type == ImageAnnotatorMouseOverType.BOTTOM){
          if (this.mouse.y > box.y){
            box.h = this.mouse.y-box.y;
          }
        }
        else if (this.resizing.type == ImageAnnotatorMouseOverType.TOP){
          if (this.mouse.y < box.y + box.h){
            box.h = box.y+box.h - this.mouse.y;
            box.y = this.mouse.y;

          }
        }
        else if (this.resizing.type == ImageAnnotatorMouseOverType.LEFT){
          if (this.mouse.x < box.x + box.w){
            box.w = box.x+box.w - this.mouse.x;
            box.x = this.mouse.x;

          }
        }
        if (this.resizing.type == ImageAnnotatorMouseOverType.RIGHT){
          if (this.mouse.x > box.x){
            box.w = this.mouse.x-box.x;
          }
        }
        if (this.resizing.type == ImageAnnotatorMouseOverType.TOP_RIGHT){
          if (this.mouse.y < box.y + box.h){
            box.h = box.y+box.h - this.mouse.y;
            box.y = this.mouse.y;
          }
          if (this.mouse.x > box.x){
            box.w = this.mouse.x-box.x;
          }
        }
        if (this.resizing.type == ImageAnnotatorMouseOverType.TOP_LEFT){
          if (this.mouse.y < box.y + box.h){
            box.h = box.y+box.h - this.mouse.y;
            box.y = this.mouse.y;

          }
          if (this.mouse.x < box.x + box.w){
            box.w = box.x+box.w - this.mouse.x;
            box.x = this.mouse.x;

          }
        }
        if (this.resizing.type == ImageAnnotatorMouseOverType.BOTTOM_RIGHT){
          if (this.mouse.y > box.y){
            box.h = this.mouse.y-box.y;
          }
          if (this.mouse.x > box.x){
            box.w = this.mouse.x-box.x;
          }
        }
        if (this.resizing.type == ImageAnnotatorMouseOverType.BOTTOM_LEFT){
          if (this.mouse.y > box.y){
            box.h = this.mouse.y-box.y;
          }
          if (this.mouse.x < box.x + box.w){
            box.w = box.x+box.w - this.mouse.x;
            box.x = this.mouse.x;

          }
        }
        this.draw();
      }

    }
    this.updateCursor();
  }

  updateCursor() {

    let overType: ImageAnnotatorMouseOverType =ImageAnnotatorMouseOverType.NOT_OVER;
    let boxOver: ImageAnnotatorBox | undefined = undefined;
    let boxOverIndex: number = -1;
    for (let i = 0; i < this.boxes.length; i++) {
      let box = this.boxes[i];
      let boxOverType = box.isMouseOver(this.mouse.x, this.mouse.y);
      if (boxOverType != ImageAnnotatorMouseOverType.NOT_OVER) {
        boxOver = box;
        overType = boxOverType;
        boxOverIndex = i;
        break;
      }
    }


      if (overType == ImageAnnotatorMouseOverType.BOTTOM_RIGHT){
        this.mouse.cursor = 'nwse-resize';
      }
      else if (overType == ImageAnnotatorMouseOverType.BOTTOM_LEFT){

        this.mouse.cursor = 'nesw-resize';
      }
      else if (overType == ImageAnnotatorMouseOverType.TOP_LEFT){
        this.mouse.cursor = 'nwse-resize';
      }
      else if (overType == ImageAnnotatorMouseOverType.TOP_RIGHT){
        this.mouse.cursor = 'nesw-resize';

      }
      else if (overType == ImageAnnotatorMouseOverType.TOP){
        this.mouse.cursor = 'ns-resize';
      }
      else if (overType == ImageAnnotatorMouseOverType.BOTTOM){
        this.mouse.cursor = 'ns-resize';
      }
      else if (overType == ImageAnnotatorMouseOverType.LEFT){
        this.mouse.cursor = 'ew-resize';
      }
      else if (overType == ImageAnnotatorMouseOverType.RIGHT){
        this.mouse.cursor = 'ew-resize';
      }else if (overType == ImageAnnotatorMouseOverType.INSIDE){
        this.mouse.cursor = 'move';
      }else if (overType == ImageAnnotatorMouseOverType.NOT_OVER){
        this.mouse.cursor = 'default';
      }

    this.canvas.nativeElement.style.cursor = this.mouse.cursor;
  }

  onKeyUp(event: KeyboardEvent): void {
    if (event.key == 'Backspace' && this.selectedBoxIndex != -1) {
      this.boxes.splice(this.selectedBoxIndex, 1);
      this.boxesChange.next(this.boxes);
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
        this.boxes.splice(this.selectedBoxIndex, 1);
        this.boxesChange.next(this.boxes);
        this.state = State.SELECTED;
        this.draw();
      }
    } else if (this.state == State.RESIZING) {
      this.state = State.SELECTED;
      this.draw();
    } else if (this.state == State.MOVING) {
      this.state = State.SELECTED;
      this.moving.startX = 0;
      this.moving.startY = 0;
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
      this.boxes.splice(this.selectedBoxIndex, 1);
      this.boxesChange.next(this.boxes);
      this.selectedBoxIndex = -1;
      this.draw();
    }
  }

  labelSelectedBox() {
    if (this.selectedBoxIndex != -1) {
      this.label = this.boxes[this.selectedBoxIndex];
    }
  }
}
