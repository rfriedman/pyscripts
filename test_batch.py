from batch import intrpolate

testfile = 'test/batch.json'

def batch_createbatch():
    batch = intrpolate(testfile)
    batch.createbatch()
    return batch

   
if __name__ =="__main__":
    print('hello')
    batch = batch_createbatch()
#    print batch.joblist
#    batch = batch_createbatch()
#    print batch.proclist
    
