import { Component } from '@angular/core';
import { Location } from '@angular/common';

import { Service } from './services';
import { ServicesService } from './services.service';


@Component({
    selector: 'serviceadd-app',
    template: require('./service-add.component.html'),
    providers: [ServicesService]
})

export class ServiceAddComponent {

    model = new Service(0, '', null, null);

    constructor(
        private servicesService: ServicesService,
        private location: Location
    ) { }

    add() {
        this.servicesService.create(this.model)
            .subscribe(
            model => model = model
            );
    }

    goBack(): void {
        this.location.back();
    }
}
