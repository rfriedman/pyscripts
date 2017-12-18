#!/usr/bin/python

import sys
#class to create dictionary object from output headers and process output columns
class outputToDictionary(object):
    def __init__(self,value):
        self.lines=value
    def makeHeaders(self):
        self.headers = self.lines[:1].split()


if __name__ == "__main__":
    strLine = sys.stdin.readlines()
    for line in strLine:
        strSplit = line.split()
        for a in strSplit:
           print a
        sys.stderr.write("DEBUG: got line: " + line)
       # sys.stdout.write(line)