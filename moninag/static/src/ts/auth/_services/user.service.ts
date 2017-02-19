import { Injectable } from "@angular/core";
import { Http, Headers, Response, RequestOptions } from "@angular/http";
import { Observable } from "rxjs";


@Injectable()
export class UserService {
    constructor(private http: Http) { }
    registerUser(user: any) {
        let headers = new Headers({ 'Content-Type': 'application/json', 'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest' });
        let options = new RequestOptions({ headers: headers });
        let body = JSON.stringify(user);
        return this.http.post('/auth/register_user/', body, options).map((res: Response) => res.json());
    }
}
