export class Contact {

    id: number;
    email: string;
    first_name: string;
    second_name: string;

    constructor(obj: any){
        this.id = obj.id;
        this.email = obj.email;
        this.first_name = obj.first_name;
        this.second_name = obj.second_name;
    }
}
