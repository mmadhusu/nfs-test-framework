#!/usr/bin/python
import os
from subprocess import call


if os.path.isdir('/opt') == False:
	os.mkdir('/opt')
print "==============================TEST 6 BEGINS============================="
#=========Running tests run by QA================#
call('./run-qa.sh',shell=True)
f = open('/export/tests_failed','r')
print f.read()
f.close()
if '21' in open('/export/tests_failed').read():
	print "TEST 5 : PASS"
	#counter(1)
else:
	print "TEST 5 : FAIL"

print "==============================TEST 6 ENDS==============================="




