#!/usr/bin/env python
from subprocess import call, Popen, PIPE
from multiprocessing import Process

class sensor(object):
	def __init__(self):
		self.name ="monitor"
	def setproc(self,str):
		self.proc = str
	def setdev(self,str):
		self.device =str
	def setdevname(self,str):
		self.devName = str
	def setoutfile(self,str):
		self.filename = str
	def start(self):
		Popen([self.proc , self.device],stdout=PIPE,stderr=PIPE)#,  self.devName])#, self.filename])
		
		
def a():
	s2 = sensor()
	s2.setproc("/bin/ls")
	s2.setdev("-l")
	s2.setdevname("| less")
	s2.setoutfile("/home/richard/dev/pythonscripts/echo.py")
	s2.start()

if __name__ == '__main__':
	a()
 	 #  p2 = Process(target=a )
    #	p2.start()
    #	p2.join()

	
    