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
                private location: Location) {
    }

    @Input() service: Service;

    ngOnInit(): void {
    }

    save(): void {
        this.servicesService.update(this.service)
            .subscribe(() => this.goBack());
    }

    goBack(): void {
        this.location.back();
    }
}
