#!/usr/bin/python
import os.path
current =  os.getcwd()
print "current = %s" %current


def check_setup(name):
	current = os.getcwd()
	os.chdir('tests')
	test_list = [name + '_setup' + '.py']
	if (os.path.exists(test_list[0])) == False :
		print "Setup file \"%s\" not found in the current directory, exiting." %test_list[0]
		os.chdir(current)
		exit(1)
	else:
		os.chdir(current)

	
	

