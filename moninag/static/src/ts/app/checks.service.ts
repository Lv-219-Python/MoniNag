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
     
    private checksUrl = 'api/1/check';
    private pluginsUrl = 'api/1/nagplugin';
     

    getCheck(id: number): Observable<Check> {
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

    /*update(check: Check): Observable<Check> {
        const url = `${this.checksUrl}/${check.id}`;
        return this.http
            .put(url, JSON.stringify(check))
            .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    }*/

    postCheck(check: Check): Observable<Check> {
        const url = `${this.checksUrl}/${check.id}`;
        return this.http
            .post(url, check)
            .map((res:Response) => res.json())
            .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    }

    create(name: string): Observable<Check> {
        return this.http
            .post(this.checksUrl, JSON.stringify({name: name}))
            .map(res => res.json().data)
            .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
            
    }

    update(check:Check): Observable<Check[]> {
        let headers = new Headers({ 'Content-Type': 'application/json' }); // ... Set content type to JSON
        let options = new RequestOptions({ headers: headers }); // Create a request option
        let new_check = {
            name: check.name,
            plugin_id: check.plugin_id,
            run_freq: check.run_freq,
            target_port:check.target_port
        }
        return this.http.put(`${this.checksUrl}/${check['id']}/`, JSON.stringify(new_check), options)
                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    }
 
}
            

   