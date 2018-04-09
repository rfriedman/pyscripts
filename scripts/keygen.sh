#!/bin/sh
ssh pi@172.16.24.26 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.28 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.29 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.31 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.32 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.36 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.37 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.38 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.39 'mkdir /home/pi/.ssh'
ssh pi@172.16.24.26 'ssh-keygen'
ssh pi@172.16.24.28 'ssh-keygen'
ssh pi@172.16.24.29 'ssh-keygen'
ssh pi@172.16.24.31 'ssh-keygen'
ssh pi@172.16.24.32 'ssh-keygen'
ssh pi@172.16.24.36 'ssh-keygen'
ssh pi@172.16.24.37 'ssh-keygen'
ssh pi@172.16.24.38 'ssh-keygen'
ssh pi@172.16.24.39 'ssh-keygen'
ssh pi@172.16.24.26 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
ssh pi@172.16.24.28 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
ssh pi@172.16.24.29 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
ssh pi@172.16.24.31 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
ssh pi@172.16.24.32 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
ssh pi@172.16.24.36 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
ssh pi@172.16.24.37 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
ssh pi@172.16.24.38 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
ssh pi@172.16.24.39 'ssh-keyscan -H -t rsa 172.16.24.192>>/home/pi/.ssh/known_hosts'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.26 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.28 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.29 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.31 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.32 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.36 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.37 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.38 'cat>>/home/pi/.ssh/authorized_keys'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@172.16.24.39 'cat>>/home/pi/.ssh/authorized_keys'
ssh pi@172.16.24.26 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.28 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.29 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.31 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.32 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.36 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.37 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.38 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
ssh pi@172.16.24.39 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
