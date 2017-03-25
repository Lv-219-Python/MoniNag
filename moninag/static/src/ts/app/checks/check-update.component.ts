import { ActivatedRoute, Params, Router } from '@angular/router';

import { Component, OnInit, Input } from '@angular/core';
import { Location } from '@angular/common';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/switchMap';

import { Check } from './check';
import { CheckListComponent } from './check-list.component';
import { ChecksService } from './checks.service';
import { onlyDigits } from '../validations/patterns';
import { Plugin } from './plugin';


@Component({
    selector: 'checkupdate-app',
    template: require('./check-update.component.html'),
    providers: [ChecksService],
})


export class CheckUpdateComponent implements OnInit {

    constructor(
        private checksService: ChecksService,
        private location: Location,
        private route: ActivatedRoute
    ) { }

    check: Check;
    plugins: Plugin[];
    onlyDigits = onlyDigits;

    loadPlugins() {
        this.checksService.getPlugins()
            .subscribe(plugins => this.plugins = plugins['response']);
    }

    ngOnInit(): void {
        this.route.params
            .switchMap((params: Params) => this.checksService.getCheck(+params['id']))
            .subscribe(check => {this.check = check['response']});
        this.loadPlugins();
    }

    save(): void {
        this.checksService.update(this.check)
            .subscribe(() => this.goBack());
    }

    goBack(): void {
        location.reload();
    }
}
