import { Component, OnInit } from '@angular/core';
import { ContactsService } from './service';
import { Router } from '@angular/router';
import { Contact } from './model';


@Component({
    selector: 'contacts-list',
    template: `
    <div class="table-responsive">
   <ul style="list-style-type:none; padding:0">          
   <table class="table">
    <thead>
      <tr>
        <th>#</th>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><li *ngFor="let contact of contacts; let i=index">{{i + 1}}</li></td>
        <td><li *ngFor="let contact of contacts" (click)="onSelect(contact)" (click)="gotoEdit()" value={{contact.id}}>{{ contact.first_name }}</li></td>
        <td><li *ngFor="let contact of contacts" (click)="onSelect(contact)" (click)="gotoEdit()" value={{contact.id}}>{{ contact.second_name }}</li></td>
        <td><li *ngFor="let contact of contacts" (click)="onSelect(contact)" (click)="gotoEdit()" value={{contact.id}}>{{ contact.email }}</li></td>
      </tr>
    </tbody>
  </table>
  </ul>
</div>
<email-add></email-add>
`,
    providers: [ContactsService]
})

export class ContactsListComponent implements OnInit {

  contacts: Contact[];
  selectedContact: Contact;
 
  constructor(
    private contactsService: ContactsService,
    private router: Router ){
  }

  ngOnInit(){
    this.contactsService.getContacts()
                        .subscribe((contacts) => { 
                         this.contacts = contacts
})}
  onSelect(contact: Contact){
         this.selectedContact = contact;
     }
 
  gotoEdit(){
     this.router.navigate(['contact', this.selectedContact.id]);
   }
}
