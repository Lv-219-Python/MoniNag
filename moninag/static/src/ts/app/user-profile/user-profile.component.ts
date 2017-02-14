import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';


import { UserProfile } from './user-profile';
import { UserProfileService } from './user-profile.service';


@Component({
    selector: 'user-profile',
    template: require('./user-profile.component.html'),
    providers: [UserProfileService]
})

export class UserProfileComponent implements OnInit {

    user: UserProfile;

    constructor(private userService: UserProfileService) { }

    ngOnInit(): void {
        this.getUser();
    }

    getUser(): void {
        this.userService.getUserProfile().then(userResponse => this.user = userResponse);
    }
}
