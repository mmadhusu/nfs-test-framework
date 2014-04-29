#!/usr/bin/python
import os
import glob
import re

f=[]
f1=[]
for file in glob.glob("test*.py"):
        print file
        f.append(file)
for test in f:
        f1.append(os.path.splitext(test)[0])
#print f1[0:]
complete_test_list = sorted(f1, key = lambda x: int(x.split("test")[1]))
complete_test_list = [test + '.py' for test in complete_test_list]




def check_list(test_list, version):
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


