import { DetectorClass } from '@api/index';
import { ImageAnnotatorSettings } from './image-annotator-settings';

export enum ImageAnnotatorMouseOverType {
  TOP_LEFT = 0,
  TOP = 1,
  TOP_RIGHT = 2,
  RIGHT = 3,
  BOTTOM_RIGHT = 4,
  BOTTOM = 5,
  BOTTOM_LEFT = 6,
  LEFT = 7,
  INSIDE = 8,
  NOT_OVER = 9
}

export class ImageAnnotatorBox {
  isResizing: boolean = false;
  isMoving: boolean = false;
  dataUrl?: string;
  classes: DetectorClass[] = [];


  constructor(
    public x: number = 0,
    public y: number = 0,
    public w: number = 0,
    public h: number = 0,
    public isSelected: boolean = false
  ) {

  }

  classesToStringList(): string[]{
    let ret: string[] = [];
    this.classes.forEach(clazz=>{
      ret.push(clazz.name);
    })
    return ret;
  }


  isMouseOver(settings:ImageAnnotatorSettings,x: number, y: number): ImageAnnotatorMouseOverType {
    // Bottom Right
    if (
      x >= this.x + this.w - settings.resizeHandleSize &&
      x <= this.x + this.w + settings.resizeHandleSize &&
      y >= this.y + this.h - settings.resizeHandleSize &&
      y <= this.y + this.h + settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.BOTTOM_RIGHT;
    }

    // Top Right
    else if (
      x >= this.x + this.w - settings.resizeHandleSize &&
      x <= this.x + this.w + settings.resizeHandleSize &&
      y >= this.y - settings.resizeHandleSize &&
      y <= this.y + settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.TOP_RIGHT;
    }

    // Top LEFT
    else if (
      x >= this.x - settings.resizeHandleSize &&
      x <= this.x + settings.resizeHandleSize &&
      y >= this.y - settings.resizeHandleSize &&
      y <= this.y + settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.TOP_LEFT;
    }

    // Bottom LEFT
    else if (
      x >= this.x - settings.resizeHandleSize &&
      x <= this.x + settings.resizeHandleSize &&
      y >= this.y + this.h - settings.resizeHandleSize &&
      y <= this.y + this.h + settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.BOTTOM_LEFT;
    }

    // LEFT
    else if (
      x >= this.x - settings.resizeHandleSize &&
      x <= this.x + settings.resizeHandleSize &&
      y >= this.y + settings.resizeHandleSize &&
      y <= this.y + this.h - settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.LEFT;
    }
    // RIGHT
    else if (
      x >= this.x + this.w - settings.resizeHandleSize &&
      x <= this.x + this.w + settings.resizeHandleSize &&
      y >= this.y + settings.resizeHandleSize &&
      y <= this.y + this.h - settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.RIGHT;
    }

    // TOP
    else if (
      x >= this.x + settings.resizeHandleSize &&
      x <= this.x + this.w - settings.resizeHandleSize &&
      y >= this.y - settings.resizeHandleSize &&
      y <= this.y + settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.TOP;
    }
    // BOTTOM
    else if (
      x >= this.x + settings.resizeHandleSize &&
      x <= this.x + this.w - settings.resizeHandleSize &&
      y >= this.y + this.h - settings.resizeHandleSize &&
      y <= this.y + this.h + settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.BOTTOM;
    } else if (
      x > this.x + settings.resizeHandleSize &&
      x < this.x + this.w - settings.resizeHandleSize &&
      y > this.y + settings.resizeHandleSize &&
      y < this.y + this.h - settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.INSIDE;
    } else {
      return ImageAnnotatorMouseOverType.NOT_OVER;
    }
  }

  draw(ctx: CanvasRenderingContext2D,settings:ImageAnnotatorSettings,image:HTMLImageElement){
    if (ctx==undefined) return;
    this.updateDataUrl(ctx,image);

    // Settings colors
    if (this.isSelected) {
      ctx.strokeStyle = settings.selectedBorderColor;
      ctx.fillStyle = settings.selectedColor;
    } else {
      ctx.strokeStyle = settings.defaultBorderColor;
      ctx.fillStyle = settings.defaultColor;
    }

    // Drawing the main rectangle
    ctx.fillRect(this.x, this.y, this.w, this.h);
    ctx.lineWidth = 1;
    ctx.strokeRect(this.x, this.y, this.w, this.h);

    //if (!this.isSelected) return;

    // Draw resize handles
    if (this.isSelected) {
      ctx.fillStyle = settings.selectedBorderColor;
    } else {
      ctx.fillStyle = settings.defaultBorderColor;
    }


    // Bottom right handle
    ctx.fillRect(
      this.x + this.w - settings.resizeHandleSize / 2,
      this.y + this.h - settings.resizeHandleSize / 2,
      settings.resizeHandleSize,
      settings.resizeHandleSize
    );

    // Top left handle
    ctx.fillRect(
      this.x - settings.resizeHandleSize / 2,
      this.y - settings.resizeHandleSize / 2,
      settings.resizeHandleSize,
      settings.resizeHandleSize
    );

    // Top right handle
    ctx.fillRect(
      this.x + this.w - settings.resizeHandleSize / 2,
      this.y - settings.resizeHandleSize / 2,
      settings.resizeHandleSize,
      settings.resizeHandleSize
    );

    // Bottom Left handle
    ctx.fillRect(
      this.x - settings.resizeHandleSize / 2,
      this.y + this.h - settings.resizeHandleSize / 2,
      settings.resizeHandleSize,
      settings.resizeHandleSize
    );

    // Left handle
    ctx.fillRect(
      this.x - settings.resizeHandleSize / 2,
      this.y + this.h / 2 - settings.resizeHandleSize / 2,
      settings.resizeHandleSize,
      settings.resizeHandleSize
    );

    // Right handle
    ctx.fillRect(
      this.x + this.w - settings.resizeHandleSize / 2,
      this.y + this.h / 2 - settings.resizeHandleSize / 2,
      settings.resizeHandleSize,
      settings.resizeHandleSize
    );

    // Top handle
    ctx.fillRect(
      this.x + this.w / 2 - settings.resizeHandleSize / 2,
      this.y - settings.resizeHandleSize / 2,
      settings.resizeHandleSize,
      settings.resizeHandleSize
    );

    // Bottom handle
    ctx.fillRect(
      this.x + this.w / 2 - settings.resizeHandleSize / 2,
      this.y + this.h - settings.resizeHandleSize / 2,
      settings.resizeHandleSize,
      settings.resizeHandleSize
    );

    //Classes
    if (this.classes.length > 0){
      ctx.font = "18pt Arial";
      ctx.fillText(this.classes.length.toString(), this.x+6, this.y+20+3);
    }
  }

  drawImage(ctx: CanvasRenderingContext2D,x:number,y:number,image: HTMLImageElement) {
    ctx.drawImage(
      image,
      x,
      y,
      image.width,
      image.height
    );
  }

  updateDataUrl(ctx: CanvasRenderingContext2D,image:HTMLImageElement) {
    const canvas = ctx.canvas;
    const croppedCanvas = document.createElement('canvas');
    const croppedCtx = croppedCanvas.getContext('2d')!;
    const rect = canvas.getBoundingClientRect(); // Get canvas position & size

    // Scaling factor: Adjust for responsive canvas
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;
    const cropX = this.x / scaleX;
    const cropY = this.y / scaleY;
    const cropWidth = this.w / scaleX;
    const cropHeight = this.h / scaleY;
    croppedCanvas.width = cropWidth;
    croppedCanvas.height = cropHeight;
    croppedCtx.drawImage(
      image,
      cropX,
      cropY,
      cropWidth,
      cropHeight,
      0,
      0,
      cropWidth,
      cropHeight
    );
    let croppedImage = croppedCanvas.toDataURL('image/png');
    this.dataUrl = croppedImage;
  }
}
