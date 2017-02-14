import { Component } from '@angular/core';


@Component({
    selector: 'moninag-app',
    styles: [require('../../less/styles.less').toString()],
    template: `
        <h1>{{title}}</h1>
        <a routerLink="/servers">Servers</a>
        <a routerLink="/services">Services</a>
        <a routerLink="/checks">Checks</a>
        <router-outlet></router-outlet>
    `
})

export class AppComponent {
    title = 'Moninag';
}
