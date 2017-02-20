import { NgModule, OnInit } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component'
import { AppRoutingModule } from './app-routing.module';
import { ChecksComponent } from './checks.component';
import { ServersComponent } from './servers.component';
import { ServicesComponent } from './services.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { UserProfileService } from './user-profile/user-profile.service';
import { ContactsListComponent } from './contacts/list.component';
import { ContactsEditComponent } from './contacts/edit.component';
import { ContactsEmailComponent } from './contacts/email.component';


@NgModule({
    imports: [
        BrowserModule,
        HttpModule,
        AppRoutingModule,
        BrowserModule,
        FormsModule,
        HttpModule,
        ReactiveFormsModule,

    ],
    declarations: [
        AppComponent,
        ChecksComponent,
        ServersComponent,
        ServicesComponent,
        UserProfileComponent,
        ContactsListComponent,
        ContactsEditComponent,
        ContactsEmailComponent,
    ],
    providers: [
        UserProfileService,
    ],
    bootstrap: [
        AppComponent,
    ]
})

export class AppModule { }
