#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)
from counter import counter
from compare import compare



call('./run-qa.sh',shell=True)
print "=============================TEST 9 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/glusterfs_build.log -t glusterfs_build > /export/glusterfs_build.log',shell=True)
print "Log file : /export/glusterfs_build.log"
ret=compare("Total 1 tests were successful","/export/glusterfs_build.log")
if ret == 1:
        print "Test 9: PASS"
        counter(1)
else:
        print "Test 9: FAIL"
print "==============================TEST 9 ENDS=============================="

