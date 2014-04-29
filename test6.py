#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)
call('./run-qa.sh',shell=True)
print "=============================TEST 6 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/arequal.log -t arequal',shell=True)
print "Log file : /export/arequal.log"
print "==============================TEST 6 ENDS=============================="

