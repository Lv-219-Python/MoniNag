import { Component, OnInit, OnChanges, Input, ViewEncapsulation } from '@angular/core';
import { DialogPreset, DialogPresetBuilder, Modal, VexModalModule } from 'angular2-modal/plugins/vex';

import { Observable } from 'rxjs/Observable';
import { overlayConfigFactory } from "angular2-modal";
import { Router } from '@angular/router';

import { Server } from './model';
import { ServersService } from './service';
import { ServerAddComponent } from './server-add.component'

@Component({
    selector: 'servers-app',
    template: require('./servers.component.html'),
    providers: [ServersService],
    encapsulation: ViewEncapsulation.None
})

export class ServersComponent implements OnInit {

    servers: Server[];
    selectedServer: Server;
    deletedServer: Server;
    server: Server;

    constructor(
        private serversService: ServersService,
        private router: Router,
        public modal: Modal) {}

    ngOnInit() {
        this.serversService.getServers()
            .subscribe(servers => {
                this.servers = servers['response']
            })

    }

    onSelect(server: Server): void {
        this.selectedServer = server;
    }

    gotoDetail(): void {
        this.router.navigate(['server', this.selectedServer.id]);
    }
    handleServerAdded(server: Server) {
        this.servers.push(server)
    }
    renderModal() {
        return new DialogPresetBuilder<DialogPreset>(this.modal)
            .content(ServerAddComponent)
            .isBlocking(false)
            .open();
    }

}
