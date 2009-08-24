#! /usr/bin/env python

import os, sys

app = os.path.basename(sys.argv[0])
argc = len(sys.argv[1:])

if argc == 0:
    print '%s: no command-line arguments.' % app
    sys.exit(0)

print '%s: %d command-line argument%s:' % (app, argc, '' if argc == 1 else 's')

for i, a in enumerate(sys.argv[1:]):
    print '%3d. %s' % (i+1, a)
