import { Component } from '@angular/core';


@Component({
    selector: 'moninag-app',
    styles: [require('../../less/styles.less').toString()],
    template: `
        <app-header></app-header>
        <main-nav></main-nav>
        <router-outlet></router-outlet>
    `
})

export class AppComponent { }
