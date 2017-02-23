import { Component } from '@angular/core';
import { Location } from '@angular/common';

import { Service } from './services';
import { ServicesService } from './services.service';


@Component({
    selector: 'serviceadd-app',
    template: `
    <div class="container">
        <form>
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text"
                       required [(ngModel)]="model.name" name="name">
            </div>
            <div class="form-group">
                <label for="status">Status</label>
                <input type="text" 
                       required [(ngModel)]="model.status" name="status">
            </div>
            <div class="form-group">
                <label for="server_id">Server id</label>
                <input type="text"
                        required [(ngModel)]="model.server_id" name="status">
            </div>
        </form>
        <button (click)="goBack()">Back</button>
        <button type="submit" (click)="add(); goBack()">Submit</button>
    </div>
    `,
    providers: [ ServicesService ]
})

export class ServiceAddComponent {

    model = new Service(0, '', null, null);

    constructor (
        private servicesService: ServicesService,
        private location: Location
        ) {}

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
