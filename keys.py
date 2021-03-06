#!/usr/bin/python
from batch import intrpolate
from subprocess import Popen,PIPE
import subprocess
import sys

class keygen(object):
    def __init__(self,proclist):
        self.proclist = proclist
        self.arglist = list()
        self.inputstr = '\nn\n'
    
    def arglist(proc):
        args = proc['args'].split()
        args.insert(0,proc['cmd'])
        self.arglist.append(args) 
    
    def start(self):
        for proc in batch.proclist:
          arglst=arglist(proc)
          print(arglst)
          p=Popen(arglst,stdout=PIPE,stdin=PIPE,stderr=PIPE)
          batch_out= p.communicate(input=self.inputstr)[0]
          sys.stdout.write(batch_out) 
          print('\n')



