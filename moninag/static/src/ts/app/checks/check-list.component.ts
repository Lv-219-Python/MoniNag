import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';

import { Check } from './check';
import { CheckAddComponent } from './check-add.component';
import { ChecksService } from './checks.service';
import { Observable } from 'rxjs/Observable';
import { Plugin } from './plugin';
import { Service } from '../services/services';


@Component({
    selector: 'checks-list',
    template: require('./check-list.component.html'),
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
    ) { }

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
