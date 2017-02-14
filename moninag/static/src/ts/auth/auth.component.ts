// Import the Component decorator
import { Component } from '@angular/core';

@Component({
  selector: 'auth-app',
  styles: [require('../../less/styles.less').toString()],
  template: `
  <div class="row">
    <div class="col-sm-12">
      <div class="col-md-4 col-md-offset-4">
        <message></message>
      </div>
      <router-outlet></router-outlet>
    </div>
  </div>
  `
})
export class AuthComponent {}
