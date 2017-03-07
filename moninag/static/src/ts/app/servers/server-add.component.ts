import { Component, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Location } from '@angular/common';

import { ServersService } from './service';
import { Server, states } from './model';


@Component({
    selector: 'server-add',
    template: require('./server-add.component.html'),
    providers: [ServersService]
})


export class ServerAddComponent {

    servers: Server[];
    serverForm: FormGroup;
    states = states;

    @Output() serverAdded = new EventEmitter();

    constructor(private serversService: ServersService, fb: FormBuilder, private location: Location) {
        this.serverForm = fb.group({
            'name': '',
            'address': '',
            'state': ''
        })
    }

    submitForm(server: any) {

        this.serversService.addServer(server)
            .subscribe(servers => {
                this.servers = servers['response'];
            })
    }

    goBack(): void {
        this.location.back();
    }
}
