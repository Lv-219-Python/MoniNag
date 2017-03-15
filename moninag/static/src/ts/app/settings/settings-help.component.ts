import { Component } from '@angular/core';


@Component({
    selector: 'settings-help-app',
    styles: [require('../../../less/styles.less').toString()],
    template: `
        <label>If you have any questions, please contact us at:</label>
        
        <a class="flex-container" fxLayout="row" fxLayoutAlign=" center" 
        href="mailto:moninaginfo@gmail.com">
            <md-icon>help</md-icon>
            <span> moninaginfo@gmail.com</span>
        </a>
        
    `
})

export class SettingsHelpComponent { }
