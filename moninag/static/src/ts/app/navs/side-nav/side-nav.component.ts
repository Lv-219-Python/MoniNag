import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';

import { Server } from '../../servers/model';
import { Service } from '../../services/services';
import { Check } from '../../checks/check';
import { SideNavService } from './side-nav.service';

@Component({
    selector: 'ngb-accordion',
    template: `<ng-content></ng-content>`
})

export class NgbAccordion {
    private groups: Array<NgbAccordionGroup> = [];
}

@Component({
    selector: 'ngb-accordion-group', 
    inputs: ['heading', 'isOpen', 'isDisabled'],
    template: `
        <div>
            <div class="isDisabled" (click)="toggleOpen($event)">{{heading}}</div>
            <div [hidden]="!isOpen">
                <div>
                    <ng-content></ng-content>
                </div>
            </div>
        </div>
  `
})

export class NgbAccordionGroup {

    private isDisabled: boolean;
    private isOpened: boolean = false;

    constructor(private accordion: NgbAccordion) {}

    toggleOpen(event:any) {
        event.preventDefault();
        if (!this.isDisabled) {
        this.isOpen = !this.isOpen;
        }
    }

    public get isOpen(): boolean { return this.isOpened; }

    public set isOpen(value: boolean) {
        this.isOpened = value;
    }
}

@Component({
    selector: 'side-nav',
    template: require('./side-nav.component.html'),
    providers: [SideNavService]
})

export class SideNavComponent implements OnInit {
    isOpen:boolean = false;

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

    onSelectServer(server:Server): void {
        this.selectedServer = server;
    }

    onSelectService(service:Service): void {
        this.selectedService = service;
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
