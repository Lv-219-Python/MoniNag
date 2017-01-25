import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component'
import { ChecksComponent } from './checks.component';
import { ServersComponent } from './servers.component';
import { ServicesComponent } from './services.component';


@NgModule({
    imports: [
        BrowserModule,
        RouterModule.forRoot([
            {
                path: '',
                redirectTo: '/servers',
                pathMatch: 'full'
            },
            {
                path: 'servers',
                component: ServersComponent
            },

            {
                path: 'services',
                component: ServicesComponent
            },

            {
                path: 'checks',
                component: ChecksComponent
            }
        ])
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
