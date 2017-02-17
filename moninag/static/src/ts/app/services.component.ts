import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { ServicesService } from './services.service';
import { Observable } from 'rxjs/Observable';
import { Service } from './services';
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
            display:table-cell;
            vertical-align: middle;
            text-align: center;
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
}

/////////////////////////////////////////////////////





/* 
http://127.0.0.1:8000/api/1/service/21/
export class ServicesComponent implements OnInit {

    constructor(
        private router: Router,
        private servicesService: ServicesService) { }


    getServices(): void {
    this.ServicesService.getHeroes().then(heroes => this.heroes = heroes);
  }


    ngOnInit(): void {
    this.();
  }

}
*/ 
