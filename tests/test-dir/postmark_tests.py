#!/usr/bin/python
from subprocess import call
from tests.logger import logger
import sys
log_file=sys.argv[1]
from tests.counter import counter
from tests.compare import compare
logger(log_file)


call('tests/run-qa.sh',shell=True)
print "=============================POSTMARK TESTS BEGIN============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt -l /export/postmark.log -t postmark > /export/postmark.log',shell=True)
print "Log file : /export/postmark.log"
ret=compare("Total 1 tests were successful","/export/postmark.log")
if ret == 1:
	print "POSTMARK TESTS                : PASS"
	counter(1)
else:
	print "POSTMARK TESTS                : FAIL"
print "==============================POSTMARK TESTS END=============================="

