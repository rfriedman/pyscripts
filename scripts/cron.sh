#!/bin/sh
ssh richard@192.168.0.4 'cp /etc/crontab /home/richard/crontab'
cat /home/pi/crontab | ssh richard@192.168.0.4 'cat>>/home/richard/crontab'
ssh -t richard@192.168.0.4 'sudo cp /home/richard/crontab /etc/crontab'
ssh richard@192.168.0.4 'rm /home/richard/crontab'
