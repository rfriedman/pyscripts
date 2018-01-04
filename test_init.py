from batch import intrpolate

testfile = 'test/batch.json'
def batch_init():
    batch = intrpolate(testfile)
    return batch
   
if __name__ =="__main__":
    print('hello')
    batch = batch_init()
    
