#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)
from counter import counter
from compare import compare
call('./run-qa.sh',shell=True)
print "=============================TEST 20 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/locks.log -t locks > /export/locks.log',shell=True)
print "Log file : /export/locks.log"
ret=compare("Total 1 tests were successful","/export/locks.log")
if ret == 1:
        print "Test 20: PASS"
        counter(1)
else:
        print "Test 20: FAIL"

print "==============================TEST 20 ENDS=============================="

