#!/bin/bash

/usr/local/bin/docker-compose -f /home/yuri/jobe/docker-compose.yml run certbot renew \
&& /usr/local/bin/docker-compose -f /home/yuri/jobe/docker-compose.yml kill -s SIGHUP nginx
