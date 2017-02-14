import { Injectable }     from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import { Plugin } from './plugin';
import { Check } from './check';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class ChecksService {

    constructor (private http: Http) {}
     
    private checksUrl = 'api/checks';
    private pluginsUrl = 'api/plugins';
     

    getCheck(id: number): Observable<Check[]> {
        const url = `${this.checksUrl}/${id}`;
        return this.http.get(url)
            .map((res:Response) => res = res.json())
            .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    }
  

    getPlugins() : Observable<Plugin[]> {
        return this.http.get(this.pluginsUrl)
                        .map((res:Response) => res = res.json())
                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    }

    getChecks() : Observable<Check[]> {
        return this.http.get(this.checksUrl)
                        .map((res:Response) => res = res.json())
                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));                   
    }
}
            

   