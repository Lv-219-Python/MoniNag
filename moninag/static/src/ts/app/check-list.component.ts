import { Component, OnInit } from '@angular/core';
import { Router }            from '@angular/router';

import { ChecksService } from './checks.service';
import { Observable } from 'rxjs/Observable';
import { Check } from './check';

@Component({
    selector:'checks-app',
    template:`
            <ul>
                <li *ngFor="let check of checks" (click)="onSelect(check)" value= {{check.id}} (click)="gotoDetail()"> 
                {{check.name}}
                </li>
            </ul>       
            `,

    providers: [
        ChecksService
    ],
})

export class CheckListComponent  implements OnInit {

    constructor(
        private checksService: ChecksService,
        private router: Router
    ){}

    
    checks : Check[];
    
    selectedCheck : Check;

   
    loadChecks(){
        this.checksService.getChecks().subscribe(checks => this.checks = checks);
                                        
    }     

    ngOnInit() {
        this.loadChecks();
            
    }

    onSelect(check: Check): void {
        this.selectedCheck = check;
    }

    gotoDetail(): void {
    this.router.navigate(['/checks', this.selectedCheck.id]);
  }

}