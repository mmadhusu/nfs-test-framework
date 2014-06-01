#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)
from counter import counter
from compare import compare


call('./run-qa.sh',shell=True)
print "=============================TEST 14 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/iozone.log -t iozone >/export/iozone.log',shell=True)
print "Log file : /export/iozone.log"
ret=compare("Total 1 tests were successful","/export/iozone.log")
if ret == 1:
        print "Test 14: PASS"
        counter(1)
else:
        print "Test 14: FAIL"

print "==============================TEST 14 ENDS=============================="

