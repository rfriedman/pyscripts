#!/usr/bin/python
from subprocess import Popen, PIPE
import argparse, json

class pipeToProcess(object):
	''' need to accomodate:
	ssh {user}@{hostlist} 'ssh-keygen' 2>>error.log | null
	cat .ssh/id_rsa.pub | ssh {user}@{hostlist} 'cat >> ~/.ssh/authorized_keys'
	ssh {user}@{hostlist} 'cat ~/.ssh/id_rsa.pub' | cat >> ~/.ssh/authorized_keys
	cat hostinfo.sh | ssh {user}@{hostlist} 'cat >> ~/hostinfo.sh &&
	 sudo cp ~/hostinfo.sh /usr/local/sbin &&
	 rm ~/hosinfo.sh'
	cat /etc/crontab | ssh {user}@{hostlist} 'cat >> ~/crontab &&
	 sudo cp ~/crontab /etc/crontab &&
	 rm ~/crontab'
	'''
	def __init__(self,batchfile):
		with open(batchfile,'r') as json_data:
			self.batch = json.load(json_data)

		self.joblist = self.batch['joblist']
		self.hostlist = self.batch['hostlist']
'''
	def createbatch(self,proc1):
		"""create batch from:
		{
				{"hostlist":[{pi@192.168.0.1},{pi@192.168.0.2}],
				 "joblist":[
					 		[
						     {"cmd":ssh,"args":"{host} 'ssh-keygen' 2>>error.log"},
							 {"cmd":null,"args":null}
							 ],
				 			]
		}

		"""
		for host in self.hostlist:
			for job in self.joblist:
               self.proc(job['cmd'].encode("utf-8"))
			   self.args1(job['args'].encode("utf-8").replace("{host}",host.encode("utf-8"))
	'''		   

	def setproc(self,str):
		self.proc = str
	def setredirectproc(self,str):
		self.proc2 = str
	def setArgsOne(self,str):
		self.args1 =str
	def startsingle(self):
		self.processIn = Popen(self.proc ,stderr=PIPE)

	def start(self):
		self.processIn = Popen([self.proc , self.args1],stdout=PIPE,stderr=PIPE)
		self.processOut = Popen([self.proc2 ],stdin=self.processIn.stdout,stderr=PIPE)

		self.processIn.stdout.close()
		self.processOut.communicate()
	'''	
def a():
	s2 = pipeToProcess()
	s2.setproc("/bin/ps")
	s2.setArgsOne("-A")
	s2.setredirectproc("./psJson.py")
	s2.start()

if __name__ == '__main__':
  Parser = argparse.ArgumentParser(description='pipe .')
  Parser.add_argument('process', help='process to serialize')
  Args= Parser.parse_args()

  if Args.process == "ps":
    a()
'''


    