import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';

import { Check } from './check';
import { CheckAddComponent } from './check-add.component';
import { ChecksService } from './checks.service';
import { Observable } from 'rxjs/Observable';
import { Plugin } from './plugin';
import { Service } from '../services/services';


@Component({ 
    selector:'checks-list',
    template:`
    <div class="table-responsive">
        <ul style="list-style-type:none; padding:0">          
            <table class="table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Plugin name</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><li *ngFor="let check of service.checks" (click)="onSelect(check); gotoDetail()" value={{check.id}>{{check.name}}</li></td>
                        <td><li *ngFor="let check of service.checks" (click)="onSelect(check); gotoDetail()" value={{check.id}>{{check.plugin_name}}</li></td>
                        <td><li *ngFor="let check of service.checks" (click)="onSelect(check); gotoDetail()" value={{check.id}>{{check.status}}</li></td>
                    </tr>
                </tbody>
            </table>
        </ul>
        <button (click)="onSelect2(service)"> Add new check </button>
        <div *ngIf="selectedService">
            <checkadd-app></checkadd-app>
        </div>
    </div>
    `,
    providers: [ChecksService],
    styles: [`
       table, th, td {
           border: 1px solid black;}`
    ]
})


export class CheckListComponent {

    constructor(
        private checksService: ChecksService,
        private router: Router
    ) {}

    @Input() service: Service[];

    checks: Check[];
    plugin: Plugin;
    
    selectedCheck: Check;
    selectedService: Service;

    onSelect(check: Check): void {
        this.selectedCheck = check;
    }

    onSelect2(service: Service): void {
        this.selectedService = service;
    }

    gotoDetail(): void {
    this.router.navigate(['/checks', this.selectedCheck.id]);
    }
}

