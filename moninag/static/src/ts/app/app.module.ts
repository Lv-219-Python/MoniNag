import { NgModule, OnInit } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule, JsonpModule } from '@angular/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component'
import { AppRoutingModule } from './app-routing.module';
import { CheckListComponent } from './check-list.component';
import { CheckDetailComponent } from './check-detail.component';
import { CheckUpdateComponent } from './check-update.component';
import { CheckAddComponent } from './check-add.component';
import { ChecksService } from './checks.service';
import { ServersComponent } from './servers.component';
import { ServiceDetailComponent } from './service-detail.component';
import { ServicesComponent } from './services.component';
import { ServicesService } from './services.service';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { UserProfileService } from './user-profile/user-profile.service';
import { ContactsListComponent } from './contacts/list.component';
import { ContactsEditComponent } from './contacts/edit.component';
import { ContactsEmailComponent } from './contacts/email.component';


@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        AppRoutingModule,
        JsonpModule,                        
        ReactiveFormsModule,
    ],

    declarations: [
        AppComponent,
        CheckListComponent,
        CheckDetailComponent,
        CheckUpdateComponent,
        CheckAddComponent,
        ServersComponent,
        ServicesComponent,
        UserProfileComponent,
        ServiceDetailComponent,
        ContactsListComponent,
        ContactsEditComponent,
        ContactsEmailComponent,
    ],
    providers: [
        ChecksService,
        UserProfileService,
        ServicesService,
    ],

    bootstrap: [
        AppComponent,
    ]
})

export class AppModule { }
