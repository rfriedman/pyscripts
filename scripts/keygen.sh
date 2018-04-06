#!/bin/sh
ssh pi@172.16.24.3 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.4 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.6 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.9 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.10 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.11 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.12 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.13 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.3 'ssh-keygen'
ssh pi@172.16.24.4 'ssh-keygen'
ssh pi@172.16.24.6 'ssh-keygen'
ssh pi@172.16.24.9 'ssh-keygen'
ssh pi@172.16.24.10 'ssh-keygen'
ssh pi@172.16.24.11 'ssh-keygen'
ssh pi@172.16.24.12 'ssh-keygen'
ssh pi@172.16.24.13 'ssh-keygen'
ssh pi@172.16.24.3 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
ssh pi@172.16.24.4 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
ssh pi@172.16.24.6 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
ssh pi@172.16.24.9 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
ssh pi@172.16.24.10 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
ssh pi@172.16.24.11 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
ssh pi@172.16.24.12 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
ssh pi@172.16.24.13 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.2 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.3 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.4 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.6 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.9 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.10 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.11 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.12 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.13 'cat>>/home/pi/.ssh/authorized_keys'
ssh pi@172.16.24.2 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.3 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.4 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.6 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.9 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.10 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.11 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.12 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.13 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
