import { ActivatedRoute, Params, Router } from '@angular/router';

import { Component, OnInit, Input } from '@angular/core';
import { Location } from '@angular/common';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/switchMap';

import { Service} from './services';
import { ServicesService } from './services.service';


@Component({
    selector: 'serviceupdate-app',
    template: require('./service-update.component.html'),
    providers: [ServicesService],
})


export class ServiceUpdateComponent implements OnInit {

    constructor(private servicesService: ServicesService,
                private location: Location,
                private route: ActivatedRoute) {
    }

    service: Service;

    ngOnInit(): void {
        this.route.params
            .switchMap((params: Params) => this.servicesService.getService(+params['id']))
            .subscribe(service => this.service = service['response']);
    }

    save(): void {
        this.servicesService.update(this.service)
            .subscribe((response) => {
                this.goBack()});
    }

    goBack(): void {
        location.reload();
    }
}
