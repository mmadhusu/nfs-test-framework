#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)
from counter import counter
from compare import compare


call('./run-qa.sh',shell=True)
print "=============================TEST 8 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/fileop.log -t fileop > /export/fileop.log',shell=True)
print "Log file : /export/fileop.log"
ret=compare("Total 1 tests were successful","/export/fileop.log")
if ret == 1:
        print "Test 8: PASS"
        counter(1)
else:
        print "Test 8: FAIL"

print "==============================TEST 8 ENDS=============================="

