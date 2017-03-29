import { Component, OnInit, ViewEncapsulation, ViewChild, TemplateRef } from '@angular/core';
import { DialogPreset, DialogPresetBuilder, Modal, VexModalModule, VEXModalContext, DialogFormModal } from 'angular2-modal/plugins/vex';

import { overlayConfigFactory } from "angular2-modal";
import { Router } from '@angular/router';

import { Contact } from './contact';
import { ContactsService } from './contacts.service';
import { ContactsEmailComponent } from './contacts-email.component';

import { emailValid } from '../validations/patterns';

@Component({
    selector: 'contacts-list',
    template: require('./contacts-list.component.html'),
    styles: [ require('./contacts.less').toString() ],
    providers: [ContactsService],
    encapsulation: ViewEncapsulation.None
})

export class ContactsListComponent implements OnInit {

    contacts: Contact[];
    contact: Contact;
    emailValid = emailValid;
    selectedContact: Contact;

    @ViewChild('emailAdd') public emailAdd: TemplateRef<any>;
    @ViewChild('deleteContact') public deleteContact: TemplateRef<any>;

constructor(
    private contactsService: ContactsService,
    private router: Router,
    public modal: Modal){}

ngOnInit(){
    this.contactsService.getContacts()
                        .subscribe((contacts) => {
                        this.contacts = contacts;
    })}

onSelect(contact: Contact){
    this.selectedContact = contact;
    }

save(){
    this.contactsService.putContact(this.selectedContact)
                        .subscribe(() => this.goBack())
    }

delete(){
    this.contactsService.deleteContact(this.selectedContact.id)
                        .subscribe(() => this.goBack())
    }

goBack(){
    location.reload();
    }

renderModalAdd(){
        return new DialogPresetBuilder<DialogPreset>(this.modal)
            .content(ContactsEmailComponent)
            .isBlocking(false)
            .open()
    }

renderModalDelete(){
        return this.modal.open(this.deleteContact, overlayConfigFactory({ isBlocking: false }, VEXModalContext))
    }

renderModalEdit(){
        return this.modal.open(this.emailAdd, overlayConfigFactory({ isBlocking: false }, VEXModalContext))
    }
}
