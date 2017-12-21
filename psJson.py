#!/usr/bin/python

import sys
import json
#class to create dictionary object from output headers and process output columns
class outputToDictionary(object):
    def __init__(self,value):
        self.lines=value
        self.headerlist()
        self.serialtojson()
    def headerlist(self):
        self.headers = self.lines[0].split()
        self.headercnt=len(self.headers)
    def serialtojson(self):
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
           json.dump(self.data, sys.stdout, indent=4)

if __name__ == "__main__":
    strLine = sys.stdin.readlines()
    p = outputToDictionary(strLine)
    p.outputjson()


       # sys.stdout.write(line)
