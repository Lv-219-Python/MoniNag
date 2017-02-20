import { Component } from '@angular/core';
import { Location } from '@angular/common';

import { Check } from './check';
import { Service } from './service';
import { ChecksService } from './checks.service';



@Component({
    selector: 'checkadd-app',
    template: `

    <div class="container">
        <form>
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text"
                       required
                       [(ngModel)]="model.name" name="name">
            </div>
            <div class="form-group">
                <label for="target_port">Target port</label>
                <input type="text" 
                       required
                       [(ngModel)]="model.target_port" name="target_port">
            </div>
            <div class="form-group">
                <label for="run_freq">Run frequency</label>
                <select required
                        [(ngModel)]="model.run_freq" name="run_freq">
                    <option value=1>1 min</option>
                    <option value=5>5 min</option>
                    <option value=15>15 min</option>
                    <option value=30>30 min</option>
                    <option value=1>1 hour</option>
                </select>
            </div>
            <div class="form-group">
                <label for="plugin_id">Plugin</label>
                <select required
                        [(ngModel)]="model.plugin_id" name="plugin_id">
                    <option *ngFor="let plugin of plugins" [value]="plugin.id">{{plugin.name}}</option>
                </select>
            </div>
            <div class="form-group">
                <label for="service_id">Service id</label>
                <select required
                        [(ngModel)]="model.service_id" name="service_id">
                    <option *ngFor="let service of services" [value]="service.id">{{service.name}}</option>
                </select>
            </div>
        </form>
        <button (click)="goBack()">Back</button>
        <button type="submit" (click)="add(); goBack()">Submit</button>
    </div>
    `,
    providers: [ ChecksService ]
})

export class CheckAddComponent {

    model = new Check(10, '', null, null, null , null);
    
    constructor (
        private checksService: ChecksService,
        private location: Location
        ) {}

    plugins : Plugin[];
    services : Service[];

    loadPlugins(){
        this.checksService.getPlugins().subscribe(plugins => this.plugins = plugins["response"]);
                                        
    } 

    loadServices(){
        this.checksService.getServices().subscribe(services => this.services = services["response"]);

    }                                    
    
    ngOnInit(): void {
        this.loadPlugins();
        this.loadServices();
    }

    add() {

        this.checksService.create(this.model)
                          .subscribe(
                              model => model = model
                          );
    }

    goBack(): void {
        this.location.back();
    }


}
