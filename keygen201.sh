#!/bin/sh
ssh pi@192.168.0.201 'mkdir /home/pi/.ssh'
ssh pi@192.168.0.201 'ssh-keygen'
cat /home/pi/.ssh/key.host | ssh pi@192.168.0.201 'cat>>/home/pi/.ssh/known_hosts'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@192.168.0.201 'cat>>/home/pi/.ssh/authorized_keys'
ssh pi@192.168.0.201 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
