import { Component, Output, EventEmitter } from '@angular/core';
import { Validators } from '@angular/forms';
import { Location } from '@angular/common';

import { ServersService } from './service';
import { Server } from './model';


@Component({
    selector: 'server-add',
    template: require('./server-add.component.html'),
    providers: [ServersService]
})


export class ServerAddComponent {

    servers: Server[];

    model = new Server();

    @Output() serverAdded = new EventEmitter();

    constructor(
        private serversService: ServersService,
        private location: Location) {
    }

    submitForm() {
        this.serversService.addServer(this.model)
            .subscribe(model => model = model);
    }

    goBack(): void {
        location.reload();
    }
}
