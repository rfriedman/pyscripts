#!/usr/bin/python
from batch import intrpolate
from subprocess import Popen,PIPE
import subprocess
import sys

def arglist(proc):
    l = proc['args'].split()
    l.insert(0,proc['cmd'])
    return l    
batch = intrpolate('test/batch.json')
batch.createbatch()
print(batch.proclist )

for proc in batch.proclist:
    arglst=proc['args'].split()
    arglst.insert(0,proc['cmd'])
    print(arglst)
    p=Popen(arglst,stdout=PIPE,stdin=PIPE,stderr=PIPE)
    batch_out= p.communicate(input='\nn\n')[0]
    sys.stdout.write(batch_out) 
print('\n')



