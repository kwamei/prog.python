#! /usr/bin/env python

import os, pwd, sys

app = os.path.basename(sys.argv[0])
uid = os.getuid()
pw = pwd.getpwuid(uid)

print pw.pw_name
