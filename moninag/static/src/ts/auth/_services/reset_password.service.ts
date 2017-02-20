import { Injectable } from '@angular/core';
import { Http, Headers, Response, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map'

@Injectable()
export class ResetPasswordService {
    constructor(private http: Http) { }

    resetPassword(email: string) {
        let headers = new Headers({ 'Content-Type': 'application/json', 'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'});
        let options = new RequestOptions({ headers: headers });
        let body = JSON.stringify({'email': email});
        return this.http.post('/auth/reset_password', body, options).map((res: Response) => res.json());
    }

    confirmPasswordReset(password: string, uidb64: string, token: string) {
        let headers = new Headers({ 'Content-Type': 'application/json', 'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'});
        let options = new RequestOptions({ headers: headers });
        let body = JSON.stringify({'password': password, 'uidb64': uidb64, 'token': token });
        return this.http.post(`/auth/confirm_password_reset/${uidb64}/${token}/`, body, options).map((res: Response) => res.json());
    }
}
