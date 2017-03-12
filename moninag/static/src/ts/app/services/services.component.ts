import { Component, OnInit, Input, ViewEncapsulation } from '@angular/core';
import { DialogPreset, DialogPresetBuilder, Modal, VexModalModule } from 'angular2-modal/plugins/vex';

import { Observable } from 'rxjs/Observable';
import { overlayConfigFactory } from "angular2-modal";
import { Router } from '@angular/router';

import { Server } from '../servers/model';
import { Service } from './services';
import { ServiceAddComponent } from './service-add.component';
import { ServicesService } from './services.service';

@Component({
    selector: 'services-app',
    template: require('./services.component.html'),
    providers: [ServicesService],
    encapsulation: ViewEncapsulation.None,
    styles: [require('./services.component.css')]
})

export class ServicesComponent {

    services: Service[];
    selectedService: Service;

    constructor(
        private servicesService: ServicesService,
        private router: Router,
        public modal: Modal
    ) { }

    @Input() server: Server[];

    onSelect(service: Service): void {
        this.selectedService = service;
    }

    gotoDetail(): void {
        this.router.navigate(['/services', this.selectedService.id]);
    }

    renderModal() {
        return new DialogPresetBuilder<DialogPreset>(this.modal)
            .content(ServiceAddComponent)
            .isBlocking(false)
            .open();
    }
}
