#!/usr/bin/python
from subprocess import call
from tests.logger import logger
import sys
log_file=sys.argv[1]
logger(log_file)
from tests.counter import counter
from tests.compare import compare


call('tests/run-qa.sh',shell=True)
print "=============================SYSCALL TESTS BEGIN============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/syscall.log -t syscallbench > /export/syscall.log',shell=True)
print "Log file : /export/syscall.log"
ret=compare("Total 1 tests were successful","/export/syscall.log")
if ret == 1:
        print "SYSCALL TESTS                   : PASS"
        counter(1)
else:
        print "SYSCALL TESTS                   : FAIL"

print "==============================SYSCALL TESTS END=============================="

