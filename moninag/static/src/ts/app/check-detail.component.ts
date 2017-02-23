import 'rxjs/add/operator/switchMap';
import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Location } from '@angular/common';
import { Router }            from '@angular/router';


import { CheckUpdateComponent } from './check-update.component';
import { Check } from './check';
import { ChecksService } from './checks.service';


@Component({
    selector: 'checkdetail-app',
    template: `

    <div *ngIf="check"><div>
    <h6>Name:{{check.name}}</h6>
    <h6>Run frequency:{{check.run_freq}} min</h6>
    <h6>Plugin id:{{check.plugin_id}}</h6>
    <h6>Target port:{{check.target_port}}</h6>
    <h6>Last run:</h6>
    <h6>Output:</h6>
    <h6>Status:</h6>
    <h6>Active:</h6>
    <button (click)="onSelect(check)">Edit</button>
    <button (click)="delete()">Delete</button>
    <div *ngIf="selectedCheck">
    <checkupdate-app [check]='check'> </checkupdate-app>
    <div>
    `,

    providers: [
        ChecksService
    ],
})

export class CheckDetailComponent implements OnInit{


    constructor(
        private checksService: ChecksService,
        private route: ActivatedRoute,
        private location: Location,
        private router: Router
    ) {}

    check: Check;
    selectedCheck : Check;
                                                
    ngOnInit(): void {
        this.route.params
            .switchMap((params: Params) => this.checksService.getCheck(+params['id']))
            .subscribe(check => this.check = check["response"]); 
    }

     onSelect(check: Check): void {
        this.selectedCheck = check;
    }

    update(): void {
    this.router.navigate(['/checks/update', this.check.id]);
    }

    delete(): void {
        this.checksService.remove(this.check.id)
            .subscribe(() => this.goBack());
    } 

    goBack(): void {
    this.location.back();
    }
}
