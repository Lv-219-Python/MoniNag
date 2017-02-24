import { Component, OnInit, OnChanges } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs/Observable';

import { Server, states } from './servers/model';
import { ServersService } from './servers/service';
import { ServersEditComponent } from './servers/edit-server.component'
import { ServerComponent } from './servers/server.component'

@Component({
    selector: 'servers-app',
    template: `
    <div class="table-responsive">
    <ul style="list-style-type:none; padding:0">
    <table class="table">
    <thead>
      <tr>
        <th></th>
        <th>Name</th>
        <th>Address</th>
        <th>State</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr *ngFor="let server of servers">
        <td>{{ server.name }}</td>
        <td>{{ server.address }}</td>
        <td>{{ server.state }}</td>
        <td>
          <button (click)="onSelect(server)" (click)="gotoEdit()" value={{server.id}}>Edit</button>
        </td>
      </tr>
    </tbody>
    </table>
      </ul>
      <button (click)="onSelect(server)" (click)="add()">Add</button>
    </div>
    `,
    providers: [ServersService]
})

export class ServersComponent implements OnInit {

  servers: Server[];
  selectedServer : Server;
  deletedServer: Server;
  server: Server;

  constructor(
    private serversService: ServersService,
    private router: Router){}

  ngOnInit(){
    this.serversService.getServers()
                        .subscribe(servers => {
                          this.servers = servers['response']
                        })}

  onSelect(server: Server): void{
        this.selectedServer = server;
    }

  gotoEdit(): void{
    this.router.navigate(['server', this.selectedServer.id]);
  }
  handleServerAdded(server: Server){
      this.servers.push(server)
    }
  add() {
      this.router.navigate(['server-add']);
 }
}
