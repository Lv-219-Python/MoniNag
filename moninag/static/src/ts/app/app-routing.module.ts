import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HttpModule, JsonpModule } from '@angular/http';

import { CheckListComponent } from './check-list.component';
import { CheckDetailComponent } from './check-detail.component';
import { CheckUpdateComponent } from './check-update.component';
import { ServersComponent } from './servers.component';
import { ServicesComponent } from './services.component';


const APP_ROUTES: Routes = [
    {
        path: '',
        redirectTo: '/servers',
        pathMatch: 'full'
    },
    {
        path: 'servers',
        component: ServersComponent
    },
    {
        path: 'services',
        component: ServicesComponent
    },
    {
        path: 'checks',
        component: CheckListComponent
    },
    { 
        path: 'checks/:id', 
        component: CheckDetailComponent 
    },
    { 
        path: 'checks/update/:id', 
        component: CheckUpdateComponent 
    }
]

@NgModule({
    imports: [ 
        RouterModule.forRoot(APP_ROUTES),
        HttpModule,
        JsonpModule
    ],
    exports: [ RouterModule ]
})


export class AppRoutingModule {}
