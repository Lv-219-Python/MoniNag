
import {Component} from 'angular2/core';


@Component({
    selector: 'moninag-app',
    template: `
        <div class="row">
            <div class="col-sm-6">
                <todo-list></todo-list>
            </div>
            <div class="col-sm-6">
                <todo-view></todo-view>
            </div>
        </div>
    `
})

export class MoniNagApp {
    constructor() {}
}
