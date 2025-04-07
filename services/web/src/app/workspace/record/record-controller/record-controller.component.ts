import { Component, Input, OnInit } from '@angular/core';
import { Project } from '@api/index';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-controller',
  standalone: false,
  templateUrl: './record-controller.component.html',
  styleUrl: './record-controller.component.scss',
})
export class RecordControllerComponent extends BaseComponent implements OnInit {
  @Input() project!: Project;
  running?: boolean;

  ngOnInit(): void {
    this.load();
  }

  load() {
    this.ctx.api.recorder.recorderRunning().subscribe({
      next: (result) => {
        this.running = result;
      },
      error: (result) => {
        this.error.next(result.error.detail);
      },
    });
  }

  start() {
    if (!this.project._id) return;
    this.ctx.api.recorder
      .recorderStart(
        this.project._id,
        this.project.name,
        this.project.description
      )
      .subscribe({
        next: (result) => {
          this.running = true;
        },
        error: (result) => {
          this.error.next(result.error.detail);
        },
      });
  }

  stop() {
    if (!this.project._id) return;
    this.ctx.api.recorder.recorderStop().subscribe({
      next: (result) => {
        this.running = false;
        this.ctx.closeModal(result);
      },
      error: (result) => {
        this.error.next(result.error.detail);
      },
    });
  }

  cancel() {
    this.ctx.dismissModal();
  }
}
