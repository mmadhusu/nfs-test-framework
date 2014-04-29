#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)


call('./run-qa.sh',shell=True)
print "=============================TEST 12 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/dd.log -t dd',shell=True)
print "Log file : /export/dd.log"
print "==============================TEST 12 ENDS=============================="

