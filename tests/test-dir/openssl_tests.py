#!/usr/bin/python
from subprocess import call
from tests.logger import logger
import sys
log_file=sys.argv[1]
logger(log_file)
from tests.counter import counter
from tests.compare import compare
call('tests/run-qa.sh',shell=True)
print "=============================OPENSSL TESTS BEGIN============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/openssl.log -t openssl >/export/openssl.log',shell=True)
print "Log file : /export/openssl.log"
ret=compare("Total 1 tests were successful","/export/openssl.log")
if ret == 1:
        print "OPENSSL TESTS                   : PASS"
        counter(1)
else:
        print "OPENSSL TESTS                   : FAIL"

print "==============================OPENSSL TESTS END=============================="

