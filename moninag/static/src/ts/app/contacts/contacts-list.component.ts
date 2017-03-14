import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { DialogPreset, DialogPresetBuilder, Modal, VexModalModule } from 'angular2-modal/plugins/vex';

import { overlayConfigFactory } from "angular2-modal";
import { Router } from '@angular/router';

import { Contact } from './contact';
import { ContactsService } from './contacts.service';
import { ContactsEmailComponent } from './contacts-email.component';

@Component({
    selector: 'contacts-list',
    template: require('./contacts-list.component.html'),
    providers: [ContactsService],
    encapsulation: ViewEncapsulation.None
})

export class ContactsListComponent implements OnInit {

    contacts: Contact[];
    selectedContact: Contact;
    contact: Contact;

constructor(
    private contactsService: ContactsService,
    private router: Router,
    public modal: Modal ){
  }

ngOnInit(){
    this.contactsService.getContacts()
                        .subscribe((contacts) => {
                        this.contacts = contacts;
})}

onSelect(contact: Contact){
    this.selectedContact = contact;
    }

handleContactAdded(contact: Contact){
    this.contacts.push(contact);
    }

edit(){
  this.router.navigate(['contact', this.selectedContact.id]);
}

delete(){
    this.contactsService.deleteContact(this.selectedContact.id)
    .subscribe(() => (this.contact));
    this.contacts.splice(this.contacts.indexOf(this.selectedContact),1);
    }

renderModalAdd(){
        return new DialogPresetBuilder<DialogPreset>(this.modal)
            .content(ContactsEmailComponent)
            .isBlocking(false)
            .open();
    }
}
