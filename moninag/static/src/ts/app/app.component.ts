import { Component } from '@angular/core';


@Component({
    selector: 'moninag-app',
    styles: [
                require('../../less/styles.less').toString()
            ],

    template: `
        <app-header></app-header>
        <side-nav id="side-navigation"></side-nav>
        <div class="content">
            <router-outlet></router-outlet>
        </div>
    `
})

export class AppComponent { }
