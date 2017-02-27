import { ActivatedRoute, Params, Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/switchMap';


import { Server, states } from './model';
import { ServersService } from './service';
import { ServicesComponent } from '../services/services.component';


@Component({
    selector: 'servers-edit',
    template: require('./edit-server.component.html'),
    providers: [
        ServersService,
    ],
})


export class ServersEditComponent {

    constructor(
        private serversService: ServersService,
        private route: ActivatedRoute,
        private router: Router,
        private location: Location
    ) { }

    server: Server[];
    states = states;

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
        this.location.back();
    }
}
