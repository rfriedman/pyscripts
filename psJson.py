#!/usr/bin/python

import sys
import json
#class to create dictionary object from output headers and process output columns
class outputToDictionary(object):
    def __init__(self,value):
        self.lines=value
        self.stringList()
        self.serialtojson()
    def stringList(self):
        self.headers = self.lines[0].split()
        self.headercnt=len(self.headers)
    def serialtojson(self):
        self.data={}
        self.node=dict()
        self.data['process']=[]
        for line in self.lines[1:]:
            __cnt = 0
            self.values=line.split()
            for i in range(0,self.headercnt):
               self.node[self.headers[__cnt]]=self.values[__cnt]
               __cnt = __cnt +1
            self.data['process'].append(self.node)
    def outputjson(self):
        with open('ps_data.txt', 'w') as outfile:  
           json.dump(self.data, outfile, indent=4)

if __name__ == "__main__":
    strLine = sys.stdin.readlines()
    p = outputToDictionary(strLine)
    p.outputjson()


       # sys.stdout.write(line)
