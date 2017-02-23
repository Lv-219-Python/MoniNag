import { NgModule } from '@angular/core';
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
import { ServersEditComponent } from './servers/edit-server.component';
import { ServersService } from './servers/service';
import { ServerComponent } from './servers/server.component';

import { ServicesComponent } from './services/services.component';
import { ServicesService } from './services/services.service';
import { ServiceDetailComponent } from './services/service-detail.component';

import { UserProfileComponent } from './user-profile/user-profile.component';
import { UserProfileService } from './user-profile/user-profile.service';

@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        AppRoutingModule,
        JsonpModule,
        ReactiveFormsModule
    ],

    declarations: [
        AppComponent,
        CheckListComponent,
        CheckDetailComponent,
        CheckUpdateComponent,
        CheckAddComponent,
        ServersComponent,
        ServerComponent,
        ServersEditComponent,
        ServicesComponent,
        ServiceDetailComponent,
        UserProfileComponent
    ],
    providers: [
        ChecksService,
        ServicesService,
        ServersService,
        UserProfileService,
    ],

    bootstrap: [
        AppComponent,
    ]
})

export class AppModule { }
