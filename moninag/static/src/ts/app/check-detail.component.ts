import 'rxjs/add/operator/switchMap';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Location } from '@angular/common';
import { Router }            from '@angular/router';


import { Check } from './check';
import { ChecksService } from './checks.service';


@Component({
    selector: 'checkdetail-app',
    template: `

    <div *ngIf="check"><div>
    <h6>Name:{{check.name}}</h6>
    <h6>Run frequency:{{check.run_freq}} min</h6>
    <h6>Plugin:{{check.plugin_id}}</h6>
    <h6>Target port:{{check.target_port}}</h6>
    <h6>Service:{{check.service_id}}</h6>
    <button (click)="goBack()">Back</button>
    <button (click)="update()">Update</button>
    <button (click)="delete()">Delete</button>
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


    check : Check;
    selectedCheck : Check;
                                                
    ngOnInit(): void {
        this.route.params
            .switchMap((params: Params) => this.checksService.getCheck(+params['id']))
            .subscribe(check => this.check = check["response"]); 
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
