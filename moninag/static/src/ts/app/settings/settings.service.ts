import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

import { Plugin } from './plugin';


@Injectable()

export class SettingsService {

    constructor(private http: Http) { }

    private pluginsUrl = 'api/1/nagplugin';

    getPlugins(): Observable<Plugin[]> {
        return this.http.get(this.pluginsUrl)
            .map((res: Response) => res = res.json())
            .catch(this.handleError);
    }

    private handleError(error: Response | any) {
        let errMsg: string;
        if (error instanceof Response) {
            const body = error.json() || '';
            const err = body.error || JSON.stringify(body);
            errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
        } else {
            errMsg = error.message ? error.message : error.toString();
        }
        console.error(errMsg);
        return Observable.throw(errMsg);
    }
}
