#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)
from counter import counter
from compare import compare


call('./run-qa.sh',shell=True)
print "=============================TEST 11 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/posix.log -t posix_compliance > /export/posix.log',shell=True)
print "Log file : /export/posix.log"
ret=compare("Total 1 tests were successful","/export/posix.log")
if ret == 1:
        print "Test 11: PASS"
        counter(1)
else:
        print "Test 11: FAIL"

print "==============================TEST 11 ENDS=============================="

