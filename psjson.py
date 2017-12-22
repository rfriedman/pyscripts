#!/usr/bin/python
"""serialize process to json"""
import sys
import json
#class to create dictionary object from output headers and process output columns
class PsTblToJson(object):
    """create json object from process list (bash$ps)
       the following properties are used:
       member variables:
       self.lines:  lines from file with newlines removed
       self.headers:  list contains headers from process table ie(["pid","cmd"])
       self.headercnt:  int number of columns in table ie 
       self.values:  list contains individual values for each process ie(["1234","ps"]) 
       self.data:  dictionary" containing the structure to output to json
       self.node:  dictionary containing the key:value pair ie([{"pid":"1234"}])
       """  
    def __init__(self,value):
        """constructor reads file and parses lines into a list self.lines"""
        self.lines = value.readlines()
        self.headerlist()
        self.serialtojson()
    def headerlist(self):
        """creates headers from first line read in from file self.lines"""
        self.headers = self.lines[0].split()
        self.headercnt = len(self.headers)
    def serialtojson(self):
        """creates dictionary object to output to json self.data"""
        self.data={}
        self.data['process']=[]
        for line in self.lines[1:]:
            __cnt = 0
            self.values=line.split()
            self.node=dict()            
            for __cnt in range(0,self.headercnt):
               self.node[self.headers[__cnt]]=self.values[__cnt]
            self.data['process'].append(self.node)
    def outputjson(self):
        """dumps json file self.data to stdout"""
        json.dump(self.data, sys.stdout, indent=4)

if __name__ == "__main__":
    #strLine = sys.stdin.readlines()
    p = PsTblToJson(sys.stdin)
    p.outputjson()


       # sys.stdout.write(line)
