export class Check {
    constructor(
        public id: number,
        public name: string,
        public target_port: number,
        public run_freq: number,
        public plugin_id: number,
        public service_id: number
    ) { }
}