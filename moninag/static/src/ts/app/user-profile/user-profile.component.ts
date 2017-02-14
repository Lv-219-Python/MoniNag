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
    errorMessage: any;

    constructor(private userService: UserProfileService) { }

    ngOnInit(): void {
        this.getUser();
    }

    getUser(): void {
        this.userService.getUserProfile().subscribe(
            user => this.user = user,
            error => this.errorMessage = <any>error);        
    }
}
