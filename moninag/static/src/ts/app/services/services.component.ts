import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { ServicesService } from './services.service';
import { Observable } from 'rxjs/Observable';
import { Service } from './services';
import { ServiceAddComponent } from './service-add.component';
@Component({
    selector: 'services-app',
    template: `
        <h2>Services</h2>  
        <div>  
        <ul>
            <li class="Box" *ngFor="let service of services"
                (click)="onSelect(service)" (click)="gotoDetail()">
                {{service.name}}
            </li>
        </ul>
        <button (click)="add()"> Add new service </button>
        </div>
    `,
    providers: [ ServicesService ],
    styles: [`
        .Box {
            height: 70px;
            width: 150px;
            background-color: rgba(80, 100, 170, 0.5);
            position: relative;
            box-shadow: 0 0 10px rgba(0,0,0,0.5);
            display: table-cell;
            vertical-align: middle;
            text-align: center;
            position: relative;
            padding: 1em;
            margin: 2em 10px 4em;
            background: #fff;
            -webkit-box-shadow: 0 1px 4px rgba(0, 0, 0, 0.3), 0 0 40px rgba(0, 0, 0, 0.1) inset;
            -moz-box-shadow: 0 1px 4px rgba(0, 0, 0, 0.3), 0 0 40px rgba(0, 0, 0, 0.1) inset;
            box-shadow: 0 1px 4px rgba(0, 0, 0, 0.3), 0 0 40px rgba(0, 0, 0, 0.1) inset;
            -webkit-box-shadow: 0 15px 10px -10px rgba(0, 0, 0, 0.5), 0 1px 4px rgba(0, 0, 0, 0.3), 0 0 40px rgba(0, 0, 0, 0.1) inset;
            -moz-box-shadow: 0 15px 10px -10px rgba(0, 0, 0, 0.5), 0 1px 4px rgba(0, 0, 0, 0.3), 0 0 40px rgba(0, 0, 0, 0.1) inset;
            box-shadow: 0 15px 10px -10px rgba(0, 0, 0, 0.5), 0 1px 4px rgba(0, 0, 0, 0.3), 0 0 40px rgba(0, 0, 0, 0.1) inset;
        }
        ul {
            list-style-type: none;
        }
    `]
})

export class ServicesComponent implements OnInit {
    services: Service[];
    selectedService: Service;

    
    constructor (
        private servicesService: ServicesService,
        private router: Router
    ) {}


    ngOnInit() { 
        this.getServices(); 
    }

    getServices() {
        this.servicesService.getServices().subscribe(services => this.services = services);
    }    

    onSelect(service: Service): void {
        this.selectedService = service;
    }
    gotoDetail(): void {
        this.router.navigate(['/services', this.selectedService.id]);
    }
    add() {
        this.router.navigate(['service-add']);
    }
}
