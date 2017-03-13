import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';


@Component({
    selector: 'side-nav-settings',
    template: require('./side-nav.component.html'),
    styles: [require('./settings.less').toString()],
})

export class SideNavSettingsComponent { }