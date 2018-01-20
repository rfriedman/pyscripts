#!/bin/sh
./resetkeys.py>script.sh
./keygen.py >>script.sh
./log.py >>script.sh
./cron.py>>script.sh
