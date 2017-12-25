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
        self.node = dict()
        self.data = dict() 
        self.datanode = dict()
        self.data['hostinfo']= dict()
        self.lines = value.readlines()
        self.headerlist()
        self.hostinfo()
        self.serialtojson()

    def headerlist(self):
        """creates headers from first line read in from file self.lines"""
        self.headers = self.lines[2].split()
        self.headercnt = len(self.headers)

    def hostinfo(self):
        """get host info {"ipv4":address,"ipv6":address} """
        self.infolist = dict(ip = 'ipv4',date = 'datetime')
        self.host = self.lines[0].split()
        self.date = self.lines[1]
        self.node.clear()
        self.node[self.infolist['ip']] = self.host[0]
        self.node[self.infolist['date']] = self.date
        self.data['hostinfo'].update(self.node)
        
        
    def serialtojson(self):
        """creates dictionary object to output to json self.data"""
        self.datanode.clear()
        self.datanode['process'] = []
        for line in self.lines[3:]:
            __cnt = 0
            self.values = line.split()
            self.node.clear()            
            for __cnt in range(0,self.headercnt):
               self.node[self.headers[__cnt]]=self.values[__cnt]
            self.datanode['process'].append(self.node)
        self.data['hostinfo'].update(self.datanode)
        
    def outputjson(self):
        """dumps json self.data to stdout"""
        json.dump(self.data, sys.stdout, indent=4)
        
    def jsontofile(self):
        """dumps json to file based on ip 192.168.0.[1] = host1"""
        self.ip = self.host[0].split('.')
        self.hostnum = self.ip[3]
        self.file = 'host' + self.hostnum + '.json'
        with open(self.file,'w') as jsonfile:
            json.dump(self.data, jsonfile, indent = 4)


if __name__ == "__main__":
    #strLine = sys.stdin.readlines()
    p = PsTblToJson(sys.stdin)
#    p.outputjson()
    p.jsontofile()


       # sys.stdout.write(line)
