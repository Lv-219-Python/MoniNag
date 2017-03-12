import { Component, OnInit, Input, ViewEncapsulation } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { DialogPreset, DialogPresetBuilder, Modal, VexModalModule } from 'angular2-modal/plugins/vex';

import { Location } from '@angular/common';
import 'rxjs/add/operator/switchMap';

import { overlayConfigFactory } from "angular2-modal";

import { Server, states } from './model';
import { ServersService } from './service';
import { ServerEditComponent } from './server-edit.component'
import { ServicesComponent } from '../services/services.component';


@Component({
    selector: 'serverdetail-app',
    template: require('./server-detail.component.html'),
    providers: [ServersService],
    encapsulation: ViewEncapsulation.None
})


export class ServerDetailComponent implements OnInit {

    constructor(
        private serversService: ServersService,
        private route: ActivatedRoute,
        private router: Router,
        private location: Location,
        public modal: Modal
    ) { }

    server: Server;
    selectedServer: Server;

    ngOnInit(): void {
        this.route.params
            .switchMap((params: Params) => this.serversService.getServer(+params['id']))
            .subscribe(server => this.server = server['response']);
    }

    gotoEdit(): void {
        this.router.navigate(['server/edit', this.server['id']]);
    }

    delete() {
        this.serversService.deleteServer(this.server['id'])
            .subscribe(() => this.goBack())
    }

    deactivate(): void {
        this.serversService.deactivate(this.server)
            .subscribe(() => this.goBack());
    }

    activate(): void {
        this.serversService.activate(this.server)
            .subscribe(() => this.goBack());
    }

    goBack(): void {
        this.location.back();
    }

    renderModal() {
        return new DialogPresetBuilder<DialogPreset>(this.modal)
            .content(ServerEditComponent)
            .isBlocking(false)
            .open();
    }
}
