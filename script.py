#!/bin/sh
ssh pi@192.168.0.202 'mkdir /home/pi/.ssh'
ssh 192.168.0.202 'ssh-keygen'
cat /home/pi/.ssh/key.host | ssh pi@192.168.0.202 'cat>>/home/pi/.ssh/known_hosts'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@192.168.0.202 'cat>>/home/pi/.ssh/authorized_keys'
ssh pi@192.168.0.202 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
cat /home/pi/jsonlog.sh | ssh pi@192.168.0.202 'cat>/home/pi/jsonlog.sh
ssh pi@192.168.0.202 sudo cp /home/pi/jsonlog.sh /usr/local/sbin/jsonlog.sh
ssh pi@192.168.0.202 'rm /home/pi/jsonlog.sh'
cat /home/pi/crontab | ssh pi@192.168.0.202 'cat>/home/pi/crontab
ssh pi@192.168.0.202 sudo cp /home/pi/crontab /etc/crontab
ssh pi@192.168.0.202 rm /home/pi/crontab'
ssh pi@192.168.0.202 'sudo chmod 755 /usr/local/sbin/jsonlog.sh'
