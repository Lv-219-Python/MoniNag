import { ActivatedRoute, Params, Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/switchMap';

import { Service } from './services';
import { ServicesService } from './services.service';

@Component({
    selector: 'service-delete',
    template: require('./service-delete.component.html'),
    providers: [
        ServicesService,
    ],
})


export class ServiceDeleteComponent {

    constructor(
        private servicesService: ServicesService,
        private route: ActivatedRoute,
        private router: Router,
        private location: Location
    ) { }
    service: Service;

    ngOnInit(): void {
        this.route.params
            .switchMap((params: Params) => this.servicesService.getService(+params['id']))
            .subscribe(service => this.service = service["response"]);
    }


    gotoServers() {
        location = 'http://127.0.0.1:8000';

    }
    delete(): void {
        this.servicesService.remove(this.service.id)
            .subscribe(() => this.gotoServers());
    }

    goBack() {
        location.reload();
    }
}
