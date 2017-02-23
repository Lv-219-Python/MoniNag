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
                        .map((res:Response) => res = res.json())
                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    }

    postService(service: Service): Observable<Service[]>{
        const url = `${this.servicesUrl}/${service.id}`;
        return this.http.post(url, service)
                        .map((res:Response) => res.json())
                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    }

    update(service:Service): Observable<Service[]> {
        let headers = new Headers({ 'Content-Type': 'application/json' }); 
        let options = new RequestOptions({ headers: headers }); 
        let updated_service = {
            name: service.name,
            status: service.status,
        }
        return this.http.put(`${this.servicesUrl}/${service['id']}/`, JSON.stringify(updated_service), options)
                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    }

    remove(id:number): Observable<Service[]> {
        return this.http.delete(`${this.servicesUrl}/${id}`)
                         .catch((error:any) => Observable.throw(error.json().error || 'Server error')); 
    }

    create(service:Service): Observable<Service[]> {
        const url = `${this.servicesUrl}/`;
        let headers = new Headers({ 'Content-Type': 'application/json' }); 
        let options = new RequestOptions({ headers: headers }); 
        let new_service = {
            name: service.name,
            status: service.status,
            server_id: service.server_id,
        }
        return this.http.post(url, new_service, options)
                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    }

    private extractData(res: Response) {
        let body = res.json();
        return body.response;
    }

    // update(service: Service): Observable<Service[]>{
    //     let headers = new Headers({ 'Content-Type': 'application/json' }); 
    //     let options = new RequestOptions({ headers: headers }); 
    //     let updated_service = {
    //         name: service.name,
    //         server_id: service.server_id
    //     }
    //     return this.http.put(`${this.servicesUrl}/${service['id']}/`, JSON.stringify(updated_service), options)
    //                     .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    // }
}













// import { Http } from '@angular/http';
// import { Injectable } from '@angular/core';
// import 'rxjs/add/operator/map';
// import 'rxjs/add/operator/toPromise';

// @Injectable()
// export class SearchService {

//   constructor(private http: Http) {}

//   search(term: string) {
//     return this.http
//       .get(`http://127.0.0.1:8000/api/1/service/21/`)
//       .map((response) => response.json())
//       .toPromise();
//   }
// }




// import { Injectable }              from '@angular/core';
// import { Http, Response }          from '@angular/http';

// import { Observable } from 'rxjs/Observable';

// import 'rxjs/add/operator/catch';
// import 'rxjs/add/operator/map';

// import database? here??

// @Injectable()
// export class HeroService {

//     private servicesUrl = 'api/1/service/';


//     constructor (private http: Http) {}

//     get Services(): Observable<'what?'[xzxzxzxzxzxzxzxz]>{

//         return this.http.get(this.servicesUrl)
//                         .map(this.extractData)
//                         .catch(this.handleError);
//     }

//     private extractData(res: Response) {
//         let body = res.json();
//         return body.data || { };
//     }
//     private handleError (error: Response | any) {
//         // In a real world app, we might use a remote logging infrastructure
//         let errMsg: string;
//         if (error instanceof Response) {
//             const body = error.json() || '';
//             const err = body.error || JSON.stringify(body);
//             errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
//         } else {
//             errMsg = error.message ? error.message : error.toString();
//         }
//         console.error(errMsg);
//         return Observable.throw(errMsg);
//     }
// }











 
// import { DBtest } from './dbtest';
// import { SERVICES } from './mock-db';

// import { Injectable } from '@angular/core';

// @Injectable()
// export class ServicesService {
//     getDBs(): Promise<DBtest[]> {
//         return Promise.resolve(SERVICES);
//     }

//     getDB(id: number): Promise<DBtest> {
//     return this.getDBs()
//                .then(DBs => DBs.find(DB => DB.id === id));
//   }

// }
