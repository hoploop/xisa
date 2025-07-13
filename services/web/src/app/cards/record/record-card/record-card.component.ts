import { Component, Input, OnInit } from '@angular/core';
import { Detector, Project, Record } from '@api/index';
import { DetectorSelectorModalComponent } from '@modals/detector/detector-selector-modal/detector-selector-modal.component';
import { RecordFormModalComponent } from '@modals/record/record-form-modal/record-form-modal.component';
import { RecordVideoModalComponent } from '@modals/record/record-video-modal/record-video-modal.component';
import { BaseComponent } from '@utils/base/base.component';

@Component({
  selector: 'app-record-card',
  standalone: false,
  templateUrl: './record-card.component.html',
  styleUrl: './record-card.component.scss',
})
export class RecordCardComponent extends BaseComponent implements OnInit {
  @Input() record!: Record;
  project?: Project;

  ngOnInit(): void {
    this.ctx.api.project.projectLoad(this.record.project).subscribe({
      next: (result) => {
        this.project = result;
      },
      error: (result) => {
        this.log.error(result.error.detail);
      },
    });
  }

  navigateVideoList() {}

  edit() {
    this.ctx
      .openModal(RecordFormModalComponent, { record: this.record })
      .subscribe({
        next: (result) => {},
        error: (result) => {},
      });
  }

  video() {
    this.ctx
      .openModal(
        RecordVideoModalComponent,
        { record: this.record },
        { size: 'lg', centered: true }
      )
      .subscribe({
        next: (result) => {},
        error: (result) => {},
      });
  }

  train() {
    if (!this.project) return;
    this.ctx
      .openModal<Detector | undefined>(DetectorSelectorModalComponent, {
        project: this.project,
      })
      .subscribe({
        next: (result) => {



          if (result) {
            this.router.navigate([
              'trainer/lesson',
              result._id,
              this.record._id,
            ]);
          }
        },
        error: (result) => {},
      });
  }

  automate() {
    this.router.navigate(['auto/page',this.record._id]);
  }

  play() {}
}
