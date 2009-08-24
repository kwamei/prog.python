#! /usr/bin/env python

import sys
from os.path import basename, dirname

print 'Script name: %s' % basename(sys.argv[0])
print 'Script path: %s' % dirname(sys.argv[0])
