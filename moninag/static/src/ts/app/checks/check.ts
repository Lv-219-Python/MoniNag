export class Check {
    public id: number;
    public name: string;
    public status: string;
    public last_run: string;
    public output: string;
    public target_port: number;
    public run_freq: number;
    public plugin_id: number;
    public service_id: number;
    public state: boolean;
}
