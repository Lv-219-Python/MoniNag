import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule, JsonpModule } from '@angular/http';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component'
import { AppRoutingModule } from './app-routing.module';

import { CheckAddComponent } from './check-add.component';
import { CheckDetailComponent } from './check-detail.component';
import { CheckListComponent } from './check-list.component';
import { CheckUpdateComponent } from './check-update.component';
import { ChecksService } from './checks.service';

import { ServerComponent } from './servers/server.component';
import { ServersComponent } from './servers.component';
import { ServersEditComponent } from './servers/edit-server.component';
import { ServersService } from './servers/service';

import { ServiceAddComponent } from './services/service-add.component';
import { ServiceDetailComponent } from './services/service-detail.component';
import { ServicesComponent } from './services/services.component';
import { ServicesService } from './services/services.service';

import { UserProfileComponent } from './user-profile/user-profile.component';
import { UserProfileService } from './user-profile/user-profile.service';

@NgModule({
    imports: [
        AppRoutingModule,
        BrowserModule,
        FormsModule,
        HttpModule,
        JsonpModule,
        ReactiveFormsModule
    ],

    declarations: [
        AppComponent,
        CheckAddComponent,
        CheckDetailComponent,
        CheckListComponent,
        CheckUpdateComponent,
        ServerComponent,
        ServersComponent,
        ServersEditComponent,
        ServiceAddComponent,
        ServiceDetailComponent,
        ServicesComponent,
        UserProfileComponent
    ],
    providers: [
        ChecksService,
        ServersService,
        ServicesService,
        UserProfileService,
    ],

    bootstrap: [
        AppComponent,
    ]
})

export class AppModule { }
