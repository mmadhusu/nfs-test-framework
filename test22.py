#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)
from counter import counter
from compare import compare

call('./run-qa.sh',shell=True)
print "=============================TEST 22 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/tiobench.log -t tiobench >/export/tiobench.log',shell=True)
print "Log file : /export/tiobench.log"
ret=compare("Total 1 tests were successful","/export/tiobench.log")
if ret == 1:
        print "Test 22: PASS"
        counter(1)
else:
        print "Test 22: FAIL"

print "==============================TEST 22 ENDS=============================="

