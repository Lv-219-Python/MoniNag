import { Component, OnInit, OnChanges } from '@angular/core';
import { Router } from '@angular/router';

import { ServersService } from './servers/service';
import { ServersEditComponent } from './servers/edit-server.component'
import { Server, states } from './servers/model';


@Component({
    selector: 'servers-app',
    template: require('./servers/servers.html'),
    providers: [ServersService]
})

export class ServersComponent implements OnInit {

  servers: Server[];
  selectedServer : Server;

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
}
