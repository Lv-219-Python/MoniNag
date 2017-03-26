import { Injectable, Inject } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

import { Server } from './model';


@Injectable()
export class ServersService {

    constructor(private http: Http) { }

    private serversUrl = '/api/1/server/';

    getServers(): Observable<Server[]> {
        return this.http.get(this.serversUrl)
            .map((response: Response) => response = response.json())
            .catch((error: any) => Observable.throw(error.json().error || 'Server Error'));
    }

    getServer(id: number): Observable<Server> {
        const url = `${this.serversUrl}${id}`;
        return this.http.get(url)
            .map((response: Response) => response.json())
            .catch((error: any) => Observable.throw(error.json().error || 'Server error'));
    }

    putServer(server: any): Observable<Server[]> {
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let options = new RequestOptions({ headers: headers });
        let updatedServer = JSON.stringify({
            name: server.name,
            address: server.address,
            state: server.state
        });

        return this.http.put(`${this.serversUrl}${server['id']}/`, updatedServer, options)
            .map((response: any) => {

                if (response.status === 200) {
                    console.log("Edited!");
                };
            })
            .catch((error: any) => Observable.throw(error.json() || 'Server Error'));
    }

    addServer(server: Server): Observable<Server[]> {
        let bodyString = JSON.stringify(server);
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let options = new RequestOptions({ headers: headers });

        delete server.expanded;

        return this.http.post(this.serversUrl, server, options)
            .map((res: Response) => res.json())
            .catch((error: any) => Observable.throw(error.json().error || 'Server Error'))
    }

    deleteServer(id: number): Observable<Server[]> {
        return this.http.delete(`${this.serversUrl}${id}`)
            .map((response: any) => {

                if (response.status === 200) {
                    console.log("200");
                };
            })
            .catch((error: any) => Observable.throw(error.json() || 'Server error'));
    }

    deactivate(server: Server): Observable<Server[]> {
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let options = new RequestOptions({ headers: headers });
        let updatedServer = {
            state: false
        }
        return this.http.put(`${this.serversUrl}/${server['id']}/`, JSON.stringify(updatedServer), options)
            .catch((error: any) => Observable.throw(error.json().error || 'Server error'));
    }

    activate(server: Server): Observable<Server[]> {
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let options = new RequestOptions({ headers: headers });
        let updatedServer = {
            state: true
        }
        return this.http.put(`${this.serversUrl}/${server['id']}/`, JSON.stringify(updatedServer), options)
            .catch((error: any) => Observable.throw(error.json().error || 'Server error'));
    }

}
