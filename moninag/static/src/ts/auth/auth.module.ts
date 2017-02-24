import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpModule, BaseRequestOptions } from '@angular/http';
import { RouterModule } from '@angular/router';
import { MaterialModule } from '@angular/material';
import { FlexLayoutModule } from "@angular/flex-layout";

import { AlertService, AuthenticationService, UserService, ResetPasswordService } from './_services/index';
import { AuthComponent } from './auth.component'
import { ConfirmPasswordResetComponent } from './reset_password/confirm_password_reset.component'
import { EqualValidator } from './reset_password/equal-validator.directive';
import { LoginComponent } from './login/login.component'
import { MessageComponent } from './message/message.component'
import { RegisterComponent } from './register/register.component'
import { ResetPasswordComponent } from './reset_password/reset_password.component'


@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        MaterialModule.forRoot(),
        FlexLayoutModule.forRoot(),
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
            },
            {
                path: 'auth/reset_password',
                component: ResetPasswordComponent
            },
            {
                path: 'auth/confirm_password_reset/:uidb64/:token',
                component: ConfirmPasswordResetComponent
            }
        ])
    ],
    declarations: [
        AuthComponent,
        LoginComponent,
        RegisterComponent,
        MessageComponent,
        ResetPasswordComponent,
        ConfirmPasswordResetComponent,
        EqualValidator
    ],
    providers: [
        AlertService,
        AuthenticationService,
        UserService,
        ResetPasswordService,
        BaseRequestOptions
    ],
    bootstrap: [
        AuthComponent
    ]
})

export class AuthModule { }
