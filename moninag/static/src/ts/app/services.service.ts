/* 
import { DBtest } from './dbtest';
import { SERVICES } from './mock-db';

import { Injectable } from '@angular/core';

@Injectable()
export class ServicesService {
    getDBs(): Promise<DBtest[]> {
        return Promise.resolve(SERVICES);
    }

    getDB(id: number): Promise<DBtest> {
    return this.getDBs()
               .then(DBs => DBs.find(DB => DB.id === id));
  }

}
*/