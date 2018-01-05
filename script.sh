#!/bin/sh
ssh pi@172.16.24.46 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.47 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.46 'ssh-keygen'
ssh pi@172.16.24.47 'ssh-keygen'
cat /home/pi/.ssh/key.host | ssh pi@172.16.24.46 'cat>>/home/pi/.ssh/known_hosts'
cat /home/pi/.ssh/key.host | ssh pi@172.16.24.47 'cat>>/home/pi/.ssh/known_hosts'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.46 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.47 'cat>>/home/pi/.ssh/authorized_keys'
ssh pi@172.16.24.46 'cat /home/pi/.ssh/id_rsa.pub'>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.47 'cat /home/pi/.ssh/id_rsa.pub'>>/home/pi/.ssh/authorized_keys
cat /home/pi/jsonlog.sh | ssh pi@172.16.24.46 'cat>/home/pi/jsonlog.sh && sudo cp /home/pi/jsonlog.sh /usr/local/sbin/jsonlog.sh&&rm /home/pi/jsonlog.sh'
cat /home/pi/jsonlog.sh | ssh pi@172.16.24.47 'cat>/home/pi/jsonlog.sh && sudo cp /home/pi/jsonlog.sh /usr/local/sbin/jsonlog.sh&&rm /home/pi/jsonlog.sh'
cat /home/pi/crontab | ssh pi@172.16.24.46 'cat>/home/pi/crontab && sudo cp /home/pi/crontab /etc/crontab&&rm /home/pi/crontab'
cat /home/pi/crontab | ssh pi@172.16.24.47 'cat>/home/pi/crontab && sudo cp /home/pi/crontab /etc/crontab&&rm /home/pi/crontab'
ssh pi@172.16.24.46 'sudo chmod 755 /usr/local/sbin/jsonlog.sh'
ssh pi@172.16.24.47 'sudo chmod 755 /usr/local/sbin/jsonlog.sh'
