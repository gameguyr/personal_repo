#!/usr/bin/python

import re

with open (testRe.py) as f:
  source = f.read()

definitions = r ('^(def|Class)\s+([a-zA-Z_0-9]+)\s*\(')

found = re.findall(definitions, source)

print found


