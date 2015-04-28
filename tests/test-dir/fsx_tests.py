#!/usr/bin/python
from subprocess import call
from tests.logger import logger
import sys
log_file=sys.argv[1]
logger(log_file)
from tests.counter import counter
from tests.compare import compare

call('tests/run-qa.sh',shell=True)
print "=============================FSX TESTS BEGIN============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/fsx.log -t fsx > /export/fsx.log',shell=True)
print "Log file : /export/fsx.log"
ret=compare("Total 1 tests were successful","/export/fsx.log")
if ret == 1:
        print "FSX TESTS                     : PASS"
        counter(1)
else:
        print "FSX TESTS                     : FAIL"

print "==============================FSX TESTS END=============================="

