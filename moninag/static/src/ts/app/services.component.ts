import { Component, OnInit } from '@angular/core';

import { ServicesService } from './services.service';
import { Observable } from 'rxjs/Observable';
import { Service } from './services';


@Component({
    selector: 'services-app',
    template: `
        <h2> Services ({{mode}}) </h2>  
        <div>  
        <ul>
            <li class="Box" *ngFor="let service of services">
            <a href="api/1/service/{{service.id}}"> {{service.name}} </a></li>
        </ul>
        </div>
        <button (click)="my();">
            Services
        </button>

        <button (click)="foo();">
            Service(21)
        </button>


        <!-- <input #id (keyup)="0">
        <p>{{id.value}}</p> -->

        <input #box (keyup.enter)="onEnter(box.value);">

        <p>{{value}}</p>

    `,
    providers: [ ServicesService ],
    styles: [`
        .test1 {
            margin: 20px;
            padding: 20px;
        }
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
    oneService: Service;
    mode = 'Observable';

    value = '';



    
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


    getTrueService(){

    }
    // addService(name: string) {
    //     if (!name) { return; }
    //     this.servicesService.addService(name)
    //                         .subscribe(
    //                             service =>this.services.push(service));
    //     }
    onEnter(value: string) {
        this.value = value;
        console.log("this.services")
    }
    my() {
       console.log(this.services)
     }
    foo() {
       console.log(this.oneService)
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
