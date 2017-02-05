import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ChecksComponent } from './checks.component';
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
        component: ChecksComponent
    }
]

@NgModule({
  imports: [ RouterModule.forRoot(APP_ROUTES) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
