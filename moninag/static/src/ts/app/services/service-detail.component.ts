import { ActivatedRoute, Params, Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';

import { Service } from './services';
import { ServicesService } from './services.service';
import { ServiceUpdateComponent } from './service-update.component'

@Component({
    selector: 'services-detail',
    template: require('./service-detail.component.html'),
    providers: [ServicesService]
})

export class ServiceDetailComponent implements OnInit {

    constructor(private route: ActivatedRoute,
                private location: Location,
                private servicesService: ServicesService) {
    }

    service: Service;
    selectedService: Service;

    ngOnInit(): void {
        this.route.params
            .switchMap((params: Params) => this.servicesService.getService(+params['id']))
            .subscribe(service => this.service = service["response"]);
    }

    onSelect(service: Service): void {
        this.selectedService = service;
    }

    delete(): void {
        this.servicesService.remove(this.service.id)
            .subscribe(() => this.goBack());
    }

    deactivate(): void {
        this.servicesService.deactivate(this.service)
            .subscribe(() => this.goBack());
    }

    activate(): void {
        this.servicesService.activate(this.service)
            .subscribe(() => this.goBack());
    }

    goBack(): void {
        this.location.back();
    }
}
