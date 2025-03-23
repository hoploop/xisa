import { ImageAnnotatorSettings } from './image-annotator-settings';

export class ImageAnnotatorHighlight {
  public isSelected: boolean = false;
  constructor(
    public x: number = 0,
    public y: number = 0,
    public w: number = 0,
    public h: number = 0
  ) {}

  isMouseOver(x: number, y: number): boolean {
    if (x > this.x && x < this.x+this.w && y > this.y && y < this.y+this.h){
      return true;
    }
    return false;
  }

  public draw(ctx: CanvasRenderingContext2D, settings: ImageAnnotatorSettings){
    if (ctx==undefined) return;
    if (!settings.showHighlights) return;
     // Settings colors
     if (this.isSelected) {
      ctx.strokeStyle = settings.selectedHighlightBorderColor;
      ctx.fillStyle = settings.selectedHighlightColor;
    } else {
      ctx.strokeStyle = settings.defaultHighlightBorderColor;
      ctx.fillStyle = settings.defaultHighlightColor;
    }

    let cw = ctx.canvas.width;
    let ch = ctx.canvas.height;
    let x = this.x * cw;
    let y = this.y * ch;
    let w = this.w * cw;
    let h = this.h * ch;

    // Drawing the main rectangle
    ctx.fillRect(x,y,w,h);
    ctx.lineWidth = 1;
    ctx.strokeRect(x,y,w,h);
  }
}
