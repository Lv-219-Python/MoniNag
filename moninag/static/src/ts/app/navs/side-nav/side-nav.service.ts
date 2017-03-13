import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

import { Check } from '../../checks/check';
import { Plugin } from '../../checks/plugin';
import { Service } from '../../services/services';
import { Server } from '../../servers/model';


@Injectable()
export class SideNavService {

    constructor(private http: Http) { }

    private treeUrl = 'api/1/tree';

    getTree(): Observable<Server> {
        return this.http.get(this.treeUrl)
            .map((res: Response) => res = res.json())
            .catch((error: any) => Observable.throw(error.json().error || 'Server error'));
    }
}
