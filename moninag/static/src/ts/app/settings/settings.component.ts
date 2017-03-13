import { Component } from '@angular/core';

import { SettingsMenuComponent } from './settings-menu.component';

@Component({
    selector: 'settings-app',
    styles: [require('../../../less/styles.less').toString()],
    template: `
        <settings-menu></settings-menu>
    `
})

export class SettingsComponent { }
/*        <md-toolbar>
            <button md-button
                [routerLink]="['settings', {outlets: {'userroute': ['profile']}}]">
                Speakers
            </button>
        </md-toolbar>*/
