#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)


call('./run-qa.sh',shell=True)
print "=============================TEST 15 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/postmark.log -t postmark',shell=True)
print "Log file : /export/postmark.log"
print "==============================TEST 15 ENDS=============================="

