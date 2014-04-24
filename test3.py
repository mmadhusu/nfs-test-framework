#!/usr/bin/python

import subprocess,os,sys,counter,setup,time
from subprocess import call
log_file=sys.argv[5]
class  Logger(object):
        def __init__(self):

                self.terminal = sys.stdout
                self.log = open(log_file, "a")
        def write(self, message):
                self.terminal.write(message)
                self.log.write(message)
sys.stdout =  Logger()
print "==============================TEST 3 : Pynfs tests BEGINS==============="

server_ip=sys.argv[1]
client_ip=sys.argv[2]
confile=sys.argv[3]
known_failures = int (sys.argv[4])
setup.setup("pynfs-test-volume",server_ip,client_ip,confile)
time.sleep(30)
if os.path.isdir("pynfs")== True:
	call('rm -rf pynfs',shell=True)
call(' git clone git://linux-nfs.org/~bfields/pynfs.git',shell=True)
cur = os.getcwd()
os.chdir("pynfs")
call('yes  | python setup.py build >/dev/null 2>/dev/null' ,shell=True)
os.chdir("nfs4.0")

os.environ['server_ip'] = server_ip
time.sleep(45)
ret = call('./testserver.py  -v --outfile ~/pynfs.run.1 --maketree $server_ip:/pynfs-test-volume  --showomit --rundeps  all > /tmp/pynfs-results.log',shell=True)

if  ret:
	print "pynfs tests failed, check logfile for details"
	print " TEST 3 : FAIL"
	print "==============================TEST 3 ENDS================================="
	sys.exit()
os.chdir(cur)

os.system('cat /tmp/pynfs-results.log| grep "Command" | cut -d " " -f5 > /tmp/pynfs-log.txt')
fo = open ('/tmp/pynfs-log.txt','r')
total = int( fo.read())
fo.close()
os.system('cat /tmp/pynfs-results.log| grep "Of those" | cut -d " " -f5 > /tmp/pynfs-log.txt')
fo = open ('/tmp/pynfs-log.txt','r')
failures=int(fo.read())
fo.close()
os.system('cat /tmp/pynfs-results.log| grep "Of those" | cut -d " " -f9 > /tmp/pynfs-log.txt')
fo = open ('/tmp/pynfs-log.txt','r')
passed=int(fo.read())
fo.close()


print "===============================Pynfs tests================================================"
print "TOTAL           : %d " %total
print "FAILURES        : %d " %failures
print "PASS            : %d " %passed
#print "Number of successes is %s" %passed

new_failures = failures - known_failures
if new_failures > 0 :
	if total == "568" :
		print " Test 3 : FAIL "
		print "Check /tmp/pynfs-results.log for results"

else:
	print " Test 3 : PASS "
	counter.counter(1)
print "====================================TEST 3 ENDS=========================================="

