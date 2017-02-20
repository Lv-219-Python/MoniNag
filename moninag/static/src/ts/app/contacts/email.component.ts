import { Component } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ContactsService } from './service';
import { Contact } from './model';


@Component({
    selector: 'email-add',
    template: `
    <div>
    <form [formGroup]="emailForm" (ngSubmit)="submitForm(emailForm.value)">
      <div class="form-group">
        <input class="form-control" type="text" placeholder="First Name" [formControl]="emailForm.controls['first_name']">
      </div>
      <div class="form-group">
        <input class="form-control" type="text" placeholder="Second Name" [formControl]="emailForm.controls['second_name']">
      </div>
      <div class="form-group" [ngClass]="{'has-error':!emailForm.controls['email'].valid && emailForm.controls['email'].touched}">
        <input class="form-control" type="text" placeholder="example@email.com" [formControl]="emailForm.controls['email']">
        <div *ngIf="emailForm.controls['email'].hasError('required') && emailForm.controls['email'].touched" class="alert alert-danger">Please, enter valid email.</div>
      </div>
      <div class="form-group">
          <button class="btn btn-primary" [disabled]="!emailForm.valid">Submit</button>
     </div>
    </form>
  </div>
  `,
    providers: [ContactsService]
})

export class ContactsEmailComponent {

  emailForm: FormGroup;
  contacts: Contact[];

    constructor(private contactsService: ContactsService,
                        fb: FormBuilder) {
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
                this.contacts = contact;
                  })
            }
    }
    