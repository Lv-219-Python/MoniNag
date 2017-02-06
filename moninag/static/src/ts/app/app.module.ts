import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component'
import { AppRoutingModule } from './app-routing.module';
import { ChecksComponent } from './checks.component';
import { ServersComponent } from './servers.component';
import { ServicesComponent } from './services.component';
import { DBListComponent }    from './db-list';


import { SearchService } from './search.service';
import { ServiceListComponent } from './get.service-list';

@NgModule({
    imports: [
        BrowserModule,
        AppRoutingModule
    ],
    declarations: [
        AppComponent,
        ChecksComponent,
        ServersComponent,
        ServicesComponent,
        DBListComponent,
        ServiceListComponent,
    ],
    providers: [
        SearchService
    ],
    bootstrap: [
        AppComponent
    ]
})

export class AppModule {

}
