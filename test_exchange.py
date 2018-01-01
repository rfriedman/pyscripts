from batch import intrpolate
from keyexchange import keyexchange
testfile = 'test/batch.json'

def keyexchange_init():
    batch = intrpolate(testfile)
    batch.createbatch()
    keybatch = keyexchange(batch.proclist)
    return keybatch

def keyexchange_arglist():
    batch = intrpolate(testfile)
    batch.createbatch()
    keybatch = keyexchange(batch.proclist)
    keybatch.argslist()
    for list in keybatch.arglist:
        for arg in list:
          print arg
    return keybatch.arglist 
   
def keyexchange_tstart():
    batch = intrpolate(testfile)
    batch.createbatch()
    keybatch = keyexchange(batch.proclist)
    keybatch.argslist()
    keybatch.start()
    return keybatch.arglist 
   
if __name__ =="__main__":
    print('hello')
    key = keyexchange_arglist()
    print key 

    
