export class Service {
    public id: number;
    public name: string;
    public status: string;
    public server_id: number;
    public state: boolean;
    public expanded: boolean;

    constructor() {
        this.status = '';
        this.expanded = false;
    }
}
