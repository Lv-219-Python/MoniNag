import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FlexLayoutModule } from "@angular/flex-layout";
import { UserProfileComponent } from '../user-profile/user-profile.component';

@Component({
    selector: 'settings-menu',
    template: require('./settings-menu.component.html'),
    styles: [require('./settings.less').toString()],
})

export class SettingsMenuComponent { }