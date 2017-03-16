import { Component } from '@angular/core';

import { SettingsService } from './settings.service';


@Component({
    selector: 'plugins-app',
    template: require('./plugins.component.html'),
    providers: [SettingsService]
})


export class SettingsPluginsComponent {

    constructor(
        private settingsService: SettingsService,
    ) { }

    plugins: Plugin[];

    loadPlugins() {
        this.settingsService.getPlugins()
            .subscribe(plugins => this.plugins = plugins['response']);
    }

    ngOnInit(): void {
        this.loadPlugins();
    }
}
