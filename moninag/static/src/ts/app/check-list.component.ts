import { Component, OnInit } from '@angular/core';
import { Router }            from '@angular/router';

import { CheckAddComponent } from './check-add.component';
import { ChecksService } from './checks.service';
import { Observable } from 'rxjs/Observable';
import { Check } from './check';

@Component({ 
    selector:'checks-app',
    template:`
            <ul>
                <li *ngFor="let check of checks" (click)="onSelect(check); gotoDetail()" value= {{check.id}> 
                {{check.name}}
                </li>   
            </ul>
            <button (click)="add()"> Add new check </button>
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
        this.checksService.getChecks().subscribe(checks => this.checks = checks["response"]);
                                        
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

    add(): void {
    this.router.navigate(['add']);
    }

}