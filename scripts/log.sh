#!/bin/sh
cat /home/pi/jsonlog.sh | ssh richard@192.168.0.4 'cat>/home/richard/jsonlog.sh'
ssh -t richard@192.168.0.4 'sudo cp /home/richard/jsonlog.sh /usr/local/sbin/jsonlog.sh'
ssh richard@192.168.0.4 'rm /home/richard/jsonlog.sh'
ssh -t richard@192.168.0.4 'sudo chmod 755 /usr/local/sbin/jsonlog.sh'
