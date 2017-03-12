import { BrowserModule } from '@angular/platform-browser';
import { FlexLayoutModule } from "@angular/flex-layout";
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule, JsonpModule } from '@angular/http';
import { NgModule } from '@angular/core';
import { MaterialModule } from '@angular/material';

import { AppComponent } from './app.component'
import { AppRoutingModule } from './app-routing.module';
import { AppHeaderComponent } from './app-header/app-header.component';
import { MainNavComponent } from './navs/main-nav/main-nav.component';
import { SideNavComponent } from './navs/side-nav/side-nav.component';

import { CheckAddComponent } from './checks/check-add.component';
import { CheckDetailComponent } from './checks/check-detail.component';
import { CheckListComponent } from './checks/check-list.component';
import { CheckUpdateComponent } from './checks/check-update.component';
import { ChecksService } from './checks/checks.service';

import { VexModalModule } from 'angular2-modal/plugins/vex';
import { ModalModule } from 'angular2-modal';

import { ServerAddComponent } from './servers/server-add.component';
import { ServersComponent } from './servers/servers.component';
import { ServerEditComponent } from './servers/server-edit.component';
import { ServerDetailComponent } from './servers/server-detail.component';
import { ServersService } from './servers/service';

import { ServiceAddComponent } from './services/service-add.component';
import { ServiceDetailComponent } from './services/service-detail.component';
import { ServicesComponent } from './services/services.component';
import { ServicesService } from './services/services.service';
import { ServiceUpdateComponent } from './services/service-update.component'

import { UserProfileComponent } from './user-profile/user-profile.component';
import { UserProfileService } from './user-profile/user-profile.service';


@NgModule({
    imports: [
        AppRoutingModule,
        BrowserModule,
        FlexLayoutModule.forRoot(),
        FormsModule,
        HttpModule,
        JsonpModule,
        MaterialModule.forRoot(),
        ModalModule.forRoot(),
        ReactiveFormsModule,
        VexModalModule
    ],

    declarations: [
        AppComponent,
        AppHeaderComponent,
        CheckAddComponent,
        CheckDetailComponent,
        CheckListComponent,
        CheckUpdateComponent,
        MainNavComponent,
        ServerAddComponent,
        ServerDetailComponent,
        ServersComponent,
        ServerEditComponent,
        ServiceAddComponent,
        ServiceDetailComponent,
        ServicesComponent,
        ServiceUpdateComponent,
        SideNavComponent,
        UserProfileComponent,
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
