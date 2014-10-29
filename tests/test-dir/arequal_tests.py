#!/usr/bin/python
from subprocess import call
import sys
log_file=sys.argv[1]
from tests.counter  import counter
from tests.compare import compare
from tests.logger import logger

logger(log_file)
call('.tests/run-qa.sh',shell=True)
print "=============================AREQUAL TESTS BEGIN============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/arequal.log -t arequal > /export/arequal.log',shell=True)
print "Log file : /export/arequal.log"
ret=compare("Total 1 tests were successful","/export/arequal.log")
if ret == 1:
        print "AREQUAL TESTS                   : PASS"
        counter(1)
else:
        print "AREQUAL TESTS                   : FAIL"

print "==============================AREQUAL TESTS END=============================="

