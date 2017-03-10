import { Component, OnInit, OnChanges, Input, ViewEncapsulation, ViewChild, TemplateRef } from '@angular/core';
import {
  VEXBuiltInThemes,
  Modal,
  DialogPreset,
  DialogFormModal,
  DialogPresetBuilder,
  VEXModalContext,
  VexModalModule,
  providers
} from 'angular2-modal/plugins/vex';
import { Observable } from 'rxjs/Observable';
import { overlayConfigFactory } from "angular2-modal";
import { Router } from '@angular/router';

import { Server, states } from './model';
import { ServersService } from './service';
import { ServerAddComponent } from './server-add.component'

@Component({
    selector: 'servers-app',
    template: require('./servers.component.html'),
    styles: [
                require('../../../less/common/vex/vex.less').toString(),
                require('../../../less/common/vex/vex-theme-default.css').toString(),
            ],
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
    add() {
        //this.router.navigate(['server-add']);
        let modal = this.modal.alert()
        modal.open();
    }
}
