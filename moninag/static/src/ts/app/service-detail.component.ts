import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Location } from '@angular/common';

import { Service } from './services';
import { ServicesService } from './services.service';

@Component({
    selector: 'services-detail',
    template: `
        <div *ngIf="service">
            <h3>Service Details</h3>
            <div>
                <label>name: </label>{{service.name}}
            </div>

            <div>
                <label>status: </label>{{service.status}}
            </div>

            <div>
                <label>id: </label>{{service.id}}
            </div>

            <div>
                <label>server id: </label>{{service.server_id}}
            </div>
        </div>
        <button (click)="goBack()">Back</button>
    `,
    providers: [ ServicesService ]
})
export class ServiceDetailComponent implements OnInit {

    constructor(
        private route: ActivatedRoute,
        private location: Location,
        private router: Router,
        private servicesService: ServicesService
        ) {}

    service: Service[];
    selectedService: Service;

    ngOnInit(): void {
        this.route.params
            .switchMap((params: Params) => this.servicesService.getService(+params['id']))
            .subscribe(service => this.service = service["response"]); 
}
    goBack(): void {
        this.location.back();
    }
    onSelect(service: Service): void {
        this.selectedService = service;
    }    
}

