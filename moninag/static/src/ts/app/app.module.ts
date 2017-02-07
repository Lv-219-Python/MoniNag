import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component'
import { AppRoutingModule } from './app-routing.module';
import { ChecksComponent } from './checks.component';
import { ServersComponent } from './servers.component';
import { ServicesComponent } from './services.component';



@NgModule({
    imports: [
        BrowserModule,
        AppRoutingModule
    ],
    declarations: [
        AppComponent,
        ChecksComponent,
        ServersComponent,
        ServicesComponent
    ],
    providers: [
    ],
    bootstrap: [
        AppComponent
    ]
})

export class AppModule {

}
