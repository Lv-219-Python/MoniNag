import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Location } from '@angular/common';


import { Contact } from './model';
import { ContactsService } from './service';

import 'rxjs/add/operator/switchMap';

@Component({
    selector: 'contacts-edit',
    template: `
    <div *ngIf="contact"><div>
    <h5>First Name:</h5>
    <input [(ngModel)]="contact.first_name" placeholder="{{contact.first_name}}" />
    <h5>Second Name:</h5>
    <input [(ngModel)]="contact.second_name" placeholder="{{contact.second_name}}" />
    <h5>Email:</h5>
    <input [(ngModel)]="contact.email" placeholder="{{contact.email}}" />
    <div>
    <br>
    <button (click)="goBack()">Back</button>
    <button (click)="save()">Save</button>
    <button (click)="delete()">x</button>
    </div>
    `,
    providers: [
        ContactsService
    ],
})

export class ContactsEditComponent {

    constructor(
        private contactsService: ContactsService,
        private route: ActivatedRoute,
        private router: Router,
        private location: Location
    ){}

    contact : Contact[];                                 
    
    ngOnInit(){
        this.route.params
            .switchMap((params: Params) => this.contactsService.getContact(+params['id']))
            .subscribe(contact => this.contact = contact['response']);
    }
    
    save(){
        this.contactsService.putContact(this.contact)
        .subscribe(() => this.goBack())
    }

    delete(){
        this.contactsService.deleteContact(this.contact['id'])
        .subscribe(() => this.goBack())
    }

    goBack(){
        this.location.back();
    }    
} 
                                          