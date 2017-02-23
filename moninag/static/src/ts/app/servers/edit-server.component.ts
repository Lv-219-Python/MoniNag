import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Location } from '@angular/common';


import { Server, states } from './model';
import { ServersService } from './service';
import { ServicesComponent } from '../services/services.component';
import 'rxjs/add/operator/switchMap';

@Component({
    selector: 'servers-edit',
    template: `
    <div *ngIf="server"><div>
    <h5>Server:</h5>
    <input [(ngModel)]="server.name" placeholder="{{server.name}}" />
    <h5>Address:</h5>
    <input [(ngModel)]="server.address" placeholder="{{server.address}}" />
    <button (click)="goBack()">Back</button>
    <button (click)="save()">Save</button>
    <button (click)="delete()">x</button>
    <services-app [server]='server'></services-app>
    `,
    providers: [
        ServersService
    ],
})

export class ServersEditComponent {

    constructor(
        private serversService: ServersService,
        private route: ActivatedRoute,
        private router: Router,
        private location: Location
    ){}

    server : Server[];

    ngOnInit(){
        this.route.params
            .switchMap((params: Params) => this.serversService.getServer(+params['id']))
            .subscribe(server => this.server = server['response']);
    }

    save(){
        this.serversService.putServer(this.server)
        .subscribe(() => this.goBack())
    }
    delete(){
        this.serversService.deleteServer(this.server['id'])
        .subscribe(() => this.goBack())
    }

    goBack(){
        this.location.back();
    }
}
