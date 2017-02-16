import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component'
import { AppRoutingModule } from './app-routing.module';
import { ChecksComponent } from './checks.component';
import { ServersComponent } from './servers.component';
import { ServicesComponent } from './services.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { UserProfileService } from './user-profile/user-profile.service';

import { ServicesService } from './services.service';
import { HttpModule, JsonpModule } from '@angular/http';
import { FormsModule } from '@angular/forms';
import { ServiceDetailComponent } from './service-detail.component';
@NgModule({
    imports: [
        BrowserModule,
        AppRoutingModule,
        HttpModule,
        FormsModule,
        JsonpModule
    ],
    declarations: [
        AppComponent,
        ChecksComponent,
        ServersComponent,
        ServicesComponent,
        UserProfileComponent,
        ServiceDetailComponent
    ],
    providers: [
        UserProfileService,
        ServicesService,
    ],
    bootstrap: [
        AppComponent,
    ]
})

export class AppModule { }
