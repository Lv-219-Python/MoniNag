import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { FlexLayoutModule } from "@angular/flex-layout";

import { SettingsPluginsComponent } from './plugins.component';
import { SettingsHelpComponent } from './settings-help.component';
import { UserProfileComponent } from '../user-profile/user-profile.component';

@Component({
    selector: 'settings-menu',
    styles: [require('./settings.less').toString()],
    template: require('./settings-menu.component.html'),
})

export class SettingsMenuComponent { }
