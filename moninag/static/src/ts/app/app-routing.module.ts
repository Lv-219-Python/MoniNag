import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CheckAddComponent } from './checks/check-add.component';
import { CheckDetailComponent } from './checks/check-detail.component';
import { CheckListComponent } from './checks/check-list.component';
import { CheckUpdateComponent } from './checks/check-update.component';
import { CheckDeleteComponent } from './checks/check-delete.component';

import { ContactsListComponent} from './contacts/contacts-list.component';
import { ContactsEmailComponent } from './contacts/contacts-email.component';

import { ServersComponent } from './servers/servers.component';
import { ServerAddComponent } from './servers/server-add.component';
import { ServerEditComponent } from './servers/server-edit.component';
import { ServerDetailComponent } from './servers/server-detail.component';
import { ServerDeleteComponent } from './servers/server-delete.component'

import { ServiceAddComponent } from './services/service-add.component';
import { ServicesComponent } from './services/services.component';
import { ServiceDeleteComponent } from './services/service-delete.component'
import { ServiceDetailComponent } from './services/service-detail.component';
import { ServiceUpdateComponent } from './services/service-update.component'

import { SettingsComponent } from './settings/settings.component';
import { SettingsMenuComponent } from './settings/settings-menu.component';

import { UserProfileComponent } from './user-profile/user-profile.component';

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
        path: 'server/:id',
        component: ServerDetailComponent
    },
    {
        path: 'server/edit/:id',
        component: ServerEditComponent
    },
    {
        path: 'server/delete/:id',
        component: ServerDeleteComponent
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
        path: 'service/delete/:id',
        component: ServiceDeleteComponent,
    },
    {
        path: 'settings',
        component: SettingsComponent,
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
        path: 'checks/delete/:id',
        component: CheckDeleteComponent
    },
    {
        path: 'add',
        component: CheckAddComponent
    },
    {
        path: 'contacts',
        component: ContactsListComponent
    },
    {
        path: 'contact-add',
        component: ContactsEmailComponent
    },
    {
        path: 'server-add',
        component: ServerAddComponent
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
