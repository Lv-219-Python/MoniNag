import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';

import { CheckAddComponent } from './check-add.component';
import { ChecksService } from './checks.service';
import { Observable } from 'rxjs/Observable';
import { Check } from './check';
import { Service } from './service';
import { Plugin } from './plugin';


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
      
    <button (click)="add()"> Add new check </button>
    <button (click)="onSelect(check)">Edit</button>
    <button (click)="delete()">Delete</button>
    <div *ngIf="selectedCheck">
    <checkupdate-app [check]='check'> </checkupdate-app>
            `,

    providers: [
        ChecksService
    ],
    styles: [`
       table, th, td {
           border: 1px solid black;}`
    ]
})

export class CheckListComponent {

    constructor(
        private checksService: ChecksService,
        private router: Router
    ){}

    @Input() service: Service[];

    
    checks : Check[];
    plugin : Plugin;
    
    selectedCheck : Check;

    onSelect(check: Check): void {
        this.selectedCheck = check;
    }

    gotoDetail(): void {
    this.router.navigate(['/checks', this.selectedCheck.id]);
    }

}