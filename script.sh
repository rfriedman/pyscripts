#!/bin/sh
ssh pi@192.168.0.6 'rm /home/pi/.ssh/known_hosts'
ssh pi@192.168.0.6 'rm /home/pi/.ssh/authorized_keys'
#!/bin/sh
ssh pi@192.168.0.6 'mkdir /home/pi/.ssh'
ssh pi@192.168.0.6 'ssh-keygen'
cat /home/pi/.ssh/key.host | ssh pi@192.168.0.6 'cat>>/home/pi/.ssh/known_hosts'
cat /home/pi/.ssh/id_rsa.pub | ssh pi@192.168.0.6 'cat>>/home/pi/.ssh/authorized_keys'
ssh pi@192.168.0.6 'cat /home/pi/.ssh/id_rsa.pub' | cat>>/home/pi/.ssh/authorized_keys
#!/bin/sh
cat /home/pi/jsonlog.sh | ssh pi@192.168.0.6 'cat>/home/pi/jsonlog.sh'
ssh -t pi@192.168.0.6 'sudo cp /home/pi/jsonlog.sh /usr/local/sbin/jsonlog.sh'
ssh pi@192.168.0.6 'rm /home/pi/jsonlog.sh'
ssh -t pi@192.168.0.6 'sudo chmod 755 /usr/local/sbin/jsonlog.sh'
#!/bin/sh
ssh pi@192.168.0.6 'cp /etc/crontab /home/pi/crontab'
cat /home/pi/crontab | ssh pi@192.168.0.6 'cat>>/home/pi/crontab'
ssh -t pi@192.168.0.6 'sudo cp /home/pi/crontab /etc/crontab'
ssh pi@192.168.0.6 'rm /home/pi/crontab'
