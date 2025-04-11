import { Component, OnInit } from "@angular/core";
import { RouteComponent } from "@utils/route/route.component";
import { RecordStudioComponent } from "./record-studio.component";

@Component({
  selector: 'app-record-studio-route',
  standalone: false,
  template: ''
})
export class RecordStudioRoute extends RouteComponent implements OnInit {

  ngOnInit(): void {
    let recordId = this.getParam('record_id');
    if (!recordId) return;
    this.ctx.api.recorder.recorderLoad(recordId).subscribe(result=>{
      this.ctx.open(RecordStudioComponent, { record: result }).subscribe();
    })
  }


}
