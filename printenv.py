#! /usr/bin/env python

import os, sys

def printenv(keys):
    for key in keys:
	if key in os.environ:
	    print os.environ[key]

def dumpenv():
    for k, v in os.environ.iteritems():
	print '%s=%s' % (k, v)

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
	printenv(sys.argv[1:])
    else:
	dumpenv()
