import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CheckAddComponent } from './checks/check-add.component';
import { CheckDetailComponent } from './checks/check-detail.component';
import { CheckListComponent } from './checks/check-list.component';
import { CheckUpdateComponent } from './checks/check-update.component';

import { ServersComponent } from './servers/servers.component';
import { ServerComponent } from './servers/server.component';
import { ServerEditComponent } from './servers/edit-server.component';
import { ServerDetailComponent } from './servers/server-detail.component';

import { ServiceAddComponent } from './services/service-add.component';
import { ServicesComponent } from './services/services.component';
import { ServiceDetailComponent } from './services/service-detail.component';
import { ServiceUpdateComponent } from './services/service-update.component'

import { UserProfileComponent } from './user-profile/user-profile.component';

const APP_ROUTES: Routes = [
    {
        path: '',
        redirectTo: '/servers',
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
        component: ServerDetailComponent
    },
    {
        path: 'server/edit/:id',
        component: ServerEditComponent
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
        path: 'service/update/:id',
        component: ServiceUpdateComponent,
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
    },
    {
        path: 'server-add',
        component: ServerComponent
    },
    {
        path: 'service-add',
        component: ServiceAddComponent
    },
];

@NgModule({
    imports: [
        RouterModule.forRoot(APP_ROUTES, { useHash: true }),
    ],
    exports: [RouterModule]
})

export class AppRoutingModule { }
