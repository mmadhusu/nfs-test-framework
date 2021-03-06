#!/usr/bin/python
from subprocess import call

from tests.logger import logger
import sys
log_file=sys.argv[1]
logger(log_file)
from tests.counter import counter
from tests.compare import compare



call('tests/run-qa.sh',shell=True)
print "=============================LTP TESTS BEGIN============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/ltp.log -t ltp >/export/ltp.log',shell=True)
print "Log file : /export/ltp.log"
ret=compare("Total 1 tests were successful","/export/ltp.log")
if ret == 1:
        print "LTP TESTS                   : PASS"
	counter(1)
else:
        print "LTP TESTS                   : FAIL"

print "==============================LTP TESTS END=============================="

