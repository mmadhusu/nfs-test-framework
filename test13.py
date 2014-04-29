#!/usr/bin/python
from subprocess import call
from logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)


call('./run-qa.sh',shell=True)
print "=============================TEST 13 BEGINS============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/multiple_files.log -t multiple_files',shell=True)
print "Log file : /export/multiple_files.log"
print "==============================TEST 13 ENDS=============================="

