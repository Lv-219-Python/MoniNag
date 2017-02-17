import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';

import { AppComponent } from './app.component'
import { AppRoutingModule } from './app-routing.module';
import { CheckListComponent } from './check-list.component';
import { CheckDetailComponent } from './check-detail.component';
import { CheckUpdateComponent } from './check-update.component';
import { ServersComponent } from './servers.component';
import { ServicesComponent } from './services.component';
import { ChecksService } from './checks.service';



@NgModule({
    imports: [
        BrowserModule,
        AppRoutingModule,
        FormsModule
    ],

    declarations: [
        AppComponent,
        CheckListComponent,
        CheckDetailComponent,
        CheckUpdateComponent,
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
