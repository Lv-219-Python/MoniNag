import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { AlertService, UserService } from '../_services/index';

@Component({
    templateUrl: 'static/src/ts/app/registration/register/register.component.html'
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
                    if(data.success) {
                        this.alertService.success(data.message, true);
                        setTimeout(() => {this.router.navigate(['/accounts'])}, 5000);
                    } else {
                        this.alertService.error(data.error);
                        this.loading = false;
                    }
                },
                error => {
                    this.alertService.error(error);
                    this.loading = false;
                });
    }
}
