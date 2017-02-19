import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { AlertService, UserService } from '../_services/index';


@Component({
    template: require('./register.component.html')
})

export class RegisterComponent {
    model: any = {};
    loading = false;

    constructor(
        private router: Router,
        private userService: UserService,
        private alertService: AlertService) { }

    register() {
        this.loading = true;
        this.userService.registerUser(this.model)
            .subscribe(
                data => {
                    if (data.success) {
                        this.alertService.success(data.message, true);
                        setTimeout(() => { this.router.navigate(['/auth']) }, 5000);
                    } else {
                        this.alertService.error(data.error);
                        this.loading = false;
                    }
                },
                error => {
                    debugger;
                    this.alertService.error(error);
                    this.loading = false;
                }
            );
    }
}
