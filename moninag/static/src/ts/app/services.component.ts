import { Component, OnInit } from '@angular/core';

import { ServicesService } from './services.service';
import { Observable } from 'rxjs/Observable';
import { Services } from './services';

@Component({
    selector: 'services-app',
    templateUrl: 'static/src/ts/app/services.component.html',
    styleUrls: ['static/src/ts/app/services.component.css'],
})

export class ServicesComponent implements OnInit {
    services: Services[];
    selectedService: Services;

    constructor(
        private servicesService: ServicesService){}

    getServices(): void {
        this.servicesService
            .getServices()
            .subscribe(services => this.services = services);
    }

    ngOnInit(): void {
        this.getServices();
    }
}




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
