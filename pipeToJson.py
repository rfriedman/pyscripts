#!/usr/bin/python
from subprocess import Popen, PIPE
import argparse

class pipeToProcess(object):
	''' need to accomodate:
	ssh {user}@{hostlist} 'ssh-keygen' 2>>error.log
	cat .ssh/id_rsa.pub | ssh {user}@{hostlist} 'cat >> ~/.ssh/authorized_keys'
	ssh {user}@{hostlist} 'cat ~/.ssh/id_rsa.pub' | cat >> ~/.ssh/authorized_keys
	cat hostinfo.sh | ssh {user}@{hostlist} 'cat >> ~/hostinfo.sh &&
	 sudo cp ~/hostinfo.sh /usr/local/sbin &&
	 rm ~/hosinfo.sh'
	cat /etc/crontab | ssh {user}@{hostlist} 'cat >> ~/crontab &&
	 sudo cp ~/crontab /etc/crontab &&
	 rm ~/crontab'
	'''
	def __init__(self,procfile, hostfile):
		self.processlist = procfile.readlines()
		self.hostlist = hostfile.readlines()
		self.inlist = list()
		self.outlist = list()
		self.procinlist()
		self.batch = dict()
		self.node = dict()
		self.user = self.hostlist[0]
	def createbatch(self,proc1):
		"""create batch as:
		{
				{"hostlist":[{pi@192.168.0.1},{pi@192.168.0.2}],
				 "joblist":[{"cmd":ssh,"args":"{host} 'ssh-keygen' 2>>error.log}]
		}

		"""
		self.node = dict()
		del self.hostlist[0]
		self.batch['hostlist']=[]
		self.batch['joblist'] =[]:
			self.batch['hostlist'].append(self.user + '@'+ host)
		__cnt = 0
		cmd=''
		arglist=''
		for proc in proc1:
			args = proc.split()
			for a in args:
				if __cnt==0:
					cmd=a
				if cnt > 0:
					arglist=arglist + ' ' + a	
				cnt = cnt + 1
		self.node['cmd']=cmd
		self.node['args']=argslist
		self.batch['joblist'].append(node)
		
		
	def keygen(self):
		for host in self.hostslist:
			self.setproc(self.inlist[0])


	def procinlist(self):
		'''inlist()'''
		lst = self.processlist.split('|')
		cnt = 0
		for line in lst:
			cnt = cnt+1
			if cnt % 2 == 0:
				self.outlist.append(line)
			else:
				self.inlist.append(line)
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



    