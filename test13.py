#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)
from counter import counter
from compare import compare


call('./run-qa.sh',shell=True)
print "=============================TEST 13 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/multiple_files.log -t multiple_files >/export/multiple_files.log',shell=True)
print "Log file : /export/multiple_files.log"
ret=compare("Total 1 tests were successful","/export/multiple_files.log")
if ret == 1:
        print "Test 13: PASS"
        counter(1)
else:
        print "Test 13: FAIL"

print "==============================TEST 13 ENDS=============================="

