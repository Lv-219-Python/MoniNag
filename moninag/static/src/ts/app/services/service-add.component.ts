import { ActivatedRoute } from '@angular/router';
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

    model = new Service(0, '', 'UNKNOWN', null, null);

    constructor(
        private servicesService: ServicesService,
        private route: ActivatedRoute,
        private location: Location
    ) { }

    add() {
        this.route.params.
            subscribe(params => {
                // (+) converts string 'id' to a number
                this.model.server_id = +params['id'];
            });

        this.servicesService.create(this.model)
            .subscribe(
            model => model = model
            );
    }

    goBack(): void {
        location.reload();
    }
}
