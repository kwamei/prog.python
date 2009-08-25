#! /usr/bin/env python

import os, pwd, sys

app = os.path.basename(sys.argv[0])
uid = os.getuid()

try:
    pw = pwd.getpwuid(uid)
except KeyError:
    print '%s: failed to find user name for %lu' % (app, uid)
    sys.exit(1)

print pw.pw_name
