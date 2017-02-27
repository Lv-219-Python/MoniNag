import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Location } from '@angular/common';
import 'rxjs/add/operator/switchMap';

import { Check } from './check';
import { ChecksService } from './checks.service';
import { CheckUpdateComponent } from './check-update.component';


@Component({
    selector: 'checkdetail-app',
    template: require('./check-detail.component.html'),
    providers: [ChecksService]
})


export class CheckDetailComponent implements OnInit {

    constructor(
        private checksService: ChecksService,
        private route: ActivatedRoute,
        private location: Location
    ) { }

    check: Check;
    selectedCheck: Check;

    ngOnInit(): void {
        this.route.params
            .switchMap((params: Params) => this.checksService.getCheck(+params['id']))
            .subscribe(check => this.check = check['response']);
    }

    onSelect(check: Check): void {
        this.selectedCheck = check;
    }

    delete(): void {
        this.checksService.remove(this.check.id)
            .subscribe(() => this.goBack());
    }

    goBack(): void {
        this.location.back();
    }
}
