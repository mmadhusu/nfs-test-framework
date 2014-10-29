#!/usr/bin/python
from subprocess import call
from tests.logger import logger
import sys
log_file=sys.argv[1]
logger(log_file)
from tests.counter import counter
from tests.compare import compare


call('tests/run-qa.sh',shell=True)
print "=============================POSIX COMPLIANCE TESTS BEGIN============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/posix.log -t posix_compliance > /export/posix.log',shell=True)
print "Log file : /export/posix.log"
ret=compare("Total 1 tests were successful","/export/posix.log")
if ret == 1:
        print "POSIX COMPLIANCE TESTS                  : PASS"
	counter(1)
else:
        print "POSIC COMPLIANCE TESTS                  : END"

print "==============================POSIX COMPLIANCE TESTS END=============================="

