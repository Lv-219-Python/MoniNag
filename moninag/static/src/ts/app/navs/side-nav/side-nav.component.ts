import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';

import { Server } from '../../servers/model';
import { Service } from '../../services/services';
import { Check } from '../../checks/check';
import { SideNavService } from './side-nav.service';


@Component({
    selector: 'side-nav',
    template: require('./side-nav.component.html'),
    providers: [SideNavService]
})


export class SideNavComponent implements OnInit {

    constructor(
        private sideNavService: SideNavService,
        private router: Router
    ) { }

    servers: Server[];
    selectedServer: Server;
    selectedService: Service;
    selectedCheck: Check;

    ngOnInit(): void {
        this.sideNavService.getTree()
            .subscribe(servers => {
                this.servers = servers['response']
            })    
    }

    gotoServer(server:Server): void {
        this.selectedServer = server;
        this.router.navigate(['server', this.selectedServer.id]);
        event.stopPropagation();
    }

    gotoService(service:Service): void {
        this.selectedService = service;
        this.router.navigate(['/services', this.selectedService.id]);
        event.stopPropagation();
    }

    gotoCheck(check:Check): void {
        this.selectedCheck = check;
        this.router.navigate(['checks', this.selectedCheck.id]);
        event.stopPropagation();
    }
}
