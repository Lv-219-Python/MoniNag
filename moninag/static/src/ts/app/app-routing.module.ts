import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ChecksComponent } from './checks.component';
import { ServersComponent } from './servers.component';
import { ServersEditComponent } from './servers/edit-server.component';
import { ServicesComponent } from './services.component';
import { UserProfileComponent } from './user-profile/user-profile.component';


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
        path: 'checks',
        component: ChecksComponent
    }
];

@NgModule({
    imports: [RouterModule.forRoot(APP_ROUTES)],
    exports: [RouterModule]
})

export class AppRoutingModule { }
