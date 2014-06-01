#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)
from counter import counter
from compare import compare


call('./run-qa.sh',shell=True)
print "=============================TEST 16 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/syscall.log -t syscallbench > /export/syscall.log',shell=True)
print "Log file : /export/syscall.log"
ret=("Total 1 tests were successful","/export/syscall.log")
if ret == 1:
        print "Test 16: PASS"
        counter(1)
else:
        print "Test 16: FAIL"

print "==============================TEST 16 ENDS=============================="

