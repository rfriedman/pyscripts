#!/bin/sh
ssh richard@192.168.0.4 'mkdir /home/pi/.ssh'
ssh richard@192.168.0.4 'ssh-keygen'
cat /home/pi/.ssh/key.host | ssh richard@192.168.0.4 'cat>>/home/richard/.ssh/known_hosts'
cat /home/pi/.ssh/id_rsa.pub | ssh richard@192.168.0.4 'cat>>/home/richard/.ssh/authorized_keys'
ssh richard@192.168.0.4 'cat /home/richard/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
