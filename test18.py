#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)

call('./run-qa.sh',shell=True)
print "=============================TEST 18 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/ffsb.log -t ffsb',shell=True)
print "Log file : /export/ffsb.log"
print "==============================TEST 18 ENDS=============================="

