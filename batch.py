#!/usr/bin/env python
from subprocess import Popen, PIPE
import argparse, json

class intrpolate(object):
  def __init__(self, batchfile):
      with open(batchfile,'r') as data:
        self.batch = json.load(data)
      self.hostuser = self.batch['hostuser']
      self.clientuser = self.batch['clientuser']
      self.hostlist = self.batch['hostlist']
      self.joblist = self.batch['joblist']
      self.node = dict()
      self.proclist = list()
      self.cmds = list()
      self.args = list()
  def createbatch(self):
          for job in self.joblist:
              self.node['cmd'] = job['cmd'] 
              self.node['args'] = job['args'] 
              self.setproc(self.node)
              self.node = dict()
          for node in self.proclist:
            self.setargs(node)
          self.proclist = self.args
   
  '''[{"cmd":self.cmds,"args":self.args},{"cmd":self.cmds,"args":self.args}] (joblist*hostlist)'''
  def setargs(self, node):
        for host in self.hostlist:
                self.node['args']=node['args'].replace("{host}",host)
                self.node['args']=self.node['args'].replace("{clientuser}",self.clientuser)
                self.node['args']=self.node['args'].replace("{hostuser}",self.hostuser)
                self.node['cmd']=node['cmd']
                self.args.append(self.node)
                self.node =dict()
         
  '''{"cmd":self.cmds,"args":self.args} (joblist/joblist)'''
  def setproc(self, value):
        self.proclist.append(value)
        
  def start(self):
        print(self.proclist) 


