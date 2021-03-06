#!/bin/sh
sudo timedatectl set-timezone America/New_York &&
sudo date --set="$(ssh pi@172.16.24.192 date)" &&
hostname -I > /tmp/out.txt &&
date >> /tmp/out.txt && 
cat /sys/class/net/wlan0/address >> /tmp/out.txt &&
cat /home/pi/.station >> /tmp/out.txt &&
ps -a >> /tmp/out.txt && 
cat /tmp/out.txt | /usr/bin/ssh pi@172.16.24.192 '/home/pi/psjson.py 2>>error.log' &&  
rm /tmp/out.txt
