import { Component } from '@angular/core';

import { SideNavSettingsComponent } from './side-nav.component';

@Component({
    selector: 'settings-app',
    styles: [require('../../../less/styles.less').toString()],
    template: `
        <side-nav-settings></side-nav-settings>
    `
})

export class SettingsComponent { }
/*        <md-toolbar>
            <button md-button
                [routerLink]="['settings', {outlets: {'userroute': ['profile']}}]">
                Speakers
            </button>
        </md-toolbar>*/
