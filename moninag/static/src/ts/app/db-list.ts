import { Component }   from '@angular/core';
import { SERVICES }      from './mock-db';


@Component({
    selector: 'db-list',
    template: `
        <div class="info" *ngFor="let dbase of dbases">
            <label> {{dbase.id}} </label> - <label> {{dbase.name}} </label> - {{dbase.status}}
        </div>

    `,
    styles: [`
        label {
          color: #607D8B;
          font-weight: bold;
        }
        .StatusOk {
            color: green;
        }
        .StatusNotOk {
            color: red;
        }
        .info {
            margin-left: auto;
            margin-right: auto;
            width: 6em
        }
    `]
})

export class DBListComponent {
    dbases = SERVICES;
}