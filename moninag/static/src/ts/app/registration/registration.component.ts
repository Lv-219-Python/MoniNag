// Import the Component decorator
import { Component } from '@angular/core';

@Component({
  // We'll call our root component daily-deals
  selector: 'registration-app',
  template: `
    <div class="col-sm-12">
      <!-- The router-outlet directive will display the component based on the route we are on, more on this soon -->
      <message></message>
      <router-outlet></router-outlet>
      <login></login>
    </div>
  `
})
export class RegistrationAppComponent {
  constructor() {}
}
