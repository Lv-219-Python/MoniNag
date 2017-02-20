import { NgModule } from '@angular/core';
import { Routes, RouterModule, Router } from '@angular/router';

import { ChecksComponent } from './checks.component';
import { ServersComponent } from './servers.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { ServicesComponent } from './services.component';
import { ContactsListComponent} from './contacts/list.component';
import { ContactsEditComponent } from './contacts/edit.component';


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
    },

    {
        path: 'contacts',
        component: ContactsListComponent
    },
    { 
        path: 'contact/:id', 
        component: ContactsEditComponent 
    }
]

@NgModule({
    imports: [RouterModule.forRoot(APP_ROUTES)],
    exports: [RouterModule]

})

export class AppRoutingModule { }
