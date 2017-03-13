import { ActivatedRoute, Params, Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/switchMap';

import { Server, states } from './model';
import { ServersService } from './service';
import { ServicesComponent } from '../services/services.component';


@Component({
    selector: 'servers-delete',
    template: require('./server-delete.component.html'),
    providers: [
        ServersService,
    ],
})


export class ServerDeleteComponent {

    constructor(
        private serversService: ServersService,
        private route: ActivatedRoute,
        private router: Router,
        private location: Location
    ) { }
    servers: Server[];
    server: Server[];
    states = states;

    ngOnInit() {
        this.route.params
            .switchMap((params: Params) => this.serversService.getServer(+params['id']))
            .subscribe(server => this.server = server['response']);
        }

    gotoServers() {
        location.href = '/#/servers/';
        location.reload();
    }

    delete() {
        this.serversService.deleteServer(this.server['id'])
            .subscribe(() => this.gotoServers())
    }

    goBack() {
        location.reload();
    }
}
