import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component'
import { AppRoutingModule } from './app-routing.module';
import { ChecksComponent } from './checks.component';
import { ServersComponent } from './servers.component';
import { ServicesComponent } from './services.component';

import { ServicesService } from './services.service';
import { HttpModule, JsonpModule } from '@angular/http';



@NgModule({
    imports: [
        BrowserModule,
        AppRoutingModule,
        HttpModule,
        JsonpModule
    ],
    declarations: [
        AppComponent,
        ChecksComponent,
        ServersComponent,
        ServicesComponent,
    ],
    providers: [
        ServicesService,
    ],
    bootstrap: [
        AppComponent
    ]
})

export class AppModule {

}
