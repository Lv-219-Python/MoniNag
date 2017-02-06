import { Component, OnInit } from '@angular/core';
import { Router }            from '@angular/router';
import { DBListComponent }   from './db-list';

@Component({
    selector: 'services-app',
    templateUrl: 'static/src/ts/app/services.component.html',
    styleUrls: ['static/src/ts/app/services.component.css'],
})

export class ServicesComponent {
    
}




/* 
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
