#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]
from counter import counter
from compare import compare


logger(log_file)
call('./run-qa.sh',shell=True)
print "=============================TEST 6 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/arequal.log -t arequal > /export/arequal.log',shell=True)
print "Log file : /export/arequal.log"
ret=compare("Total 1 tests were successful","/export/arequal.log")
if ret == 1:
        print "Test 6: PASS"
        counter(1)
else:
        print "Test 6: FAIL"

print "==============================TEST 6 ENDS=============================="

