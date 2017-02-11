import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, Params } from '@angular/router';

import { AlertService, ResetPasswordService } from '../_services/index';

@Component({
    selector: 'confirm-password-reset',
    template: require('./confirm_password_reset.component.html')
})

export class ConfirmPasswordResetComponent implements OnInit {
    model: any = {};
    loading = false;
    uidb64: string = null;
    token: string = null;

    constructor(
        private route: ActivatedRoute,
        private router: Router,
        private resetPasswordService: ResetPasswordService,
        private alertService: AlertService) { }

    ngOnInit() {
        this.route.params.subscribe((params: Params) => {
            this.uidb64 = params['uidb64'];
            this.token = params['token'];
        })
    }

    confirmPasswordReset() {
        this.loading = true;
        this.resetPasswordService.confirmPasswordReset(this.model.password, this.uidb64, this.token)
            .subscribe(
                    data => {
                        if(data.success) {
                            this.alertService.success(data.message, true);
                            setTimeout(() => {this.router.navigate(['/auth'])}, 5000);
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
