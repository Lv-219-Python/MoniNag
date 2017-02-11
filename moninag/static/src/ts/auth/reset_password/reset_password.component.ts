import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

import { AlertService, AuthenticationService, ResetPasswordService } from '../_services/index';

@Component({
    selector: 'reset_password',
    template: require('./reset_password.component.html')
})

export class ResetPasswordComponent {
    model: any = {};
    loading = false;

    constructor(
        private route: ActivatedRoute,
        private router: Router,
        private authenticationService: AuthenticationService,
        private resetPasswordService: ResetPasswordService,
        private alertService: AlertService) { }

    resetPassword() {
        this.loading = true;
        this.resetPasswordService.resetPassword(this.model.email)
            .subscribe(
                    data => {
                        if(data.success) {
                            this.alertService.success(data.message, true);
                        } else {
                            this.alertService.error(data.error);
                            this.loading = false;
                        }
                    },
                    error => {
                        this.alertService.error(error._body);
                        this.loading = false;
                    }
                );
    }
}
