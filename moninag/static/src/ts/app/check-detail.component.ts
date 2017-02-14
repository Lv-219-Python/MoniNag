import 'rxjs/add/operator/switchMap';
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { ActivatedRoute, Params } from '@angular/router';
import { Location } from '@angular/common';

import { Check } from './check';
import { Plugin } from './plugin';
import { CheckListComponent } from './check-list.component';
import { ChecksService } from './checks.service';


@Component({
    selector: 'checkdetail-app',
    template: `

    <div *ngIf="check">
    <h6>Name:{{check.name}}</h6>
    <p>Plugins:</p>
    <select>
        <option *ngFor="let plugin of plugins" value= {{plugin.id}}>
            {{plugin.name}}
        </option>
    </select>
    <p>Target port:{{portname}}</p>
    <p>Check-frequency:</p>
    <select>
        <option value="1 min">1 min</option>
        <option value="5 min">5 min</option>
        <option value="15 min">15 min</option>
        <option value="30 min">30 min</option>
        <option value="1 hour">1 hour</option>
    </select>
    <div>
    <button (click)="goBack()">Back</button>
    </div>
    `,

    providers: [
        ChecksService
    ],
})

export class CheckDetailComponent implements OnInit{


    constructor(
        private checksService: ChecksService,
        private route: ActivatedRoute,
        private location: Location
    ) {}


    plugins : Plugin[];
    check : Check[];
 

    loadPlugins(){
         this.checksService.getPlugins().subscribe(plugins => this.plugins = plugins);
                                        
    }                                               
    
    ngOnInit(): void {
        this.loadPlugins();
        this.route.params
            .switchMap((params: Params) => this.checksService.getCheck(+params['id']))
            .subscribe(check => this.check = check);
    }


    goBack(): void {
    this.location.back();
    }

   
    
    portname = 'Port1';
}
