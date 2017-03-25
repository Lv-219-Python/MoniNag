import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';

import { Server } from '../../servers/model';
import { Service } from '../../services/services';
import { Check } from '../../checks/check';
import { SideNavService } from './side-nav.service';


@Component({
    selector: 'side-nav',
    template: require('./side-nav.component.html'),
    styles: [ require('./side-nav.less').toString() ],
    providers: [SideNavService]
})

export class SideNavComponent implements OnInit {
    constructor(
        private sideNavService: SideNavService,
        private router: Router
    ) { }

    servers: Server[];
    selectedComponent: any = {
        id: null
    };

    ngOnInit(): void {
        this.sideNavService.getTree()
            .subscribe(servers => {
                this.servers = servers['response']
            })
    }

    toggleExpand(component: any): void {
        component.expanded = !component.expanded;
    }

    navigateToComponent(component: any, route: string): void {
        this.selectedComponent = component;
        component.expanded = !component.expanded;
        this.router.navigate([route, this.selectedComponent.id]);
        event.stopPropagation();
    }
}
