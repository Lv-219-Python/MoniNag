import { Http } from '@angular/http';
import { Injectable } from '@angular/core';

import {Observable} from 'rxjs/Rx';
import 'rxjs/add/operator/map';


@Injectable()
export class SearchService {
  
  constructor(private http: Http) {}
  
  getService(serviceId: string) {
    return this.http.get(`http://127.0.0.1:8000/api/1/service/21/`)
      .map(response => response.json());
  }
}

