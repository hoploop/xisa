import { ImageAnnotatorSettings } from './image-annotator-settings';
import { v4 as uuid } from 'uuid';



export class ImageAnnotatorHighlight {
  dataUrl?: string;
  selectedBorderColor: string = 'blue';
  defaultBorderColor: string = 'red';
  defaultBorderSize: number = 1;
  selectedColor: string = 'rgba(255,255,255,0.4)';
  defaultColor: string = 'rgba(255,255,255,0.2)';
  selectedBorderSize: number = 1;
  id = uuid();

  constructor(
    public x: number = 0,
    public y: number = 0,
    public w: number = 0,
    public h: number = 0,
    public percentage: boolean = false,
    public isSelected: boolean = false
  ) {}



  draw(
    ctx: CanvasRenderingContext2D,
    settings: ImageAnnotatorSettings,
    image: HTMLImageElement
  ) {
    if (ctx == undefined) return;
    this.updateDataUrl(ctx, image);

    // Settings colors
    if (this.isSelected) {
      ctx.strokeStyle = this.selectedBorderColor;
      ctx.fillStyle = this.selectedColor;
    } else {
      ctx.strokeStyle = this.defaultBorderColor;
      ctx.fillStyle = this.defaultColor;
    }

    // Drawing the main rectangle
    ctx.fillRect(this.x, this.y, this.w, this.h);
    if (this.isSelected){
      ctx.lineWidth = this.selectedBorderSize;
    }else{
      ctx.lineWidth = this.defaultBorderSize;
    }

    ctx.strokeRect(this.x, this.y, this.w, this.h);


    //ctx.fillText(labels, this.x + 6, this.y + 20 + 3);

  }

  drawImage(
    ctx: CanvasRenderingContext2D,
    x: number,
    y: number,
    image: HTMLImageElement
  ) {
    ctx.drawImage(image, x, y, image.width, image.height);
  }

  updateDataUrl(ctx: CanvasRenderingContext2D, image: HTMLImageElement) {
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
