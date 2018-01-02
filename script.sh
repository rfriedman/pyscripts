#!/bin/sh
ssh richard@192.168.0.6 'ssh-keygen'
cat /home/pi/.ssh/id_rsa | ssh richard@192.168.0.6 'cat>>/home/richard/.ssh/authorized_keys_replace'
ssh richard@192.168.0.6 'cat /home/richard/.ssh/id_rsa.pub'>/home/pi/.ssh/authorized_keys_replace
ssh richard@192.168.0.6 'ssh-keygen'
cat /home/pi/.ssh/id_rsa | ssh richard@192.168.0.6 'cat>>/home/richard/.ssh/authorized_keys_replace'
ssh richard@192.168.0.6 'cat /home/richard/.ssh/id_rsa.pub'>/home/pi/.ssh/authorized_keys_replace
