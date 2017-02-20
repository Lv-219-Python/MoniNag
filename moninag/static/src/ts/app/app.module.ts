import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
<<<<<<< HEAD
=======
import { FormsModule }   from '@angular/forms';
import { HttpModule } from '@angular/http';

>>>>>>> f61bfa1383d64fceb755122c1a48ab95ad864b26
import { AppComponent } from './app.component'
import { AppRoutingModule } from './app-routing.module';
import { CheckListComponent } from './check-list.component';
import { CheckDetailComponent } from './check-detail.component';
import { CheckUpdateComponent } from './check-update.component';
import { CheckAddComponent } from './check-add.component';
import { ServersComponent } from './servers.component';
<<<<<<< HEAD
import { ServicesComponent } from './services/services.component';
=======
import { ServicesComponent } from './services.component';
import { ChecksService } from './checks.service';
>>>>>>> f61bfa1383d64fceb755122c1a48ab95ad864b26
import { UserProfileComponent } from './user-profile/user-profile.component';
import { UserProfileService } from './user-profile/user-profile.service';

import { ServicesService } from './services/services.service';
import { HttpModule, JsonpModule } from '@angular/http';
import { FormsModule } from '@angular/forms';
import { ServiceDetailComponent } from './services/service-detail.component';
@NgModule({
    imports: [
        BrowserModule,
<<<<<<< HEAD
=======
        FormsModule,
        HttpModule,
>>>>>>> f61bfa1383d64fceb755122c1a48ab95ad864b26
        AppRoutingModule,
        HttpModule,
        FormsModule,
        JsonpModule
    ],

    declarations: [
        AppComponent,
        CheckListComponent,
        CheckDetailComponent,
        CheckUpdateComponent,
        CheckAddComponent,
        ServersComponent,
        ServicesComponent,
        UserProfileComponent,
        ServiceDetailComponent
    ],
    providers: [
        ChecksService,
        UserProfileService,
        ServicesService,
    ],

    bootstrap: [
        AppComponent,
    ]
})

export class AppModule { }
