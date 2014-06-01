#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]
from counter import counter
from compare import compare

logger(log_file)
from counter import counter
from compare import compare


call('./run-qa.sh',shell=True)
print "=============================TEST 15 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt -l /export/postmark.log -t postmark > /export/postmark.log',shell=True)
print "Log file : /export/postmark.log"
ret=compare("Total 1 tests were successful","/export/postmark.log")
if ret == 1:
	print "Test 15: PASS"
	counter(1)
else:
	print "Test 15: FAIL"
print "==============================TEST 15 ENDS=============================="

