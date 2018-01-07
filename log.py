from batch import intrpolate
from processlist import processlist
import sys
import pdb
config = 'config/log.json'
def processlist_writescript():
    sys.stderr.write('process_writescript\n')
    batch = intrpolate(config)
    batch.createbatch()
    keybatch = processlist(batch.proclist)
    keybatch.argslist()
    keybatch.writescript()
    return keybatch.arglist
   
if __name__ =="__main__":
   script=processlist_writescript()
    
