import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

import { Service } from './services';


@Injectable()

export class ServicesService {

    private servicesUrl = 'api/1/service';

    constructor(private http: Http) { }

    getServices(): Observable<Service[]> {
        return this.http.get(this.servicesUrl)
            .map(this.extractData);
    }

    getService(id: number): Observable<Service> {
        const url = `${this.servicesUrl}/${id}`;
        return this.http.get(url)
            .map((res: Response) => res = res.json())
            .catch((error: any) => Observable.throw(error.json().error || 'Server error'));
    }

    postService(service: Service): Observable<Service[]> {
        const url = `${this.servicesUrl}/${service.id}`;
        return this.http.post(url, service)
            .map((res: Response) => res.json())
            .catch((error: any) => Observable.throw(error.json().error || 'Server error'));
    }

    update(service: Service): Observable<Service[]> {
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let options = new RequestOptions({ headers: headers });
        let updated_service = {
            name: service.name,
            status: service.status
        }

        return this.http.put(`${this.servicesUrl}/${service['id']}/`, JSON.stringify(updated_service), options)
            .catch((error: any) => Observable.throw(error.json().error || 'Server error'));
    }

    deactivate(service: Service): Observable<Service[]> {
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let options = new RequestOptions({ headers: headers });
        let updated_service = {
            state: false
        }
        return this.http.put(`${this.servicesUrl}/${service['id']}/`, JSON.stringify(updated_service), options)
            .catch((error: any) => Observable.throw(error.json().error || 'Server error'));
    }

    activate(service: Service): Observable<Service[]> {
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let options = new RequestOptions({ headers: headers });
        let updated_service = {
            state: true
        }
        return this.http.put(`${this.servicesUrl}/${service['id']}/`, JSON.stringify(updated_service), options)
            .catch((error: any) => Observable.throw(error.json().error || 'Server error'));
    }
    remove(id: number): Observable<Service[]> {
        return this.http.delete(`${this.servicesUrl}/${id}`)
            .catch((error: any) => Observable.throw(error.json().error || 'Server error'));
    }

    create(service: Service): Observable<Service[]> {
        const url = `${this.servicesUrl}/`;
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let options = new RequestOptions({ headers: headers });
        let new_service = {
            name: service.name,
            status: service.status,
            server_id: service.server_id,
        }
        return this.http.post(url, new_service, options)
            .catch((error: any) => Observable.throw(error.json().error || 'Server error'));
    }

    private extractData(res: Response) {
        let body = res.json();
        return body.response;
    }
}
