
export class Server {
    public id: number;
    public name: string;
    public address: string;
    public state: string;
    public userid: number;
    public expanded: boolean;

    constructor() {
        this.state = 'Disabled';
        this.expanded = false;
    }
}
