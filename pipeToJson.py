#!/usr/bin/python
from subprocess import Popen, PIPE
import argparse

class pipeToProcess(object):
	def __init__(self):
		self.name ="monitor"
	def setproc(self,str):
		self.proc = str
	def setredirectproc(self,str):
		self.proc2 = str
	def setArgsOne(self,str):
		self.args1 =str
	def start(self):
		self.processIn=Popen([self.proc , self.args1],stdout=PIPE,stderr=PIPE)
		#for line in self.processIn.stdout:
		#	sys.stdout.write(line)
		self.processOut=Popen([self.proc2 ],stdin=self.processIn.stdout,stderr=PIPE)
		self.processIn.stdout.close()
		self.processOut.communicate()
		
def a():
	s2 = pipeToProcess()
	s2.setproc("/bin/ps")
	s2.setArgsOne("-A")
	s2.setredirectproc("./psJson.py")
	s2.start()

if __name__ == '__main__':
  Parser = argparse.ArgumentParser(description='Select process for json serialize.')
  Parser.add_argument('process', help='process to serialize')
  Args= Parser.parse_args()

  if Args.process == "ps":
    a()



    