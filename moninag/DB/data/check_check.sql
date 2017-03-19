INSERT INTO check_check (id, name, run_freq, service_id, target_port, plugin_id, last_run, output, status, state) VALUES
    (12, 'TCP checker', 60, 5, 80, 6, '2017-03-14 15:07:20.074326+02', 'PING WARNING - Packet loss = 0%, RTA = 124.02 ms|rta=124.017998ms;100.000000;500.000000;0.000000 pl=0%;20;60;0', 'WARNING', 't'),
    (9, 'DNS checker', 300, 4, 80, 1, '2017-03-17 10:10:31.485749+02', 'DNS OK: 0.051 seconds response time. softserve.ua returns 188.226.190.17|time=0.051400s;;;0.000000','OK', 't'),
    (14, 'Pinger', 60, 6, 80, 4, '2017-03-17 10:12:34.853087+02', 'PING WARNING - Packet loss = 0%, RTA = 124.13 ms|rta=124.130997ms;100.000000;500.000000;0.000000 pl=0%;20;60;0', 'WARNING', 't'),
    (18, 'Can I send email?', 300, 10, 587, 5, '2017-03-14 15:09:27.818877+02', 'TCP OK - 0.167 second response time on github.com port 80|time=0.166832s;;;0.000000;10.000000','OK', 'f'),
    (19, 'FTP I need you!', 300, 11, 21, 2, '2017-03-14 15:04:03.699009+02', 'PING WARNING - Packet loss = 0%, RTA = 123.96 ms|rta=123.964996ms;100.000000;500.000000;0.000000 pl=0%;20;60;0', 'WARNING', 't'),
    (17, 'Are you alive, HTTP?', 300, 9, 80, 3, '2017-03-14 15:11:22.723653+02', 'TCP OK - 0.172 second response time on github.com port 80|time=0.171654s;;;0.000000;10.000000','OK', 't'),
    (13, 'HTTP checker', 60, 5, 80, 3, '2017-03-14 15:11:24.746931+02', 'HTTP OK: HTTP/1.1 301 Moved Permanently - 490 bytes in 0.108 second response time |time=0.108433s;;;0.000000 size=490B;;;0','OK', 't'),
    (20, 'Time difference', 900, 12, 37, 7, '2017-03-14 15:05:02.433722+02', 'HTTP OK: HTTP/1.1 301 Moved Permanently - 103 bytes in 0.291 second response time |time=0.291413s;;;0.000000 size=103B;;;0','OK', 't'),
    (10, 'Pinger', 900, 4, 80, 4, '2017-03-14 14:31:12.686155+02', 'PING CRITICAL - Packet loss = 100%|rta=500.000000ms;100.000000;500.000000;0.000000 pl=100%;20;60;0','FAIL', 't'),
    (15, 'Pinger', 60, 7, 80, 4, '2017-03-14 15:13:32.056138+02', 'HTTP OK: HTTP/1.1 301 Moved Permanently - 103 bytes in 0.296 second response time |time=0.296464s;;;0.000000 size=103B;;;0','OK', 't'),
    (11, 'HTTP checker', 60, 4, 80, 3, '2017-03-14 15:13:33.060569+02', 'PING CRITICAL - Packet loss = 100%|rta=500.000000ms;100.000000;500.000000;0.000000 pl=100%;20;60;0','FAIL', 't');
