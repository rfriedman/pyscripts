#!/bin/sh
ssh richard@192.168.0.4 'rm /home/richard/.ssh/known_hosts'
ssh richard@192.168.0.4 'rm /home/richard/.ssh/authorized_keys'
