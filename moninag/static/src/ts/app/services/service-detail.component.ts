import { ActivatedRoute, Params, Router } from '@angular/router';
import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { DialogPreset, DialogPresetBuilder, Modal, VexModalModule } from 'angular2-modal/plugins/vex';
import { Location } from '@angular/common';
import { MdDialog, MdDialogRef } from '@angular/material';

import { overlayConfigFactory } from "angular2-modal";

import { Service } from './services';
import { ServicesService } from './services.service';
import { ServiceDeleteComponent } from './service-delete.component';
import { ServiceUpdateComponent } from './service-update.component';
import { ServicesDialog } from './services-activate-deactivate.component';

@Component({
    selector: 'services-detail',
    template: require('./service-detail.component.html'),
    providers: [ServicesService],
    encapsulation: ViewEncapsulation.None
})

export class ServiceDetailComponent implements OnInit {

    constructor(private route: ActivatedRoute,
                private location: Location,
                private servicesService: ServicesService,
                public modal: Modal,
                public dialog: MdDialog,) {
    }

    service: Service;
    selectedService: Service;

    ngOnInit(): void {
        this.route.params
            .switchMap((params: Params) => this.servicesService.getService(+params['id']))
            .subscribe(service => this.service = service["response"]);
    }

    openDialog($event:any) {
        let dialogRef = this.dialog.open(ServicesDialog);
        dialogRef.componentInstance.serviceState = this.service.state;
        dialogRef.componentInstance.actionName = this.service.state ? 'deactivate' : 'activate';
        dialogRef.afterClosed().subscribe(result => {
            if (result === undefined) return;
            result ? this.activate() : this.deactivate();
        });
    }

    onSelect(service: Service): void {
        this.selectedService = service;
    }

    deleteModal() {
        return new DialogPresetBuilder<DialogPreset>(this.modal)
            .content(ServiceDeleteComponent)
            .isBlocking(false)
            .open();
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

    renderModal() {
        return new DialogPresetBuilder<DialogPreset>(this.modal)
            .content(ServiceUpdateComponent)
            .isBlocking(false)
            .open();
    }
}
