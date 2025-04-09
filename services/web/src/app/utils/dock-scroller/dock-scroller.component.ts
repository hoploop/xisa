import { Component, ElementRef, QueryList, ViewChildren } from '@angular/core';
import { FAIconType } from '@constants/icons';

@Component({
  selector: 'app-dock-scroller',
  standalone: false,
  templateUrl: './dock-scroller.component.html',
  styleUrl: './dock-scroller.component.scss'
})
export class DockScrollerComponent {
  FAIconType = FAIconType;
  tracks = [
    {
      id: 'video-track-1',
      clips: [
        { label: 'Intro', start: 0, duration: 20 },
        { label: 'Scene 1', start: 21, duration: 30 },
        { label: 'Scene 2', start: 25, duration: 30 },
        { label: 'Scene 3', start: 90, duration: 2 },
        { label: 'Scene 1', start: 25, duration: 30 },
        { label: 'Scene 1', start: 25, duration: 30 },
      ],
    },
    {
      id: 'video-track-2',
      clips: [
        { label: 'Overlay', start: 10, duration: 15 },
      ],
    },
  ];

  onClipClick(clip: any) {
    console.log('Clip clicked:', clip);
    // maybe open a modal, load it in preview, etc.
  }
}
