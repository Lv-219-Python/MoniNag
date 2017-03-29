import { Component, Output } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Location } from '@angular/common';

import { ContactsService } from './contacts.service';
import { Contact } from './contact';

import { emailValid } from '../validations/patterns';

@Component({
    selector: 'contact-add',
    template: require('./contacts-email.component.html'),
    providers: [ContactsService]
})

export class ContactsEmailComponent {

    emailForm: FormGroup;
    contact: Contact[];

    constructor(private contactsService: ContactsService,
                        fb: FormBuilder,
                      private location: Location) {
    this.emailForm = fb.group({
        'first_name': [null, Validators.required],
        'second_name': [null, Validators.required],
        'email':[null, [Validators.required,
                        Validators.pattern(emailValid)]]})
    }

    submitForm(contact: any) {
        this.contactsService.postContact(contact)
                            .subscribe((contact) => {
                             this.contact = contact;})
    }

    goBack(){
        location.reload()
    }
}
