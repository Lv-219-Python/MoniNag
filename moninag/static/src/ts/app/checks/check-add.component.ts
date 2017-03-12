import { Component } from '@angular/core';
import { Location } from '@angular/common';

import { Check } from './check';
import { ChecksService } from './checks.service';
import { Service } from '../services/services';


@Component({
    selector: 'checkadd-app',
    template: require('./check-add.component.html'),
    providers: [ChecksService]
})


export class CheckAddComponent {

    model = new Check(10, '', null, null, null, null, null, null, null, null);

    constructor(
        private checksService: ChecksService,
        private location: Location
    ) { }

    plugins: Plugin[];
    services: Service[];

    loadPlugins() {
        this.checksService.getPlugins()
            .subscribe(plugins => this.plugins = plugins['response']);
    }

    ngOnInit(): void {
        this.loadPlugins();
    }

    add() {
        this.checksService.create(this.model)
            .subscribe(model => model = model);
    }

    goBack(): void {
        location.reload();
    }
}
