#!/usr/bin/python
import sys,getopt,threading
from subprocess import call
import setup,os,time
from counter import counter
from usage import usage
import header
from mount import mount

server_ip=""
client_ip=""
lfile=""
cleanup=""
confile=""
total=11
known_failures=13
version=""
test_list=list()


argv=sys.argv[1:]
try:
        opts, args = getopt.getopt(argv,"hl:ns:v:c:tf:",["nocleanup"])
except getopt.GetoptError:
        print 'main.py -s <SERVER-HOST-IP> -c <CLIENT-HOST-IP> -f <CONFIG_FILE> -l [LOG_FILE] -t [tests] -v [version][-n|--nocleanup] -'
        sys.exit(2)
for opt, arg in opts:
        if opt == '-h':
                print 'main.py -i <logfile> -n|--nocleanup'
                sys.exit()
        elif  opt in ("-n", "--nocleanup"):
                cleanup =  "yes"
                print "Tests to be run in no cleanup mode"
        elif opt == '-l':
                lfile = arg
        elif opt == '-s':
                server_ip = arg
	elif opt == '-c':
		client_ip = arg
	elif opt == '-f':
		confile = arg
        elif opt == '-t':
		test_list.append(arg)
        elif opt == '-v':
                version = arg
                print "version "
                print version



class  Logger(object):
        def __init__(self):
                self.terminal = sys.stdout
                self.log = open(lfile, "a")
        def write(self, message):
                self.terminal.write(message)
                self.log.write(message)




class myThread (threading.Thread):
	def __init__(self, name):
		threading.Thread.__init__(self)
		self.name = name
		#self.test = test
	def run(self):
		os.system(self.name)

usage(client_ip)
usage(server_ip)
usage(confile)

if lfile == "":
	lfile="/tmp/ganesha.log"
	if os.path.isfile(lfile) == True :
		os.remove(lfile)

sys.stdout = Logger()
header.header_1(lfile)

original = os.getcwd()
#os.system('./copy.sh')
#os.chdir('/tmp/working-scripts/')
setup.setup("ganesha-test-volume",server_ip,client_ip,confile)

#list = ["test1.py","test2.py","test3.py","test4.py","test5.py"]
#list = ["test5.py"]

if not test_list:
        test_list = ["test1.py"]

def run_tests(list):
        for test in list:
	        if test == "test3.py":
		        thread1 = myThread("python %s %s %s %s %d %s " %(test,server_ip,client_ip,confile,known_failures,lfile))
	        else:
		        thread1 = myThread("python %s %s %s " %(test,lfile,server_ip))
                thread1.start()
                thread1.join()

def check_list(test_list):
        if "test3.py" in test_list:
                test_list.remove("test3.py")

if (version == "3" or version==""):
        mount("ganesha-test-volume",server_ip,"3")
        run_tests(test_list)
if (version == "4" or version==""):
        call('umount /mnt/ganesha-mnt',shell=True)
        mount("ganesha-test-volume",server_ip,"4")
        check_list(test_list)
        run_tests(test_list)




passed=counter(0)
os.chdir(original)
os.environ['server_ip']=server_ip
if cleanup == "":
	setup.clean()
	os.system('ssh -t $server_ip "yes | /root/copy-to-server/cleanup.sh" ')

os.system('rm -rf /tmp/counter.txt')

failed = total - passed

print ""
print "==============================Results===================================="
print " Total tests run : %d  " %total
print " Tests passed    : %d  " %passed
print " Tests failed    : %d  " %failed
print "========================================================================="


