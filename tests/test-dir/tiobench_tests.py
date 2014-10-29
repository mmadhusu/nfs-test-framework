#!/usr/bin/python
from subprocess import call
from tests.logger import logger
import sys
log_file=sys.argv[1]
logger(log_file)
from tests.counter import counter
from tests.compare import compare

call('tests/run-qa.sh',shell=True)
print "=============================TIOBENCH TESTS BEGIN============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/tiobench.log -t tiobench >/export/tiobench.log',shell=True)
print "Log file : /export/tiobench.log"
ret=compare("Total 1 tests were successful","/export/tiobench.log")
if ret == 1:
        print "TIOBENCH TESTS                       : PASS"
        counter(1)
else:
        print "TIOBENCH TESTS                       : FAIL"

print "=============================TIOBENCH TESTS END=============================="

