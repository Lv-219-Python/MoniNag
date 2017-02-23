import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HttpModule, JsonpModule } from '@angular/http';

import { CheckListComponent } from './check-list.component';
import { CheckDetailComponent } from './check-detail.component';
import { CheckUpdateComponent } from './check-update.component';
import { CheckAddComponent } from './check-add.component';
import { ServersComponent } from './servers.component';
import { ServersEditComponent } from './servers/edit-server.component';
import { ServicesComponent } from './services/services.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { ServiceDetailComponent } from './services/service-detail.component';

const APP_ROUTES: Routes = [
    {
        path: '',
        redirectTo: '/profile',
        pathMatch: 'full'
    },
    {
        path: 'profile',
        component: UserProfileComponent
    },
    {
        path: 'servers',
        component: ServersComponent
    },
    {
       path: 'server/:id',
       component: ServersEditComponent
    },
    {
        path: 'services',
        component: ServicesComponent
    },
    {
        path: 'services/:id',
        component: ServiceDetailComponent
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
    },
    {
        path: 'add',
        component: CheckAddComponent
    }
];

@NgModule({
    imports: [
        RouterModule.forRoot(APP_ROUTES),
        HttpModule,
        JsonpModule
    ],
    exports: [ RouterModule ]
})

export class AppRoutingModule { }
