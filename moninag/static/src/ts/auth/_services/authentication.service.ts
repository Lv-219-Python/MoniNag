import { Injectable } from '@angular/core';
import { Http, Headers, Response, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map'

@Injectable()
export class AuthenticationService {
    constructor(private http: Http) { }

    login(email: string, password: string) {
        let headers = new Headers({ 'Content-Type': 'application/json', 'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'});
        let options = new RequestOptions({ headers: headers });
        let body = JSON.stringify({'email': email, 'password': password});
        return this.http.post('/accounts/login/', body, options).map((res: Response) => res.json());
    }
}
