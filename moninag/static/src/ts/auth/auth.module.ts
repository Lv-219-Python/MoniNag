import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { HttpModule, BaseRequestOptions } from '@angular/http';
import { RouterModule } from '@angular/router';
import { MaterialModule } from '@angular/material';

import { AlertService, AuthenticationService, UserService } from './_services/index';
import { AuthComponent } from './auth.component'
import { MessageComponent} from './message/message.component'
import { LoginComponent } from './login/login.component'
import { RegisterComponent } from './register/register.component'


@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        MaterialModule.forRoot(),
        RouterModule.forRoot([
            {
                path: '',
                redirectTo: '/auth',
                pathMatch: 'full'
            },
            {
                path: 'auth',
                component: LoginComponent
            },
            {
                path: 'auth/register_user',
                component: RegisterComponent
            }
        ])
    ],
    declarations: [
        AuthComponent,
        LoginComponent,
        RegisterComponent,
        MessageComponent
    ],
    providers: [
        AlertService,
        AuthenticationService,
        UserService,
        BaseRequestOptions
    ],
    bootstrap: [
        AuthComponent
    ]
})

export class AuthModule {}
