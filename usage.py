#!/usr/bin/python
import sys
def usage(parameter):
        if parameter == "":
                print 'main.py -s <SERVER-HOST-IP> -c <CLIENT-HOST-IP> -f <CONFIG_FILE> -l [LOG_FILE]-v [NFS_VERSION] -t [TEST] [-n|--nocleanup]'
                sys.exit() 

