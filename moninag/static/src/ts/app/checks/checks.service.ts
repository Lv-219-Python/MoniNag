import { Injectable }     from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Check } from './check';
import { Observable } from 'rxjs/Rx';
import { Plugin } from './plugin';
import { Service } from '../services/services';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class ChecksService {

    constructor (private http: Http) {}
     
    private checksUrl = 'api/1/check';
    private servicesUrl = 'api/1/service';
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

    getChecks(id: number): Observable<Service> {
        const url = `${this.servicesUrl}/${id}`;
        return this.http.get(url)
                        .map((res:Response) => res = res.json())
                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    }

    update(check:Check): Observable<Check[]> {
        let headers = new Headers({ 'Content-Type': 'application/json' }); 
        let options = new RequestOptions({ headers: headers }); 
        let updated_check = {
            name: check.name,
            plugin_id: check.plugin_id,
            run_freq: check.run_freq,
            target_port:check.target_port
        }
        return this.http.put(`${this.checksUrl}/${check['id']}/`, JSON.stringify(updated_check), options)
                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    }

    create(check:Check): Observable<Check[]> {
        const url = `${this.checksUrl}/`;
        let headers = new Headers({ 'Content-Type': 'application/json' }); 
        let options = new RequestOptions({ headers: headers }); 
        let new_check = {
            name: check.name,
            plugin_id: check.plugin_id,
            run_freq: check.run_freq,
            target_port:check.target_port,
            service_id: check.service_id
        }
        return this.http.post(url, new_check, options)
                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    }

    remove(id:number): Observable<Check[]> {
        return this.http.delete(`${this.checksUrl}/${id}`)
                         .catch((error:any) => Observable.throw(error.json().error || 'Server error')); 
    } 
}
