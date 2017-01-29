import { Component, OnInit } from '@angular/core';

import { AlertService } from '../_services/index';

@Component({
    selector: 'message',
    templateUrl: 'static/src/ts/app/registration/message/message.component.html'
})

export class MessageComponent {
    message: any;

    constructor(private alertService: AlertService) { }

    ngOnInit() {
        this.alertService.getMessage().subscribe(message => { this.message = message; });
    }
}
