import { ActivatedRoute } from '@angular/router';
import { Component } from '@angular/core';
import { Location } from '@angular/common';

import { Check } from './check';
import { ChecksService } from './checks.service';
import { onlyDigits } from '../validations/patterns';
import { Service } from '../services/services';


@Component({
    selector: 'checkadd-app',
    template: require('./check-add.component.html'),
    providers: [ChecksService]
})


export class CheckAddComponent {

    model = new Check();

    constructor(
        private checksService: ChecksService,
        private route: ActivatedRoute,
        private location: Location
    ) { }

    plugins: Plugin[];
    services: Service[];
    onlyDigits = onlyDigits;

    loadPlugins() {
        this.checksService.getPlugins()
            .subscribe(plugins => this.plugins = plugins['response']);
    }

    ngOnInit(): void {
        this.loadPlugins();
    }

    add() {
        this.route.params.
            subscribe(params => {
                // (+) converts string 'id' to a number
                this.model.service_id = +params['id'];
            });

        this.checksService.create(this.model)
            .subscribe(model => model = model);
    }

    goBack(): void {
        location.reload();
    }
}
