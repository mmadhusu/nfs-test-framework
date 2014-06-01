#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)
from counter import counter
from compare import compare

call('./run-qa.sh',shell=True)
print "=============================TEST 19 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/fsx.log -t fsx > /export/fsx.log',shell=True)
print "Log file : /export/fsx.log"
ret=compare("Total 1 tests were successful","/export/fsx.log")
if ret == 1:
        print "Test 19: PASS"
        counter(1)
else:
        print "Test 19: FAIL"

print "==============================TEST 19 ENDS=============================="

