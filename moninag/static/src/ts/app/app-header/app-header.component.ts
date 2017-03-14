import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { UserProfile } from '../user-profile/user-profile';
import { UserProfileService } from '../user-profile/user-profile.service';
import { MainNavComponent } from '../navs/main-nav/main-nav.component'

@Component({
    selector: 'app-header',
    template: require('./app-header.component.html'),
    styles: [require('./app-header.less').toString()],
})

export class AppHeaderComponent implements OnInit {
    title = 'MoniNag';
    motto = 'Your monitoring friend';
    user: UserProfile;
    errorMessage: any;

    constructor(
        private userService: UserProfileService,
        private router: Router,
    ) { }

    ngOnInit(): void {
        this.getUser();
    }

    getUser(): void {
        this.userService.getUserProfile().subscribe(
            user => this.user = user,
            error => this.errorMessage = <any>error);
    }

    viewProfile(): void {
        this.router.navigateByUrl('settings');
    }

    logOut(): void {
        window.location.href = '/auth/logout/';
    }
}
