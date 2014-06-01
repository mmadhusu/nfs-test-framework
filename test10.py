#!/usr/bin/python
from subprocess import call

from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)
from counter import counter
from compare import compare



call('./run-qa.sh',shell=True)
print "=============================TEST 10 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/ltp.log -t ltp >/export/ltp.log',shell=True)
print "Log file : /export/ltp.log"
ret=compare("Total 1 tests were successful","/export/ltp.log")
if ret == 1:
        print "Test 10: PASS"
        counter(1)
else:
        print "Test 10: FAIL"

print "==============================TEST 10 ENDS=============================="

