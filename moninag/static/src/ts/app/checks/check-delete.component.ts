import { ActivatedRoute, Params, Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/switchMap';

import { Check } from './check';
import { ChecksService } from './checks.service';

@Component({
    selector: 'servers-delete',
    template: require('./check-delete.component.html'),
    providers: [
        ChecksService,
    ],
})


export class CheckDeleteComponent {

    constructor(
        private checksService: ChecksService,
        private route: ActivatedRoute,
        private router: Router,
        private location: Location
    ) { }

    check: Check;

    ngOnInit() {
        this.route.params
            .switchMap((params: Params) => this.checksService.getCheck(+params['id']))
            .subscribe(check => { this.check = check['response']; console.log(this.check)});
        }


    gotoServers() {
        location = 'http://127.0.0.1:8000';

    }
    delete() {
        this.checksService.remove(this.check.id)
            .subscribe(() => this.gotoServers());
    }

    goBack() {
        location.reload();
    }
}
