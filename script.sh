#!/bin/sh
ssh richard@192.168.0.7 'mkdir /home/richard/.ssh'
ssh richard@192.168.0.7 'ssh-keygen'
cat /home/pi/.ssh/key.host | ssh richard@192.168.0.7 'cat>>/home/richard/.ssh/known_hosts'
cat /home/pi/.ssh/id_rsa.pub | ssh richard@192.168.0.7 'cat>>/home/richard/.ssh/authorized_keys'
ssh richard@192.168.0.7 'cat /home/richard/.ssh/id_rsa.pub'>>/home/pi/.ssh/authorized_keys
cat /home/pi/jsonlog.sh | ssh richard@192.168.0.7 'cat>/home/richard/jsonlog.sh && sudo cp /home/richard/jsonlog.sh /usr/local/sbin/jsonlog.sh&&rm /home/richard/jsonlog.sh'
cat /home/pi/crontab | ssh richard@192.168.0.7 'cat>/home/richard/crontab && sudo cp /home/richard/crontab /etc/crontab&&rm /home/richard/crontab'
ssh richard@192.168.0.7 'sudo chmod 755 /usr/local/sbin/jsonlog.sh'
