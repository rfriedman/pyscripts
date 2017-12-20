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
        self.data['process']=[]
        for line in self.lines[1:]:
            self.values=line.split()
            self.data['process'].append({  
          self.headers[0]:self.values[0],
          self.headers[1]:self.values[1],
          self.headers[2]:self.values[2],
          self.headers[3]:self.values[3],
          })
    def outputjson(self):
        with open('ps_data.txt', 'w') as outfile:  
           json.dump(self.data, outfile, indent=4)

if __name__ == "__main__":
    strLine = sys.stdin.readlines()
    p = outputToDictionary(strLine)
    p.outputjson()


       # sys.stdout.write(line)