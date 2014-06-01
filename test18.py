#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)
from counter import counter
from compare import compare

call('./run-qa.sh',shell=True)
print "=============================TEST 18 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/ffsb.log -t ffsb > /export/ffsb.log',shell=True)
print "Log file : /export/ffsb.log"
ret=compare("Total 1 tests were successful","/export/ffsb.log")
if ret == 1:
        print "Test 18: PASS"
        counter(1)
else:
        print "Test 18: FAIL"

print "==============================TEST 18 ENDS=============================="

