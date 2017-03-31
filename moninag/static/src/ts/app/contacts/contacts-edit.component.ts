import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Location } from '@angular/common';

import { Contact } from './contact';
import { ContactsService } from './contacts.service';

import 'rxjs/add/operator/switchMap';

@Component({
    selector: 'contacts-edit',
    template: require('./contacts-edit.component.html'),
    providers: [ContactsService],
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
                            .subscribe(() => this.gotoContacts())
    }

    gotoContacts() {
        location.href = '/#/contacts/';
    }
}
