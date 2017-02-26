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
    styles: [`
        .box {
            height: 70px;
            width: 150px;
            background-color: rgba(80, 100, 170, 0.5);
            box-shadow: 0 0 10px rgba(0,0,0,0.5);
            display: table-cell;
            vertical-align: middle;
            text-align: center;
            position: relative;
            padding: 1em;
            margin: 2em 10px 4em;
            background: #fff;
        }
        ul {
            list-style-type: none;
        }
    `]
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
