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


  constructor(
    private ctx: CanvasRenderingContext2D,
    private canvas: HTMLCanvasElement,
    private image: HTMLImageElement,
    private settings: ImageAnnotatorSettings,
    public x: number = 0,
    public y: number = 0,
    public w: number = 0,
    public h: number = 0,
    public isSelected: boolean = false
  ) {

  }



  isMouseOver(x: number, y: number): ImageAnnotatorMouseOverType {
    // Bottom Right
    if (
      x >= this.x + this.w - this.settings.resizeHandleSize &&
      x <= this.x + this.w + this.settings.resizeHandleSize &&
      y >= this.y + this.h - this.settings.resizeHandleSize &&
      y <= this.y + this.h + this.settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.BOTTOM_RIGHT;
    }

    // Top Right
    else if (
      x >= this.x + this.w - this.settings.resizeHandleSize &&
      x <= this.x + this.w + this.settings.resizeHandleSize &&
      y >= this.y - this.settings.resizeHandleSize &&
      y <= this.y + this.settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.TOP_RIGHT;
    }

    // Top LEFT
    else if (
      x >= this.x - this.settings.resizeHandleSize &&
      x <= this.x + this.settings.resizeHandleSize &&
      y >= this.y - this.settings.resizeHandleSize &&
      y <= this.y + this.settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.TOP_LEFT;
    }

    // Bottom LEFT
    else if (
      x >= this.x - this.settings.resizeHandleSize &&
      x <= this.x + this.settings.resizeHandleSize &&
      y >= this.y + this.h - this.settings.resizeHandleSize &&
      y <= this.y + this.h + this.settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.BOTTOM_LEFT;
    }

    // LEFT
    else if (
      x >= this.x - this.settings.resizeHandleSize &&
      x <= this.x + this.settings.resizeHandleSize &&
      y >= this.y + this.settings.resizeHandleSize &&
      y <= this.y + this.h - this.settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.LEFT;
    }
    // RIGHT
    else if (
      x >= this.x + this.w - this.settings.resizeHandleSize &&
      x <= this.x + this.w + this.settings.resizeHandleSize &&
      y >= this.y + this.settings.resizeHandleSize &&
      y <= this.y + this.h - this.settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.RIGHT;
    }

    // TOP
    else if (
      x >= this.x + this.settings.resizeHandleSize &&
      x <= this.x + this.w - this.settings.resizeHandleSize &&
      y >= this.y - this.settings.resizeHandleSize &&
      y <= this.y + this.settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.TOP;
    }
    // BOTTOM
    else if (
      x >= this.x + this.settings.resizeHandleSize &&
      x <= this.x + this.w - this.settings.resizeHandleSize &&
      y >= this.y + this.h - this.settings.resizeHandleSize &&
      y <= this.y + this.h + this.settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.BOTTOM;
    } else if (
      x > this.x + this.settings.resizeHandleSize &&
      x < this.x + this.w - this.settings.resizeHandleSize &&
      y > this.y + this.settings.resizeHandleSize &&
      y < this.y + this.h - this.settings.resizeHandleSize
    ) {
      return ImageAnnotatorMouseOverType.INSIDE;
    } else {
      return ImageAnnotatorMouseOverType.NOT_OVER;
    }
  }

  draw() {
    this.updateDataUrl();

    // Settings colors
    if (this.isSelected) {
      this.ctx.strokeStyle = this.settings.selectedBorderColor;
      this.ctx.fillStyle = this.settings.selectedColor;
    } else {
      this.ctx.strokeStyle = this.settings.defaultBorderColor;
      this.ctx.fillStyle = this.settings.defaultColor;
    }

    // Drawing the main rectangle
    this.ctx.fillRect(this.x, this.y, this.w, this.h);
    this.ctx.lineWidth = 1;
    this.ctx.strokeRect(this.x, this.y, this.w, this.h);

    //if (!this.isSelected) return;

    // Draw resize handles
    if (this.isSelected) {
      this.ctx.fillStyle = this.settings.selectedBorderColor;
    } else {
      this.ctx.fillStyle = this.settings.defaultBorderColor;
    }


    // Bottom right handle
    this.ctx.fillRect(
      this.x + this.w - this.settings.resizeHandleSize / 2,
      this.y + this.h - this.settings.resizeHandleSize / 2,
      this.settings.resizeHandleSize,
      this.settings.resizeHandleSize
    );

    // Top left handle
    this.ctx.fillRect(
      this.x - this.settings.resizeHandleSize / 2,
      this.y - this.settings.resizeHandleSize / 2,
      this.settings.resizeHandleSize,
      this.settings.resizeHandleSize
    );

    // Top right handle
    this.ctx.fillRect(
      this.x + this.w - this.settings.resizeHandleSize / 2,
      this.y - this.settings.resizeHandleSize / 2,
      this.settings.resizeHandleSize,
      this.settings.resizeHandleSize
    );

    // Bottom Left handle
    this.ctx.fillRect(
      this.x - this.settings.resizeHandleSize / 2,
      this.y + this.h - this.settings.resizeHandleSize / 2,
      this.settings.resizeHandleSize,
      this.settings.resizeHandleSize
    );

    // Left handle
    this.ctx.fillRect(
      this.x - this.settings.resizeHandleSize / 2,
      this.y + this.h / 2 - this.settings.resizeHandleSize / 2,
      this.settings.resizeHandleSize,
      this.settings.resizeHandleSize
    );

    // Right handle
    this.ctx.fillRect(
      this.x + this.w - this.settings.resizeHandleSize / 2,
      this.y + this.h / 2 - this.settings.resizeHandleSize / 2,
      this.settings.resizeHandleSize,
      this.settings.resizeHandleSize
    );

    // Top handle
    this.ctx.fillRect(
      this.x + this.w / 2 - this.settings.resizeHandleSize / 2,
      this.y - this.settings.resizeHandleSize / 2,
      this.settings.resizeHandleSize,
      this.settings.resizeHandleSize
    );

    // Bottom handle
    this.ctx.fillRect(
      this.x + this.w / 2 - this.settings.resizeHandleSize / 2,
      this.y + this.h - this.settings.resizeHandleSize / 2,
      this.settings.resizeHandleSize,
      this.settings.resizeHandleSize
    );
  }

  drawImage(x:number,y:number,image: HTMLImageElement) {
    this.ctx.drawImage(
      image,
      x,
      y,
      image.width,
      image.height
    );
  }

  updateDataUrl() {
    const croppedCanvas = document.createElement('canvas');
    const croppedCtx = croppedCanvas.getContext('2d')!;
    const rect = this.canvas.getBoundingClientRect(); // Get canvas position & size

    // Scaling factor: Adjust for responsive canvas
    const scaleX = this.canvas.width / rect.width;
    const scaleY = this.canvas.height / rect.height;
    const cropX = this.x / scaleX;
    const cropY = this.y / scaleY;
    const cropWidth = this.w / scaleX;
    const cropHeight = this.h / scaleY;
    croppedCanvas.width = cropWidth;
    croppedCanvas.height = cropHeight;
    croppedCtx.drawImage(
      this.image,
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
