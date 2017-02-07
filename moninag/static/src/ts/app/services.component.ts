import { Component, OnInit } from '@angular/core';

import { ServicesService } from './services.service';
import { Observable } from 'rxjs/Observable';
import { Service } from './services';

@Component({
    selector: 'services-app',
    templateUrl: 'static/src/ts/app/services.component.html',
    providers: [ ServicesService ],
    styleUrls: ['static/src/ts/app/services.component.css'],
})

export class ServicesComponent implements OnInit {
    // services: Service[];
    services: Service[];
    oneService: Service;
    mode = 'Observable';

    constructor (private servicesService: ServicesService) {}

    ngOnInit() { 
        this.getServices(); 
        this.getService(21); 
    }

    getService(id: number) {
        this.servicesService.getService(id)
                            .subscribe(
                                service => this.oneService = service);
    }    

    getServices() {
        this.servicesService.getServices()
                            .subscribe(
                                services => this.services = services);
    }    
    // addService(name: string) {
    //     if (!name) { return; }
    //     this.servicesService.addService(name)
    //                         .subscribe(
    //                             service =>this.services.push(service));
    //     }

    my() {
       console.log(this.services)
     }
    foo() {
       console.log(this.oneService)
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
