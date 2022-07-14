#!/bin/bash



date=`date '+_%Y_%m_%d_%H_%M'`

tar -zcf /home/yuri/jobe/backup/html$date.tar.gz --directory=/home/yuri/jobe/ html
