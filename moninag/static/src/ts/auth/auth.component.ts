import { Component } from '@angular/core';


@Component({
    selector: 'auth-app',
    styles: [require('../../less/auth/auth.less').toString()],
    template: `
        <message></message>
        <div id="auth-app" class="flex-container" fxLayout="row" fxLayoutAlign="center center">
            <router-outlet></router-outlet>
        </div>

    `
})

export class AuthComponent { }
