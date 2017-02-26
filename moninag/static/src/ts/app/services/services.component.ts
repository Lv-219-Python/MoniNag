import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs/Observable';

import { Server } from '../servers/model';
import { Service } from './services';
import { ServiceAddComponent } from './service-add.component';
import { ServicesService } from './services.service';

@Component({
    selector: 'services-app',
    template: require('./services.component.html'),
    providers: [ ServicesService ],
    styles: [ require('./services.component.css') ]
})

export class ServicesComponent {

    services: Service[];
    selectedService: Service;

    constructor (
        private servicesService: ServicesService,
        private router: Router
    ) {}

    @Input() server: Server[];

    onSelect(service: Service): void {
        this.selectedService = service;
    }

    gotoDetail(): void {
        this.router.navigate(['/services', this.selectedService.id]);
    }

    add() {
        this.router.navigate(['service-add']);
    }
}
