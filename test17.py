#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)
from counter import counter
from compare import compare


call('./run-qa.sh',shell=True)
print "=============================TEST 17 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/compile_kernel.log -t compile_kernel > /export/compile_kernel.log',shell=True)
print "Log file : /export/syscall.log"
ret=compare("Total 1 tests were successful","/export/compile_kernel.log")
if ret == 1:
        print "Test 17: PASS"
        counter(1)
else:
        print "Test 17: FAIL"

print "==============================TEST 17 ENDS=============================="

