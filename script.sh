#!/bin/sh
ssh pi@192.168.0.7 'ssh-keygen'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@192.168.0.7 'cat>>/home/pi/.ssh/authorized_keys'
ssh pi@192.168.0.7 'cat /home/pi/.ssh/id_rsa.pub'>>/home/pi/.ssh/authorized_keys_replace
cat /home/pi/jsonlog.sh | ssh pi@192.168.0.7 'cat>>/home/pi/jsonlog.sh && sudo cp /home/pi/jsonlog.sh /usr/local/sbin'
