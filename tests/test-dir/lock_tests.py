#!/usr/bin/python
from subprocess import call
from tests.logger import logger
import sys
log_file=sys.argv[1]

logger(log_file)
from tests.counter import counter
from tests.compare import compare
call('tests/run-qa.sh',shell=True)
print "=============================LOCK TESTS BEGIN============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/locks.log -t locks > /export/locks.log',shell=True)
print "Log file : /export/locks.log"
ret=compare("Total 1 tests were successful","/export/locks.log")
if ret == 1:
        print "LOCK TESTS                     : PASS"
        counter(1)
else:
        print "LOCK TESTS                     : FAIL"

print "==============================LOCK TESTS END=============================="

