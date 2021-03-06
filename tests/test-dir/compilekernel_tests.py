#!/usr/bin/python
from subprocess import call
from tests.logger import logger
import sys
log_file=sys.argv[1]
logger(log_file)
from tests.counter import counter
from tests.compare import compare


call('tests/run-qa.sh',shell=True)
print "=============================COMPILE_KERNEL TESTS BEGIN=============================="
call('time /opt/qa/tools/system_light/run.sh -w /mnt/ganesha-mnt -l /export/compile_kernel.log -t compile_kernel > /export/compile_kernel.log',shell=True)
print "Log file : /export/compile_kernel.log"
ret=compare("Total 1 tests were successful","/export/compile_kernel.log")
if ret == 1:
        print "COMPILE_KERNEL TESTS              : PASS"
        counter(1)
else:
        print "COMPILE_KERNEL TESTS              : END"

print "==============================COMPILE_KERNEL TESTS END=============================="

