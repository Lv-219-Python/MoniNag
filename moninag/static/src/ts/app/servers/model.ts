export class Server {
  constructor(
    public id: number,
    public name: string,
    public address: string,
    public state: string,
    public userid: number
  ){}
}
export const states = ['NotSelected', 'Production', 'Staging'];
