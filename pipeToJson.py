#!/usr/bin/env python
from subprocess import call, Popen, PIPE
from multiprocessing import Process
import sys

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
	s2.setArgsOne("-a")
	s2.setredirectproc("./echo.py")
	s2.start()

if __name__ == '__main__':
	a()
	

	
    