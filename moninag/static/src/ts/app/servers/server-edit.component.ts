import { ActivatedRoute, Params, Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/switchMap';

import { ip4Address } from '../validations/patterns';
import { Server } from './model';
import { ServersService } from './service';
import { ServicesComponent } from '../services/services.component';


@Component({
    selector: 'servers-edit',
    template: require('./server-edit.component.html'),
    providers: [
        ServersService,
    ],
})


export class ServerEditComponent {

    constructor(
        private serversService: ServersService,
        private route: ActivatedRoute,
        private router: Router,
        private location: Location
    ) { }

    server: Server;
    ip4Address = ip4Address;

    ngOnInit() {
        this.route.params
            .switchMap((params: Params) => this.serversService.getServer(+params['id']))
            .subscribe(server => this.server = server['response']);
    }

    save() {
        this.serversService.putServer(this.server)
            .subscribe(() => this.goBack())
    }
    delete() {
        this.serversService.deleteServer(this.server['id'])
            .subscribe(() => this.goBack())
    }

    goBack() {
        location.reload();
    }
}
