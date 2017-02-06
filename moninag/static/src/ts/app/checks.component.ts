import { Component, OnInit } from '@angular/core';
import { Plugin } from './plugin';
import { ChecksService } from './checks.service';
import { Observable } from 'rxjs/Observable';

@Component({
    selector: 'checks-app',
    templateUrl: 'static/src/ts/app/checks.component.html',

    providers: [
        ChecksService
    ],
})

export class ChecksComponent implements OnInit{

    constructor(
        private checksService: ChecksService
    ){}

    plugins : Plugin[];

    loadPlugins(){
         this.checksService.getPlugins().subscribe(plugins => this.plugins = plugins);
                                        
    }                                                 
    

    ngOnInit() {
            this.loadPlugins();
            
    }

    checkname = 'Check1';
    portname = 'Port1';

}