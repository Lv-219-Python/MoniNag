import { Component, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Location } from '@angular/common';

import { ContactsService } from './contacts.service';
import { Contact } from './contact';


@Component({
    selector: 'contact-add',
    template: require('./contacts-email.component.html'),
    providers: [ContactsService]
})

export class ContactsEmailComponent {

  emailForm: FormGroup;
  contact: Contact[];
  @Output() contactAdded = new EventEmitter();

    constructor(private contactsService: ContactsService,
                        fb: FormBuilder,
                      private location: Location) {
        this.emailForm = fb.group({
            'first_name': '',
            'second_name': '',
            'email':[null, [Validators.required,
                            Validators.pattern("[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,64}")]
        ]})
    }

    submitForm(contact: any) {
        this.contactsService.postContact(contact)
                            .subscribe((contact) => {
                             this.contact = contact;
        })
    }

    goBack(){
      location.reload();
    }
}
