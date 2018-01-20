#!/bin/sh
hostname -I > /tmp/out.txt &&
date >> /tmp/out.txt && 
cat /sys/class/net/wlan0/address >> /tmp/out.txt &&
ps -a >> /tmp/out.txt &&  


cat /tmp/out.txt | /usr/bin/ssh pi@192.168.0.201 '/home/pi/psjson 2>>error.log'


 
 #rm /tmp/out.txt
