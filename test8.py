#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)

call('./run-qa.sh',shell=True)
print "=============================TEST 8 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/fileop.log -t fileop',shell=True)
print "Log file : /export/fileop.log"
print "==============================TEST 8 ENDS=============================="

