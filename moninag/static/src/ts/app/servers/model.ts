
export class Server {
    public id: number;
    public name: string;
    public address: string;
    public state: string;
    public userid: number;

    constructor() {
        this.state = 'Disabled';
    }
}
