import { Component, OnInit } from '@angular/core';
import { grpc } from '@improbable-eng/grpc-web';
import { createPromiseClient } from "@bufbuild/connect";
import { createConnectTransport } from "@bufbuild/connect-web";

@Component({
  selector: 'app-mockup',
  standalone: false,
  templateUrl: './mockup.component.html',
  styleUrl: './mockup.component.scss'
})
export class MockupComponent implements OnInit{

  ngOnInit(): void {

  }


}
