import { Component, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Location } from '@angular/common';

import { ServersService } from './service';
import { Server, states } from './model';


@Component({
  selector: 'server-add',
  template : `
  <div>
    <form [formGroup]="serverForm" (ngSubmit)="submitForm(serverForm.value)" >
      <div class="form-group">
        <input class="form-control" type="text" placeholder="Server Name" [formControl]="serverForm.controls['name']">
      </div>
      <div class="form-group">
        <input class="form-control" type="text" placeholder="Server Address" [formControl]="serverForm.controls['address']">
      </div>
      <div class="form-array">
            <label>State:
              <select class="form-control" formControlName="state">
                <option *ngFor="let state of states" [value]="state">{{state}}</option>
              </select>
            </label>
          </div>
      <div class="form-group">
          <button type="submit" (click)="goBack()" class="btn btn-primary">Submit</button>
     </div>
    </form>
  </div>
  `,
providers: [ServersService]

})
export class ServerComponent {

  servers : Server[];
  serverForm : FormGroup;
  states = states;
  @Output() serverAdded = new EventEmitter();

  constructor(private serversService: ServersService, fb: FormBuilder, private location: Location){
    this.serverForm = fb.group({
      'name' : '',
      'address': '',
      'state': ''

    })
}
  submitForm(server: any){

    this.serversService.addServer(server)
                        .subscribe(servers => {
                        this.servers = servers['response'];
                        })
    }
    goBack(): void {
        this.location.back();
    }
   }
