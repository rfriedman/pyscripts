#!/usr/bin/python
from batch import intrpolate
from subprocess import Popen,PIPE
import subprocess
import sys
'''
use intrpolate.proclist as constructor
change format:  [{"cmd":cmd "args":args},{"cmd":cmd "args":args}]
to ["'cmd' 'args','cmd' 'args'"]
ie  {"cmd":"ssh", "args":"?pi@192.168.0.1?'ssh-keygen'"} becomes:
ssh pi@192.168.0.1 'ssh-keygen'
'''
class processlist(object):
    def __init__(self,proclist):
        self.proclist = proclist
        self.arglist = list()
        self.inputstr = '\nn\n'
    
    def argslist(self):
        l=list()
        j=list()
        for proc in self.proclist:
          args = proc['args'].split()
          args.insert(0,proc['cmd'])
          self.arglist.append(args)
        for lst in self.arglist:
            for arg in lst:
                l.append(arg.encode("utf-8").replace("?"," ").replace('"',''))
            j.append(l)
            l=list()

        self.arglist=j
    def writescript(self):
        sys.stdout.write('#!/bin/sh\n')
        for arglist in self.arglist:
            for arg in arglist:
              sys.stdout.write(arg)
            sys.stdout.write('\n')
    def start(self):
        for arglst in self.arglist:
            #p=Popen(arglst)
            p=Popen(arglst,stdout=PIPE,stdin=PIPE,stderr=PIPE)
            result = p.stdout.readlines()
            print result
            print('\n')



