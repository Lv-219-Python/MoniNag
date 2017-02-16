import { Component, Input } from '@angular/core';
import { Service } from './services';

@Component({
  selector: 'services-detail',
  template: `
    <div *ngIf="service">
        <h3>todo: details on %id url</h3>
        <div>
            <label>name: </label>{{service.name}}
        </div>

        <div>
            <label>status: </label>{{service.status}}
        </div>

        <div>
            <label>id: </label>{{service.id}}
        </div>

        <div>
            <label>server id: </label>{{service.server_id}}
        </div>
    </div>
  `
})
export class ServiceDetailComponent {
  @Input() service: Service;
}

