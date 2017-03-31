import { Component, OnInit } from '@angular/core';
import { MdDialog, MdDialogRef } from '@angular/material';

import { ServiceDetailComponent } from './service-detail.component';
import { ServicesService } from './services.service';

@Component({
  selector: 'services-dialog',
  template: require('./services-activate-deactivate-window.html'),
})

export class ServicesDialog {
    serviceState: boolean;
    actionName: string;

    constructor(public dialogRef: MdDialogRef<ServicesDialog>) {
    }
}
