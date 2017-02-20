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
    selector: 'checkupdate-app',
    template: `

    <div *ngIf="check"><div>
    <h6>Name:</h6>
    <input [(ngModel)]="check.name" placeholder="{{check.name}}" />
    <h6>Run frequency:</h6>
    <select [(ngModel)]="check.run_freq">
        <option value=1>1 min</option>
        <option value=5>5 min</option>
        <option value=15>15 min</option>
        <option value=30>30 min</option>
        <option value=1>1 hour</option>
    </select>
    <h6>Plugin:</h6>
    <select [(ngModel)]="check.plugin_id">
        <option *ngFor="let plugin of plugins" value= {{plugin.id}}>
            {{plugin.name}}
        </option>
    </select>
    <h6>Target port:</h6>
    <input [(ngModel)]="check.target_port" placeholder="{{check.target_port}}" />
    <button (click)="goBack()">Back</button>
    <button (click)="save()">Save</button>
    `,

    providers: [
        ChecksService
    ],
})

export class CheckUpdateComponent implements OnInit{


    constructor(
        private checksService: ChecksService,
        private route: ActivatedRoute,
        private location: Location
    ) {}


    plugins : Plugin[];
    check : Check;

    loadPlugins(){
         this.checksService.getPlugins().subscribe(plugins => this.plugins = plugins["response"]);
                                        
    }                                     
    
    ngOnInit(): void {
        this.loadPlugins();
        this.route.params
            .switchMap((params: Params) => this.checksService.getCheck(+params['id']))
            .subscribe(check => this.check = check["response"]); 
        
    }
    save(): void {
        this.checksService.update(this.check)
            .subscribe(() => this.goBack());
    } 

    goBack(): void {
        this.location.back();
    }

    
}                                           