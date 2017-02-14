import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component'
import { AppRoutingModule } from './app-routing.module';
import { CheckListComponent } from './check-list.component';
import { CheckDetailComponent } from './check-detail.component';
import { ServersComponent } from './servers.component';
import { ServicesComponent } from './services.component';
import { ChecksService } from './checks.service';



@NgModule({
    imports: [
        BrowserModule,
        AppRoutingModule
    ],

    declarations: [
        AppComponent,
        CheckListComponent,
        CheckDetailComponent,
        ServersComponent,
        ServicesComponent
    ],
    providers: [
        ChecksService
    ],

    bootstrap: [
        AppComponent
    ]
})

export class AppModule {

}
