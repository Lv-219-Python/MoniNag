import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { HttpModule, BaseRequestOptions, XSRFStrategy, CookieXSRFStrategy } from '@angular/http';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component'
import { ChecksComponent } from './checks.component';
import { ServersComponent } from './servers.component';
import { ServicesComponent } from './services.component';

import { AlertService, AuthenticationService, UserService } from './registration/_services/index';
import { RegistrationAppComponent } from './registration/registration.component'
import { MessageComponent} from './registration/message/message.component'
import { LoginComponent } from './registration/login/login.component'
import { RegisterComponent } from './registration/register/register.component'


@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
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
            },

            {
                path: 'accounts',
                component: RegistrationAppComponent
            },

            {
                path: 'accounts/register_user',
                component: RegisterComponent
            }
        ])
    ],
    declarations: [
        AppComponent,
        ChecksComponent,
        ServersComponent,
        ServicesComponent,
        RegistrationAppComponent,
        LoginComponent,
        RegisterComponent,
        MessageComponent
    ],
    providers: [
        AlertService,
        AuthenticationService,
        UserService,
        BaseRequestOptions,
        {
            provide: XSRFStrategy,
            useValue: new CookieXSRFStrategy('csrftoken', 'X-CSRFToken')
        }
    ],
    bootstrap: [
        AppComponent
    ]
})

export class AppModule {

}
