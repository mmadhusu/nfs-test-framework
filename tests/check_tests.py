#!/usr/bin/python
import os
import glob
import re


def check_list(test_list, version):
	current = os.getcwd()
	complete_test_list=[]
	os.chdir("tests/test-dir")
	for file in glob.glob("*.py"):
        	#print file
        	complete_test_list.append(file)
	os.chdir(current)
	print complete_test_list[0:]
        if test_list:
                test_list = [test + '.py' for test in test_list]
                for test in test_list:
                        if test not in complete_test_list:
                                print "%s is not a valid test, skipping it." %test
                                test_list.remove(test)
                if (version == "3" and "test3.py" in test_list):
                        print "pynfs is a v4 specific test, skipping  it."
                        test_list.remove("test3.py")
        else:
                test_list.extend(complete_test_list)
        return test_list


