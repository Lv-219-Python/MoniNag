import { Injectable }     from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Plugin } from './plugin'
import {Observable} from 'rxjs/Rx';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class ChecksService {

    constructor (private http: Http) {}
     
    private checksUrl = 'api/checks/'; 

    getPlugins() : Observable<Plugin[]> {
        return this.http.get(this.checksUrl)
                        .map((res:Response) => res = JSON.parse(res.json()))
                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
                        
    }
}
            

   