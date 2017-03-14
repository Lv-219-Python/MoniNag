import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { Contact } from './contact';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';


@Injectable()
export class ContactsService {

    contacts : Contact[];

    constructor(private http:Http) {}

    private contactsUrl = '/api/1/contact/';

    getContacts(): Observable<Contact[]> {
        return this.http.get(this.contactsUrl)
           .map((response: Response) => response.json()['response'])
           .catch((error:any) => Observable.throw(error.json() || 'Server Error'))
    }

    getContact(id: number): Observable<Contact> {
        const url = `${this.contactsUrl}${id}`;
        return this.http.get(url)
              .map((response:Response) => response.json())
              .catch((error:any) => Observable.throw(error.json()|| 'Server error'));
    }

    postContact(contact: any): Observable<Contact[]> {
        let bodyString = JSON.stringify(contact);
        let headers = new Headers({ 'Content-Type': 'application/json', 'Accept': 'application/json'});
        let options = new RequestOptions({ headers: headers });

        return this.http.post(this.contactsUrl, contact, options)
                        .map((response: Response) => response.json()['response'])
                        .catch((error:any) => Observable.throw(error.json() || 'Server Error'));
    }

    putContact(contact: any): Observable<Contact[]> {
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let options = new RequestOptions({ headers: headers });
        let edited_contact = JSON.stringify({
            first_name: contact.first_name,
            second_name: contact.second_name,
            email: contact.email,
        });

        return this.http.put(`${this.contactsUrl}${contact['id']}/`, edited_contact, options)
                        .map((response: Response) => response.json())
                        .catch((error:any) => Observable.throw(error.json()['error'] || 'Server Error'));
    }

    deleteContact(id:number): Observable<Contact[]> {
        return this.http.delete(`${this.contactsUrl}${id}`)
                        .map((response: Response) => response.json())
                        .catch((error:any) => Observable.throw(error.json() || 'Server error'));
    }
}
