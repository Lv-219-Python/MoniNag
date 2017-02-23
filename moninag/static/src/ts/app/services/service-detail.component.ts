import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Location } from '@angular/common';

import { Service } from './services';
import { ServicesService } from './services.service';
import { CheckListComponent} from '../check-list.component';

@Component({
    selector: 'services-detail',
    template: `
        <div *ngIf="service">
            <h3>Service Details</h3>
            <div>
                <label>name: </label>
                <input [(ngModel)]="service.name" placeholder="{{service.name}}"/>
            </div>

            <div>
                <label>status: </label>{{service.status}}
            </div>

            <div>
                <label>id: </label>{{service.id}}
            </div>

            <div>
                <label>server id: </label>{{service.server_id}}
            </div>
        <button (click)="goBack()">Back</button>
        <button (click)="save()">Save</button>
        <button (click)="delete()">Delete</button>
        <checks-list [service]='service'> </checks-list>
        </div>
    `,
    providers: [ ServicesService ]
})

export class ServiceDetailComponent implements OnInit {

    constructor(
        private route: ActivatedRoute,
        private location: Location,
        private router: Router,
        private servicesService: ServicesService
        ) {}



    service: Service;
    selectedService: Service;

    ngOnInit(): void {
        this.route.params
            .switchMap((params: Params) => this.servicesService.getService(+params['id']))
            .subscribe(service => this.service = service["response"]); 
    }
    goBack(): void {
        this.location.back();
    }

    onSelect(service: Service): void {
        this.selectedService = service;
    }    
    save(): void {
        this.servicesService.update(this.service)
                            .subscribe(() => this.goBack());
    }
    delete(): void {
        this.servicesService.remove(this.service.id)
            .subscribe(() => this.goBack());
    } 
}

