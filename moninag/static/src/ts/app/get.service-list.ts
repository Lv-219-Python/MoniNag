import { Component } from '@angular/core';
import { SearchService } from './search.service';


@Component({
    selector: 'get.service-list',
    template: `
        <div class="info" *ngFor="let service of ServicesList">
            <label> {{service.id}} </label> 
            - <label> {{service.name}} </label> 
            - <label> {{service.status}} </label> 
            - <label> {{service.server_id}} </label>
        </div>
    `,
    styles: [`
        label {
          color: #607D8B;
          font-weight: bold;
        }
    `]

})

export class ServiceListComponent {
    ServicesList = SearchService;
}