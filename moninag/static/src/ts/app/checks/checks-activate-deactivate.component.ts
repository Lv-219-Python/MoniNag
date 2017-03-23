import { Component, OnInit } from '@angular/core';
import { MdDialog, MdDialogRef } from '@angular/material';

import { CheckDetailComponent } from './check-detail.component';
import { ChecksService } from './checks.service';

@Component({
  selector: 'dialog-result-dialog',
  template: require('./checks-activate-deactivate-window.html'),
})

export class ChecksDialog{
    checkState: boolean;
    actionName: string;

    constructor(public dialogRef: MdDialogRef<ChecksDialog>) {
    }
}
