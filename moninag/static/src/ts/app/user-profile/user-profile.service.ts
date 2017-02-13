import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { UserProfile } from './user-profile'


@Injectable()
export class UserProfileService {
    private profileURL = '/api/1/profile/';

    constructor(private http: Http) { }

    getUserProfile(): Promise<UserProfile> {
        return this.http.get(this.profileURL)
            .toPromise()
            .then(this.handleResponse)
            .catch(this.handleError);
    }

    private handleResponse(response: any): Promise<UserProfile> {
        let responseData = response.json()['response'] as UserProfile
        return Promise.resolve(responseData);
    }

    private handleError(error: any): Promise<any> {
        console.error('An error occurred', error);
        return Promise.reject(error.message || error);
    }
}
