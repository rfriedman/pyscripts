from batch import intrpolate
from keygen import keygen
testfile = 'test/batch.json'
def batch_init():
    batch = intrpolate(testfile)
    print(batch.hostlist)
    print(batch.joblist)
    return batch

def batch_createbatch():
    batch = intrpolate(testfile)
    batch.createbatch()
    return batch

   
if __name__ =="__main__":
    print('hello')
    batch = batch_init()
    print batch.hostlist
#    print batch.joblist
#    batch = batch_createbatch()
#    print batch.proclist
    
