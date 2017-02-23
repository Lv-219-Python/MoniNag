import { Component, OnInit, Input } from '@angular/core';
import { Location } from '@angular/common';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/switchMap';

import { Check } from './check';
import { CheckListComponent } from './check-list.component';
import { ChecksService } from './checks.service';
import { Plugin } from './plugin';


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
    <h6>Active:</h6>
    <input type="checkbox" name="not-active" value="False"> Deactivate <br>
    <button (click)="goBack()">Cancel</button>
    <button (click)="save()">Save</button>
    `,

    providers: [
        ChecksService
    ],
})

export class CheckUpdateComponent implements OnInit{

    constructor(
        private checksService: ChecksService,
        private location: Location
    ) {}

    @Input() check: Check;

    plugins : Plugin[];

    loadPlugins(){
         this.checksService.getPlugins().subscribe(plugins => this.plugins = plugins["response"]);
    }                                     
    
    ngOnInit(): void {
        this.loadPlugins();
    }

    save(): void {
        this.checksService.update(this.check)
    } 

    goBack(): void {
        this.location.back();
    }    
}
