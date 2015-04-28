#!/usr/bin/python
import subprocess,os,sys,time
from subprocess import call

original = sys.stdout

def setup(volume,server_ip,client_ip,confile):
	
	 os.environ['server_ip']=server_ip
	 os.environ['volume']=volume
	 os.environ['confile']=confile
	 os.environ['server_ip']=server_ip
         os.environ['client_ip'] = client_ip
         #os.environ['server_pass']=server_pass
         #call('sshpass -p $server_pass ssh-copy-id root@$server_ip',shell=True)
	 call('scp -r copy-to-server $server_ip:/tmp/',shell=True)
	 os.system('ssh -t $server_ip "/tmp/copy-to-server/run1.sh $volume $server_ip $confile" ')

def clean():
	
        call("umount /mnt/ganesha-mnt",shell=True)
	call("rm -rf /mnt/ganesha-mnt",shell=True)
	call("rm -rf /tmp/working-scripts ;rm -rf /tmp/copy.sh",shell=True)

