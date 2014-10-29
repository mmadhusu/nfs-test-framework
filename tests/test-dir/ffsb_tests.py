#!/usr/bin/python
from subprocess import call
from tests.logger import logger
import sys
log_file=sys.argv[1]
logger(log_file)
from tests.counter import counter
from tests.compare import compare

call('tests/run-qa.sh',shell=True)
print "=============================FFSB TESTS BEGIN============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/ffsb.log -t ffsb > /export/ffsb.log',shell=True)
print "Log file : /export/ffsb.log"
ret=compare("Total 1 tests were successful","/export/ffsb.log")
if ret == 1:
        print "FFSB TESTS                        : PASS"
        counter(1)
else:
        print "FFASB TESTS                       : END"

print "==============================FFSB TESTS END=============================="

