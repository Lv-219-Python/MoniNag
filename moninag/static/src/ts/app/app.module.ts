import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule } from '@angular/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component'
import { AppRoutingModule } from './app-routing.module';
import { ChecksComponent } from './checks.component';
import { ServersComponent } from './servers.component';
import { ServersEditComponent } from './servers/edit-server.component';
import { ServersService } from './servers/service';
import { ServerComponent } from './servers/server.component';
import { ServicesComponent } from './services.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { UserProfileService } from './user-profile/user-profile.service';


@NgModule({
    imports: [
        BrowserModule,
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
        ServerComponent,
        ServersEditComponent,
        ServicesComponent,
        UserProfileComponent,
    ],
    providers: [
        UserProfileService,
    ],
    bootstrap: [
        AppComponent,
    ]
})

export class AppModule { }
