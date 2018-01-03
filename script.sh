#!/bin/sh
ssh richard@192.168.0.7 'mkdir /home/pi/.ssh'
ssh richard@192.168.0.7 'ssh-keygen'
cat /home/pi/.ssh/key.host | ssh richard@192.168.0.7 'cat>>/home/pi/.ssh/known_hosts'
cat /home/pi/.ssh/id_rsa.pub | ssh richard@192.168.0.7 'cat>>/home/pi/.ssh/authorized_keys'
ssh richard@192.168.0.7 'cat /home/pi/.ssh/id_rsa.pub'>>/home/pi/.ssh/authorized_keys
cat /home/pi/jsonlog.sh | ssh richard@192.168.0.7 'cat>/home/pi/jsonlog.sh && sudo cp /home/pi/jsonlog.sh /usr/local/sbin/jsonlog.sh&&rm /home/pi/jsonlog.sh'
cat /home/pi/crontab | ssh richard@192.168.0.7 'cat>/home/pi/crontab && sudo cp /home/pi/crontab /etc/crontab&&rm /home/pi/crontab'
ssh richard@192.168.0.7 'sudo chmod 755 /usr/local/sbin/jsonlog.sh'
