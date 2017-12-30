#!/usr/bin/python
from subprocess import Popen, PIPE
import argparse, json

class processbatch(object):
  def __init__(self, batchfile):
      with open(batchfile,'r') as data:
        self.batch = json.load(data)
      self.hostlist = self.batch['hostlist']
      self.joblist = self.batch['joblist']
      self.node = dict()
      self.proc = list()
      self.cmds = list()
      self.args = list()
  def createbatch(self):
      for hostlist in self.hostlist:
        for host in hostlist:
          for joblist in self.joblist:
            for job in joblist:
              self.setcmd(job['cmd'].encode("utf-8"))
              self.setargs(job['args'].encode("utf-8").replace("{host}",host))
          
      self.node['cmd'] = self.cmds[0]
      self.node['args'] = self.args[0]
      self.setproc(self.node)
      self.node = dict()

      self.node['cmd'] = self.cmds[1]
      self.node['args'] = self.args[1]
      self.setproc(self.node)
      self.node = dict()
      
      self.cmds = list()
      self.args = list()
          
           
  '''['cmd','cmd']'''
  def setcmd(self, value):
        self.cmds.append(value)
    
  '''['args','args']'''
  def setargs(self, value):
        self.args.append(value)
  '''[
      {"cmd":self.proc[0],"args":self.proc[0]},
      {"cmd":self.proc[1],"args":self.proc[1]}
     ]
  '''
  def setproc(self, value):
        print(value)
        self.proc.append(value)
        
  def start(self):
        print(self.proc) 

