#! /usr/bin/env python

import os

for elem in os.environ['PATH'].split(os.pathsep):
    print elem
