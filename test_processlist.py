from batch import intrpolate
from processlist import processlist
import sys
import pdb
testfile = 'test/batch.json'

def processlist_init():
    batch = intrpolate(testfile)
    batch.createbatch()
    keybatch = processlist(batch.proclist)
    return keybatch

def processlist_arglist():
    batch = intrpolate(testfile)
    batch.createbatch()
    keybatch = processlist(batch.proclist)
    keybatch.argslist()
    
    return keybatch.arglist 
    
def processlist_tstart():
    print('processlist_tstart')
    batch = intrpolate(testfile)
    batch.createbatch()
    keybatch = processlist(batch.proclist)
    keybatch.argslist()
    pdb.set_trace()
    keybatch.start()
    return keybatch.arglist

   
def processlist_writescript():
    sys.stderr.write('process_writescript\n')
    batch = intrpolate(testfile)
    batch.createbatch()
    keybatch = processlist(batch.proclist)
    keybatch.argslist()
    keybatch.writescript()
    return keybatch.arglist
   
if __name__ =="__main__":
#  args=processlist_arglist()
#  print(args)
   processlist_writescript()
    
