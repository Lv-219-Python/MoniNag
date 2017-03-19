INSERT INTO nagplugin_nagplugin (id, name, template, description) VALUES 
    (1, 'check_dns', '/usr/lib/nagios/plugins/check_dns -H {host}', 'This plugin uses the nslookup program to obtain the IP address for the given host/domain query. An optional DNS server to use may be specified. If no DNS server is specified, the default server(s) specified in /etc/resolv.conf will be used.'),
    (2, 'check_ftp', '/usr/lib/nagios/plugins/check_ftp -H {host} -p {port}', 'This plugin tests FTP connections with the specified host (or unix socket).'),
    (3, 'check_http', '/usr/lib/nagios/plugins/check_http -H {host} -p {port}', 'This plugin tests the HTTP service on the specified host. It can test normal (http) and secure (https) servers, follow redirects, search for strings and regular expressions, check connection times, and report on certificate expiration times.'),
    (4, 'check_ping', '/usr/lib/nagios/plugins/check_ping -H {host} -w 100.0,20% -c 500.0,60%', 'Use ping to check connection statistics for a remote host.'),
    (5, 'check_smtp', '/usr/lib/nagios/plugins/check_smtp -H {host} -p {port}', 'This plugin will attempt to open an SMTP connection with the host.'),
    (6, 'check_tcp', '/usr/lib/nagios/plugins/check_tcp -H {host} -p {port}', 'This plugin tests TCP connections with the specified host (or unix socket).'),
    (7, 'check_time', '/usr/lib/nagios/plugins/check_time -H {host} -p {port}', 'This plugin will check the time on the specified host.');
