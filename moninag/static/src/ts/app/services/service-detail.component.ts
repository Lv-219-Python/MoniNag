import { ActivatedRoute, Params, Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';

import { CheckListComponent } from '../checks/check-list.component';
import { Service } from './services';
import { ServicesService } from './services.service';

@Component({
    selector: 'services-detail',
    template: require('./service-detail.component.html'),
    providers: [ServicesService]
})

export class ServiceDetailComponent implements OnInit {

    constructor(
        private route: ActivatedRoute,
        private location: Location,
        private router: Router,
        private servicesService: ServicesService
    ) { }

    service: Service;
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

    save(): void {
        this.servicesService.update(this.service)
            .subscribe(() => this.goBack());
    }

    delete(): void {
        this.servicesService.remove(this.service.id)
            .subscribe(() => this.goBack());
    }
}